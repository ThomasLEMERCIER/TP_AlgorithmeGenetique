"""
Fichier définissant la classe représentant un algorithme génétique.
On cherchera toujours à maximiser la fonction et non minimiser.
"""

class AlgoGen:
    def __init__(self, Indiv, pop_size, fitness_function, shape, mutation_rate, crossover_rate, starting_interval=None):
        """
        --------
        Fonction appelée à la création d'une instance de la classe.

        On y définit les différents attributs de cette instance et on les initialise.        

        --------
        Paramètres:

        self : instance de la classe AlgoGen.
        Indiv : classe des individus (Individual_vector ou Individual_path) fonctionne comme une fonction ie : Indiv(shape, fitness_function, starting_interval) 
        -> renvoie un individu créer selon votre fonction __init__ de la classe en question.
        pop_size : entier, nombre d'individu constituant la population.
        fitness_function : fonction, fonction que l'on cherche à maximiser.
        shape : entier, taille des chromosomes des individus (taille du vecteur ou ensemble de la permutation [0; shape[).
        mutation_rate : float, [0;1] module la proportion de la population qui va être muté.
        crossover_rate : float, [0;1] module la proportion de la population qui se reproduit.
        starting_interval : float.


        --------
        Return:

        None : Ne renvoie rien.

        """

        self.pop_size = 

        self.mutation_rate = 
        self.crossover_rate = 

        # Generate initial population
        self.population = 

        self.best_indv = 


    def parents_selection(self):
        """
        Fonction appelé avec chaque crossover elle renvoie les deux parents qui effecturont le crossover.

         --------
        Paramètres:

        self : instance de la classe AlgoGen, elle possède donc tous les attributs définis dans la fonction __init__().


        --------
        Return:

        Tuple : Un couple d'individus correspondant aux parents que l'on va faire reproduire
        (Syntaxe pour renvoyer un tuple : return parent1, parent2).

        """



    def survivor_selection(self):
        """
        Fonction appelé à la fin de chaque génération. Elle permet de garder la taille de la population constante
        à chaque début d'époque (step / génération).

        --------
        Paramètres:

        self : instance de la classe AlgoGen, elle possède donc tous les attributs définis dans la fonction __init__().


        --------
        Return:

        None : Ne renvoie rien, modifie la population sur place.

        """



    def step(self):
        """
        Fonction simulant un pas de l'algorithme pour passer à la génération suivante.

        --------
        Paramètres:

        self : instance de la classe AlgoGen, elle possède donc tous les attributs définis dans la fonction __init__().


        --------
        Return:

        None : Ne renvoie rien.

        """

        # Crossover
        

        # Mutation
        

        # Selection des survivants

