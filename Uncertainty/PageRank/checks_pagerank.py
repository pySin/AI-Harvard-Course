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
    visit_probabilities = {x: round((1 - damping_factor) / len(corpus), 3) for x in corpus}
    visit_probabilities = {x: visit_probabilities[x] + (damping_factor / len(links))
                           if x in links else visit_probabilities[x]
                           for x in visit_probabilities}
    print(visit_probabilities)


transition_model(corpus_1, page_1, DAMPING)
