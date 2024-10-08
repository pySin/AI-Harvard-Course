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
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


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

    # No link page scenario
    if len(corpus[page]) == 0:
        probability_distribution = {key: 1 / len(corpus.keys()) for key in corpus.keys()}

    # Links present in target page
    else:
        probability_distribution = {name: (1 - damping_factor) / len(corpus) for name in corpus.keys()}
        for k in probability_distribution.keys():
            if k in corpus[page]:
                probability_distribution[k] += damping_factor / len(corpus[page])

    return probability_distribution


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    page_ranks = {s: 0 for s in corpus}
    current_page = random.choice(list(corpus.keys()))
    n -= 1

    # collecting results through iteration
    for i in range(n):
        probability_distribution = transition_model(corpus, current_page, damping_factor)
        r_number = random.random()
        lower_range_v = 0
        for key, value in probability_distribution.items():
            if lower_range_v < r_number < lower_range_v + value:
                current_page = key
                page_ranks[key] += 1
            lower_range_v += value

    n += 1
    for key, value in page_ranks.items():
        page_ranks[key] = value / n

    return page_ranks


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pages_number = len(corpus)
    # Create an empty dictionary pages names
    old_dict = {r: 1 / len(corpus) for r in corpus}

    # Set variable to track changes of page probabilities
    stable_ratings = False

    # Reassign page ranks until criteria is met.
    while not stable_ratings:
        stable_ratings = True
        for main_page in corpus:
            current_page_rank = 0
            for page_link in corpus:
                # check if page links to our page
                if main_page in corpus[page_link]:
                    current_page_rank = current_page_rank + (damping_factor *
                                                             (old_dict[page_link] / len(corpus[page_link])))
                if len(corpus[page_link]) == 0:
                    current_page_rank = current_page_rank + \
                                        (damping_factor * (old_dict[page_link]) / len(corpus))
            current_page_rank += (1 - damping_factor) / pages_number
            ranking_difference = abs(old_dict[main_page] - current_page_rank)
            if ranking_difference > 0.001:
                stable_ratings = False
            old_dict[main_page] = current_page_rank

    return old_dict


if __name__ == "__main__":
    main()
