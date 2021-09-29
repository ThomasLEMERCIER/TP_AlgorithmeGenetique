import time
import random
from tqdm import tqdm

import matplotlib.pyplot as plt
import numpy as np

from AlgoGen import AlgoGen
from test_functions import *
from tsp import distance_path, estimate_time

def function_optimization(function, nEpochs, shape, pop_size, mutation_rate, crossover_rate, starting_interval, render=True):

    from individual_vector import Individual_vector

    fitness_function = lambda x : -function(x) * 1e-3

    algo_gen = AlgoGen(Individual_vector, pop_size, fitness_function, shape, mutation_rate, crossover_rate, starting_interval)

    max_fitness = []
    avg_fitness = []
    epochs = []

    top = time.time()

    for e in tqdm(range(nEpochs)):

        algo_gen.step()
        
        if render:
            if not(function == lvl4 or function == lvl5 or function == lvl6):
                function(algo_gen.best_indv.chromosomes, True, 1e-3)
                

        epochs.append(e+1)
        max_fitness.append(algo_gen.best_indv.fitness_score)
        avg_fitness.append(sum(indv.fitness_score for indv in algo_gen.population)/algo_gen.pop_size)

    stop = time.time()

    result = function(algo_gen.best_indv.chromosomes, False)

    plt.ioff()
    plt.close()

    print(f"\nTime elapsed : {stop-top:.3f}s")
    print(f"Chromosomes du meilleur individu : {algo_gen.best_indv.chromosomes}\nValeur de la fonction pour cette individu : {result}")

    plt.figure()
    plt.plot(epochs, max_fitness, label='Max fitness')
    plt.plot(epochs, avg_fitness, label='Average fitness')
    plt.title("Fitness over generation")
    plt.legend()
    function(algo_gen.best_indv.chromosomes, render, 5)


    return 

def tsp(nEpochs, shape, pop_size, mutation_rate, crossover_rate, method='random', estimated_time=True, render=True):

    from individual_path import Individual_path
    
    if method == 'random':
        cities = np.array([[random.random()*100, random.random()*100] for _ in range(shape)])
    elif method == 'square':
        if (root_nCities := int(shape ** (1/2))) ** 2 == shape:
            cities = np.array([[x, y] for x in range(root_nCities) for y in range(root_nCities)])
        else:
            raise ValueError(f"To use the square method the shape must be a perfect square : {shape}")
    else:
        NotImplementedError(f"The following method to create cities is not implemented : {method}")

    fitness_function = lambda x: 1/(1+distance_path(cities, x))

    algo_gen = AlgoGen(Individual_path, pop_size, fitness_function, shape, mutation_rate, crossover_rate)

    max_fitness = []
    avg_fitness = []
    epochs = []

    plt.figure()
    plt.ion()

    top = time.time()

    for e in tqdm(range(nEpochs)):

        algo_gen.step()

        epochs.append(e+1)
        max_fitness.append(algo_gen.best_indv.fitness_score)
        avg_fitness.append(sum(indv.fitness_score for indv in algo_gen.population)/algo_gen.pop_size)

        best_path = algo_gen.best_indv.chromosomes
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


    plt.figure()
    plt.plot(epochs, max_fitness, label='Max fitness')
    plt.plot(epochs, avg_fitness, label='Average fitness')
    plt.title("Fitness over generation")
    plt.legend()
    plt.show()
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

if __name__ == "__main__":
    """
    Pour lancer le fichier décommenter la ligne:
    - function_optimization pour optimiser sur les fonctions définies dans test_functions (Partie I du TP : lvl1 à lvl6)
    (se référer au fichier pour connaître les dimensions des variables d'entrée des fonctions).
    - tsp pour optimiser sur le problème du voyageur de commerce.
    
    """

    # function_optimization(function=lvl1, nEpochs=100, shape=1, pop_size=100, mutation_rate=0.2, crossover_rate=0.9, starting_interval=20)
    # tsp(nEpochs=100, shape=10, pop_size=100, mutation_rate=0.2, crossover_rate=0.9)