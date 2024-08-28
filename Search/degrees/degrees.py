# Degrees Harvard SC50 AI
import csv
import sys
import util


from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"
    # directory = sys.argv[1] if len(sys.argv) == 2 else "small"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    # print(source)
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")
    # print(target)
    # print(f"Names: {names}")
    # print(f"People: {people}")
    # print(f"Movies: {movies}")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        print(f"Path: {path}")
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """
    print(f"Source: {source}")
    print(f"Target: {target}")

    neighbours = neighbors_for_person(source)
    action = {n[1] for n in neighbours if n[1] != source}
    first_node = Node((source, ), "first_node_parent", action)
    if target in action:
        target_data = [d for d in neighbours if d[1] == target]
        return target_data

    frontier = QueueFrontier()
    frontier.add(first_node)  # OK: 158, "first_node_parent", {'102', '705', '641', '200', '398'}
    #stars_checked = list(action)
    #stars_checked.append(source)
    stars_checked = {source}

    degrees = 0
    while True:
        states = []
        source_reached = False
        if frontier.empty():
            return None
        degrees += 1
        node = frontier.remove()
        # print(f"Current Frontier State: {node.state}")
        for artist_id in node.action:
            if artist_id in stars_checked:
                continue
            neighbours = neighbors_for_person(artist_id)
            # print(f"Artist ID: {artist_id}")
            # print(f"Stars Checked: {stars_checked}")
            # print(f"Neighbours: {neighbours}")
            linking_movie = {mp[0] for mp in neighbours if mp[1] == node.state[-1]}.pop()
            stars_checked.add(artist_id)
            action = {s[1] for s in neighbours if s[1] not in stars_checked}
            # print(f"Current Action: {action}")
            if not action:
                # print(f"Not Action!")
                continue
            # print(f"New Stars: {action}") # Demi Moore
            # action = {s[1] for s in neighbours} # Ursula Andress
            new_node = Node((linking_movie, artist_id), node, action)
            frontier.add(new_node)
            if target in new_node.action:
                # print(f"Target {people[target]['name']} Found in: {new_node.state}")
                final_movie = [movie for movie in movies if target
                               in movies[movie]["stars"] and artist_id in movies[movie]["stars"]][0]
                # print(f"Final Movie: {final_movie}")
                while True:
                    # print(f"New node data: {new_node.state}, {new_node.parent}, {new_node.action}")
                    # states.append(new_node.state)
                    states.insert(0, new_node.state)
                    new_node = new_node.parent
                    # print(f"New Node State: {new_node.state}")
                    if new_node.parent == "first_node_parent":
                        print(f"Source Reached: {new_node.state}")
                        states.append((final_movie, target))
                        print(f"Stars Checked: {stars_checked}")
                        print(f"Length Stars Checked: {len(stars_checked)}")
                        return states  # Fix improper record shift
                        # return [('101523', '5460'), ('80025', '1831'), ('66212', '266')]

        # print(f"Stars Checked: {stars_checked}")
        # [print(f.state, f.parent.state, f.action) for f in frontier.frontier]
        if degrees == 6:
            break

    return None


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
