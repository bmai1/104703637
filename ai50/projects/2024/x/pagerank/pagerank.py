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
        pages[filename] = set(link for link in pages[filename] if link in pages)

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
    for p in corpus:
        # handle imprecision
        probability_dist[p] += (r * 100) / (len(corpus) * 100)

    # linked pages
    linked = corpus[page]

    if len(linked) == 0:
        for p in corpus:
            probability_dist[p] += damping_factor / len(corpus)

    for link in linked:
        probability_dist[link] += damping_factor / len(linked)

    # print(probability_dist)
    return probability_dist


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    page_rank = {page: 0 for page in corpus}

    # start on random page from corpus
    curr_page = random.choice(list(corpus.keys()))
    # print(curr_page)
    page_rank[curr_page] += 1
    
    for page in range(n - 1):
        r = random.random()

        if r <= 1 - damping_factor:
            curr_page = random.choice(list(corpus.keys()))
        else:
            model = transition_model(corpus, curr_page, damping_factor)
            links, weights = zip(*model.items())
            curr_page = random.choices(links, weights=weights, k=1)[0]

        page_rank[curr_page] += 1
    
    for page in page_rank:
        # print(page)
        # print(page_rank[page])
        # print()
        page_rank[page] /= n

    return page_rank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    n = len(corpus)
    page_rank = {page: 1 / n for page in corpus}
    new_rank = {}
    
    flag = False
    while not flag:
        for page in corpus:
            # print(page_rank)
            sum = 0
            for p in corpus:
                if len(corpus[p]) == 0:
                    sum += page_rank[p] / n
                elif page in corpus[p]:
                    sum += page_rank[p] / len(corpus[p])
                
            new_rank[page] = (1 - damping_factor) / n + (damping_factor * sum)

        for page in corpus:
            # <= 0.001 fails complex corpus
            if abs(page_rank[page] - new_rank[page]) <= 0.0001:
                flag = True
            page_rank[page] = new_rank[page]
            # if flag:
            #     break
            
    return page_rank


if __name__ == "__main__":
    main()
