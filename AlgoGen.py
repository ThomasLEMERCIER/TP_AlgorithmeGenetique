"""
Fichier définissant la classe représentant un algorithme génétique.
"""

class AlgoGen:
    def __init__(self, Indiv, pop_size, fitness_function, shape, mutation_rate, crossover_rate, starting_interval=None):
        """
        Fonction appelée à la création d'un instance de la classe.

        On y définit les différents attributs de cette instance et on les initialise.        
        """
        self.pop_size = 

        self.mutation_rate = 
        self.crossover_rate = 

        # Generate initial population
        self.population = 

        self.best_indv = 


    def parents_selection(self):
        """
        Renvoie deux individus de la population pour qu'ils effectuent un crossover.



        Return : parents : Tuple de deux individus de la population.
        """


    def survivor_selection(self):
        """
        Sélection des survivants.


        Return : None : Supprime sur place les individus que l'on ne garde pas pour la prochaine génération.
        """

    def step(self):
        """
        Fonction simulant un pas de l'algorithme pour passer à la génération suivante.
        """

        # Crossover
        

        # Mutation
        

        # Selection des survivants

