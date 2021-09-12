"""
Fichier contenant la définition d'un individu représentant un chemin.
"""

class Individual_path():
    def __init__(self, shape:int, fitness_function, starting_interval=None):
        """
        Fonction d'initialisation d'un individu de type chemin
        Les chromosomes de l'individu doivent être définis en tant qu'une liste ou un array numpy
        représentant une permutation.

        Exemple : Pour 10 villes on peut avoir [0,1,2,3,4,5,6,7,8,9] ou [1,0,2,3,4,5,6,7,8,9], etc...

        """

        self.shape = 

        # Génération d'un individu aléatoire
        self.chromosomes = 


        self.fitness_function = 
        self.fitness_score = 


    def mutate(self, *args):
        """
        Fonction de mutation d'un individu de type chemin.

        Return : None : L'individu est muté sur place.
        """


    def crossover(self, individual):
        """
        Fonction de crossover d'un individu de type chemin.

        Return : children : Tuple de deux nouveaux individus résultant de la descendance de "self" et "individual".
        """

