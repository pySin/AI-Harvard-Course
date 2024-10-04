import random as rd
import pytest as pt

from pagerank import DAMPING, crawl, iterate_pagerank, sample_pagerank

TOLERANCE = 1e-3  # Error tolerance = ±0.001 when comparing sample and iterate results
SAMPLES = 10 ** 6  # More samples => better result


