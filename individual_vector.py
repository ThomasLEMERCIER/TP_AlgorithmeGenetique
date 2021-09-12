"""
Fichier contenant la définition d'un individu représentant un vecteur.
"""

class Individual_vector():
    def __init__(self, shape, fitness_function, starting_interval):
        """
        Fonction d'initialisation d'un individu de type vecteur
        Les chromosomes de l'individu doivent être définis en tant qu'une liste ou un array numpy.
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

        Return : None : L'individu est muté sur place.
        """

    def crossover(self, individual):
        """
        Fonction de crossover d'un individu de type vecteur.

        Return : children : Tuple de deux nouveaux individus résultant de la descendance de "self" et "individual".
        """
