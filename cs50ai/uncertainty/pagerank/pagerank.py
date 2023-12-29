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

    # dictionary mapping page to prob
    probability_dist = {page: 0 for page in corpus}

    # chance to go to random page in corpus
    r = 1 - damping_factor
    for page in corpus:
        # handle imprecision
        probability_dist[page] += (r * 100 ) / (len(corpus) * 100)

    # linked pages
    linked = corpus[page]

    if len(linked) == 0:
        probability_dist[link] = damping_factor / len(corpus)

    for link in linked:
        probability_dist[link] += damping_factor / len(linked)

    return probability_dist


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    page_rank = dict()
    visited = dict() # count times visited
    for page in corpus:
        page_rank[page] = 0
        visited[page] = 0

    # start on random page from corpus
    curr_page = random.choice(list(corpus.keys()))
    visited[curr_page] += 1
    
    for i in range(n - 1):
        r = random.random()
        if r <= 1 - damping_factor:
            curr_page = random.choice(list(corpus.keys()))
            visited[curr_page] += 1
        else:
            model = transition_model(corpus, curr_page, damping_factor)
            # select random page based on transition model
            links, weights = zip(*model.items())
            curr_page = random.choices(links, weights=weights, k=1)[0]
            visited[curr_page] += 1
    
    for page, visits in visited.items():
        # print(page)
        # print(visits)
        # print()
        page_rank[page] = visits / n

    return page_rank

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    page_rank = {}
    n = len(corpus)

    for page in corpus:
        page_rank[page] = 1 / n
    
    diff = True
    while diff:
        diff = False
        for page in corpus:
            sum = 0
            for p, links in corpus.items():
                if len(links) == 0:
                    sum += page_rank[p] / n
                elif page in links:
                    sum += page_rank[p] / len(links)
                
            new_rank = (1 - damping_factor) / n + damping_factor * sum
            if abs(page_rank[page] - new_rank) > 0.001:
                diff = True
                page_rank[page] = new_rank
            
    return page_rank


if __name__ == "__main__":
    main()