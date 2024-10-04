import random as rd
import pytest as pt

from pagerank import DAMPING, crawl, iterate_pagerank, sample_pagerank

TOLERANCE = 1e-3  # Error tolerance = ±0.001 when comparing sample and iterate results
SAMPLES = 10 ** 6  # More samples => better result


corpus0 = crawl("corpus0")


def test_crawl0():
    assert len(corpus0) == 4


def test_iterate0():
    expected = {"1.html": 0.2202, "2.html": 0.4289, "3.html": 0.2202, "4.html": 0.1307}
    iterate = iterate_pagerank(corpus0, damping_factor=DAMPING)
    return compare(iterate, expected)


@pt.mark.parametrize("execution_number", range(10))
def test_sample_vs_iterate(execution_number):
    return run_sample_vs_iterate()


# additional functions
def checksum(probability):
    assert sum(probability.values()) == pt.approx(1, abs=TOLERANCE)


