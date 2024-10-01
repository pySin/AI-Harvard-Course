import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


corpus = {
    "1.html": {"2.html", "3.html"},
    "2.html": {"3.html"},
    "3.html": {"2.html"}
}

def transition_model(corpus, page, damping_factor):
    pass