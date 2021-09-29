"""
Fichier contenant la définition d'un individu représentant un chemin.
"""

class Individual_path():
    def __init__(self, shape, fitness_function, starting_interval=None):
        """
        Fonction appelée à la création d'une instance de la classe.

        On y définit les différents attributs de cette instance et on les initialise.
        Les chromosomes de l'individu doivent être définis en tant qu'une liste ou un array numpy
        représentant une permutation.

        Exemple : Pour 10 villes on peut avoir [0,1,2,3,4,5,6,7,8,9] ou [1,0,2,3,4,5,6,7,8,9], etc...

        --------
        Paramètres:

        self : instance de la classe Individual_path.
        shape : entier, taille des chromosomes des individus, permutation dans [0; shape[.
        fitness_function : fonction, fonction que l'on cherche à maximiser, permet de calculer le score (fitness_score).
        starting_interval : None, inutile ici, défini par soucis de compatibilité.


        --------
        Return:

        None : Ne renvoie rien.

        """

        self.shape = 

        # Génération d'un individu aléatoire
        self.chromosomes = 


        self.fitness_function = 
        self.fitness_score = 


    def mutate(self, *args):
        """
        Fonction de mutation d'un individu de type chemin.

        --------
        Paramètres:

        self : instance de la classe Individual_path.
        *args : None, défini par soucis de compatibilité.


        --------
        Return:

        None : Ne renvoie rien, l'individu est muté sur place.

        """


    def crossover(self, individual):
        """
        Fonction de crossover d'un individu de type chemin.

        --------
        Paramètres:

        self : instance de la classe Individual_path.
        individual : seconde instance de la classe Individual_path.

        self et individual sont les deux parents pour le crossover.

        --------
        Return:

        tuple : Un couple de nouveau individu résultant de la descendance de "self" et "individual".
        """

