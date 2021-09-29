"""
Fichier contenant la définition d'un individu représentant un vecteur.
"""

import numpy as np # Importation de numpy pour les chromosomes de l'individu

class Individual_vector():
    def __init__(self, shape, fitness_function, starting_interval):
        """
        Fonction appelée à la création d'une instance de la classe.

        On y définit les différents attributs de cette instance et on les initialise.        
        Les chromosomes de l'individu doivent être définis en tant qu'un array numpy.

        --------
        Paramètres:

        self : instance de la classe Individual_vector.
        shape : entier, taille des chromosomes des individus, taille du vecteur.
        fitness_function : fonction, fonction que l'on cherche à maximiser, permet de calculer le score (fitness_score).
        starting_interval : float.


        --------
        Return:

        None : Ne renvoie rien.

        """

        self.shape =
        self.starting_interval =

        # Génération d'un individu aléatoire
        self.chromosomes =
        
        self.fitness_function =
        self.fitness_score =


    def mutate(self, individual):
        """
        Fonction de mutation d'un individu de type vecteur.

        --------
        Paramètres:

        self : instance de la classe Individual_vector.
        individual : seconde instance de la classe Individual_vector, permet de calculer une distance caractéristique
        inter-individu. (Non obligatoire)


        --------
        Return:

        None : Ne renvoie rien, l'individu est muté sur place.

        """

    def crossover(self, individual):
        """
        Fonction de crossover d'un individu de type vecteur.
        
        --------
        Paramètres:

        self : instance de la classe Individual_vector.
        individual : seconde instance de la classe Individual_vector.

        self et individual sont les deux parents pour le crossover.

        --------
        Return:

        tuple : Un couple de nouveau individu résultant de la descendance de "self" et "individual".
        """


if __name__ == "__main__":

    shape_test = 20
    fitness_function = lambda x: x[0]
    starting_interval = 15

    try:
        pop_test = [Individual_vector(shape_test, fitness_function, starting_interval), Individual_vector(shape_test, fitness_function, starting_interval)]

    except:
        print("Erreur dans l'initialisation de Individual_vector.")

    if pop_test[0].chromosomes.shape[0] != shape_test or pop_test[1].chromosomes.shape[0] != shape_test:
        print("Les chromosomes ne sont pas de la bonne taille")

    if np.all(pop_test[0].chromosomes == pop_test[1].chromosomes):
        print("Les chromosomes ne sont pas générer de manière aléatoire.")

    if pop_test[0].fitness_function != fitness_function:
        print("La fitness_function n'est pas initialisé correctement.")

    if np.any(np.fromiter((x > starting_interval or x < -starting_interval for x in pop_test[0].chromosomes), dtype=bool)) or np.any(np.fromiter((x > starting_interval or x < -starting_interval for x in pop_test[1].chromosomes), dtype=bool)):
        print("Les composantes du vecteur ne sont pas initialisés dans [-starting_interval; starting_interval].")

    if fitness_function(pop_test[0].chromosomes) != pop_test[0].fitness_score or fitness_function(pop_test[1].chromosomes) != pop_test[1].fitness_score:
        print("Le calcul du fitness score est faux.")

    chromo_save = np.copy(pop_test[0].chromosomes)
    pop_test[0].mutate(pop_test[1])

    if pop_test[0].chromosomes.shape[0] != shape_test:
        print("La fonction de mutation ne conserve pas la taille du vecteur.")

    if np.all(pop_test[0].chromosomes == pop_test[1].chromosomes) or np.all(chromo_save == pop_test[0].chromosomes):
        print("Les chromosomes ne sont pas mutés et reste identique.")

    if fitness_function(pop_test[0].chromosomes) != pop_test[0].fitness_score or fitness_function(pop_test[1].chromosomes) != pop_test[1].fitness_score:
        print("Le fitness_score n'est pas mis à jour après la mutation.")
    
    child1, child2 = pop_test[0].crossover(pop_test[1])

    if type(child1) != Individual_vector or type(child2) != Individual_vector:
        print("A l'issue des crossovers les enfants ne sont pas des instances de la classe Individual_vector.")

    if child1.chromosomes.shape[0] != shape_test or child2.chromosomes.shape[0] != shape_test:
        print("Les chromosomes ne sont pas de la bonne taille")

    if fitness_function(child1.chromosomes) != child1.fitness_score or fitness_function(child1.chromosomes) != child1.fitness_score:
        print("Le fitness_score n'est pas mis à jour après le crossover.")

    print("Test finished !")