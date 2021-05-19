import time
from itertools import permutations
from math import factorial

def distance(point_1, point_2):
    return (point_1[0] - point_2[0])**2 + (point_1[1] - point_2[1])**2

def distance_path(cities, path):
    n = len(cities)
    return sum(distance(cities[path[i]], cities[path[(i+1)%n]]) for i in range(n))

def estimate_time(n, precision=100_000):
    nPermutations = factorial(n)
    precision = precision if nPermutations > precision else nPermutations
    permutation_generator = permutations(range(n))
    start = time.time()
    for _ in range(precision):
        next(permutation_generator)
    stop = time.time()
    return (stop - start) * (nPermutations/precision)
