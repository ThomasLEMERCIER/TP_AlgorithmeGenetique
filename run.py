import time
import random
from tqdm import tqdm

import matplotlib.pyplot as plt
import numpy as np

from ga import GA
from individual_path import Individual_path
from individual_vector import Individual_vector
from test_functions import *
from tsp import distance_path, estimate_time

def function_optimization(function, nEpochs, shape, pop_size, mutation_rate, crossover_rate, starting_interval, render=True):

    fitness_function = lambda x : -function(x) * 1e-3

    algo_gen = GA(Individual_vector, fitness_function, shape, pop_size, mutation_rate, crossover_rate, starting_interval)

    top = time.time()

    for e in tqdm(range(nEpochs)):

        algo_gen.step()

    stop = time.time()

    print(f"\nTime elapsed : {stop-top:.3f}s")

    result = function(algo_gen.best_indv.chromosome, render)

    return algo_gen.best_indv.chromosome, result

def tsp(nEpochs, shape, pop_size, mutation_rate, crossover_rate, method='random', estimated_time=True, render=True):

    if method == 'random':
        cities = np.array([[random.random()*100, random.random()*100] for _ in range(shape)])
    elif method == 'square':
        if (root_nCities := int(shape ** (1/2))) ** 2 == shape:
            cities = np.array([[x, y] for x in range(root_nCities) for y in range(root_nCities)])
        else:
            raise ValueError(f"To use the square method the shape must be a perfect square : {shape}")
    elif method == 'polynomial':
        x = np.linspace(-1, 1, shape)
        y = x**2
        cities = np.stack((x, y), axis=-1)
    else:
        NotImplementedError(f"The following method to create cities is not implemented : {method}")

    fitness_function = lambda x: 1/(1+distance_path(cities, x))

    algo_gen = GA(Individual_path, fitness_function, shape, pop_size, mutation_rate, crossover_rate)

    plt.figure()
    plt.ion()

    top = time.time()

    for e in tqdm(range(nEpochs)):

        algo_gen.step()

        best_path = algo_gen.best_indv.chromosome
        if render and e % (nEpochs//10) == 0:
            plt.clf()
            plt.plot(cities[:, 0], cities[:, 1], "ro")
            for k in range(shape):
                plt.plot([cities[best_path[k], 0], cities[best_path[(k+1)%shape], 0]],
                         [cities[best_path[k], 1], cities[best_path[(k+1)%shape], 1]],)
            plt.show()
            plt.pause(1e-3)

    stop = time.time()

    plt.close()
    plt.ioff()

    print(f"\nTime elapsed : {stop-top:.3f}s")


    if render:
        plt.figure()
        plt.plot(cities[:, 0], cities[:, 1], "ro")
        for k in range(shape):
            plt.plot(   [cities[best_path[k], 0], cities[best_path[(k+1)%shape], 0]],
                        [cities[best_path[k], 1], cities[best_path[(k+1)%shape], 1]],)

        plt.show()
    if estimated_time:
        chrono = estimate_time(shape)
        print(f"Time estimated to get exact solution : {chrono:.3e}s")

    return algo_gen.best_indv.chromosome, algo_gen.best_indv.fitness_score


if __name__ == "__main__":
    pass
