import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


corpus_1 = {
    "1.html": {"2.html", "3.html"},
    "2.html": {"3.html"},
    "3.html": {"2.html"}
}

page_1 = "1.html"


def transition_model(corpus, page, damping_factor):
    links = corpus[page]
    print(links)


transition_model(corpus_1, page_1, DAMPING)
