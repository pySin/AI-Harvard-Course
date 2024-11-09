import sys
import copy
from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """

        for var in self.domains.keys():
            # length of crossword line
            length = var.length
            # remove words with different length
            current_words = copy.deepcopy(self.domains[var])
            for w in current_words:
                if len(w) != length:
                    self.domains[var].remove(w)

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """

        x_ovp_index = self.crossword.overlaps[x, y][0]
        y_ovp_index = self.crossword.overlaps[x, y][1]

        domain_x_start = len(self.domains[x])

        for x_domain_member in copy.deepcopy(self.domains[x]):
            self.domains[x].remove(x_domain_member)
            # iterate through words in y's domain
            for y_domain_member in self.domains[y]:
                if x_domain_member[x_ovp_index] == y_domain_member[y_ovp_index]:
                    self.domains[x].add(x_domain_member)
                    break

        # True id there was revision
        return domain_x_start != len(self.domains[x])

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        if not arcs:
            # add overlapping cells if not given
            arcs = []
            for v1_domain in self.domains:
                # find overlapping words
                current_neighbours = self.crossword.neighbors(v1_domain)
                for neighbour in current_neighbours:
                    arcs.append((v1_domain, neighbour))

        self.revise(arcs[0][0], arcs[0][1])

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        for found_word in self.domains:
            if found_word not in assignment:
                return False
        return True

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """

        # word-length check
        if len(assignment) != len(set(assignment.values())):
            return False

        # cross-sections check
        for var_item in assignment:
            for neighbour in self.crossword.neighbors(var_item):
                if neighbour in assignment:
                    row, col = self.crossword.overlaps[var_item, neighbour]
                    if assignment[var_item][row] != assignment[neighbour][col]:
                        return False

        # check successful
        return True

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """

        ruled_out_dict = {}

        neighbours = self.crossword.neighbors(var)

        for neighbour in neighbours:
            sub_neighbours = self.crossword.neighbors(neighbour)
            ruled_out_dict[neighbour] = len(sub_neighbours)

        ordered_rod = sorted(ruled_out_dict, key=lambda x: ruled_out_dict[x], reverse=True)
        words_order = [assignment[v] for v in ordered_rod]

        return words_order

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """

        min_var = None

        for variable in self.domains:
            if variable not in assignment:
                if min_var is None:
                    min_var = variable

                if len(self.domains[variable]) < len(self.domains[min_var]):
                    min_var = variable

        return min_var

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """

        for _ in range(len(self.domains)):
            min_var = self.select_unassigned_variable(assignment)
            for word_value in self.domains[min_var]:
                assignment[min_var] = word_value
                if self.consistent(assignment):
                    neighbours = self.crossword.neighbors(min_var)
                    for neighbour in neighbours:
                        self.revise(min_var, neighbour)
                    break

        if assignment == {}:
            return None
        return assignment


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
