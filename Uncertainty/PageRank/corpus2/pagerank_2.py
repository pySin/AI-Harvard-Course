import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    print(f"Sample Corpus: {corpus}")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    # print(f"Corpus: {corpus}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """

    probability_distribution = {}

    # No link page scenario
    if len(corpus[page]) == 0:
        probability_distribution = {probability_distribution[name]: 1 / len(corpus)
                                    for name in corpus.keys()}

    # Links present in target page
    else:
        probability_distribution = {name: (1 - damping_factor) / len(corpus) for name in corpus.keys()}
        for k in probability_distribution.keys():
            if k in corpus[page]:
                probability_distribution[k] += damping_factor / len(corpus[page])
    return probability_distribution

    # links = corpus[page]
    # # return equal probabilities 15% of the time and distributed probabilities 85% of the time
    # num_generate_0_to_1 = random.random()
    # if len(links) == 0:
    #     if num_generate_0_to_1 < 1 - damping_factor:
    #         visit_probabilities = {x: 1 / len(corpus) for x in corpus}
    #     else:
    #         visit_probabilities = None
    # elif num_generate_0_to_1 <= 1 - damping_factor:
    #     visit_probabilities = {x: 1 / len(corpus) for x in corpus}
    # else:
    #     visit_probabilities = {x: 1 / len(links) for x in links}
    # # print(links)
    # # visit_probabilities = {x: round((1 - damping_factor) / len(corpus), 3) for x in corpus}
    # return visit_probabilities




def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    current_page = random.choice([x for x in corpus])
    page_visits = {x: 0 for x in corpus}

    for i in range(n):
        page_visit_chances = transition_model(corpus, current_page, damping_factor)
        if not page_visit_chances:
            continue

        lower_range = 0
        random_0_to_1 = random.random()

        for key, value in page_visit_chances.items():
            if lower_range < random_0_to_1 < lower_range + value:
                page_visits[key] += 1
                current_page = key
                break
            else:
                lower_range += value

        print(f"Page Visit Chances: {page_visit_chances}")
    all_visits = sum([x for x in page_visits.values()])
    page_ranks = {x: page_visits[x] / all_visits for x in page_visits}
    return page_ranks


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    page_ranks = {r: 1 / len(corpus) for r in corpus}
    stable_ratings = False

    while not stable_ratings:
        stable_ratings = True

        for page_name, page_rank in page_ranks.items():
            if not corpus[page_name]:
                corpus[page_name] = set(page_ranks.keys())
            link_weight = damping_factor * (sum([page_ranks[lr] / len(corpus[lr]) for lr in corpus
                                                if lr != page_name
                                                and page_name in corpus[lr]]))
            new_page_rank = (1 - damping_factor / len(corpus)) + link_weight

            if not (page_rank - 0.001) < new_page_rank < (page_rank + 0.001):
                stable_ratings = False
            page_ranks[page_name] = new_page_rank

    page_ranks_sum = sum([pr for pr in page_ranks.values()])
    page_ranks = {pr: (page_ranks[pr] / page_ranks_sum) for pr in page_ranks}
    return page_ranks


if __name__ == "__main__":
    main()
