# TP : Algorithme génétique

## Fonctions vectorielles (level 1 à level 6)

### Compléter la définition de la classe d'un individu vectoriel

#### Méthode d'initialisation
1. Définir les attributs nécessaires
    <details>
    <summary>Spoiler warning</summary>
    
    * Dimension du vecteur (shape)
    * Interval de recherche (starting_interval)
    * Score de l'individu
    * Fonction de score (fitness_function)
    * Chromosome de l'individu
    
    </details>

2. Création du chromosome associé à l'individu
3. Initialialisation du score de l'individu

#### Méthode de crossover

1. Pour commencer la moyenne pour chaque composantes devrait suffire
    <details>
    <summary>Spoiler warning</summary>
    
    * Ne pas oublier de calculer le score des enfants
    
    </details>

#### Méthode de mutation

1. Libre à vous de choisir quelle fonction de bruit utiliser
    <details>
    <summary>Spoiler warning</summary>
    
    * Une gaussienne donne des résultats satisfaisants
    * Ne pas oublier de calculer le score des enfants
    
    </details>


### Completer la définition de la classe de l'algorithme génétique

#### Méthode d'initialisation :
1. Définir les attributs nécessaires
    <details>
    <summary>Spoiler warning</summary>
    
    * Population
    * Taille de la population (pop_size)
    * Fréquence de mutation (mutation_rate)
    * Fréquence de crossover (crossover_rate)
    * Meilleur individu
    
    </details>
2. Génération de la population initiale


#### Méthode de sélection des parents
1. Dans un premier temps la méthode du tournoi suffira
    <details>
    <summary>Spoiler warning</summary>

        * Pour trier un sous-ensemble de la population en fonction
        du score de l'individu on pourra utiliser :

        
            topk = sorted(sous_ensemble, key=lambda x: x.score)[-k:]
        
    </details>

#### Méthode de sélection des survivants

1. Utiliser la sélection par le score
    <details>
    <summary>Spoiler warning</summary>

    * Pour trier un sous-ensemble de la population en fonction
    du score de l'individu on pourra utiliser :

            topk = sorted(sous_ensemble, key=lambda x: x.score)[-k:]
        
    </details>

#### Méthode d'une itération de l'algorithme
1. Initialiser une futur population vide
2. Effectuer les crossovers pour peupler la futur population
3. Muter la futur population
4. Définir la nouvelle population grâce à la méthode de sélection des survivants


## Approximation du problème du voyageur de commerce

### Completer la définition de la classe d'un individu chemin

#### Méthode d'initialisation
1. Définir les attributs nécessaires
    <details>
    <summary>Spoiler warning</summary>
    
    * Nombre de ville (shape)
    * Score de l'individu
    * Fonction de fitness (fitness_function)
    * Chromosome de l'individu

    </details>

2. Création du chromosome associé à l'individu
3. Initialialisation du score de l'individu

#### Méthode de crossover

1. En première intention on peux prendre deux nouveux individus aléatoires

#### Méthode de mutation

1. En première intention on peux intervertir deux villes


## Fonctions vectorielles (level 7 à level 9)

### Amélioration la définition de la classe de l'algorithme génétique

#### Nouvelle méthode de sélection des parents

1. Roulette
    <details>
    <summary>Spoiler warning</summary>
        
    Si tu es arrivé là c'est que tu te débrouilles bien mais voilà une syntaxe qui pourra surêment te servir :
        parents = np.random.choice(self.population, size=2, p=proba)
    </details>
2. Stochastic Universal Sampling [Description de l'algorithme](https://en.wikipedia.org/wiki/Stochastic_universal_sampling)

#### Sauvegarde d'une population élite

Pour accélérer la recherche maintenant que l'on a des nouvelles méthodes de crossovers qui sont plus efficace pour faire converger les solutions on fait muter toute la population i.e. la futur population avec la population initiale.

Néanmoins on risque de modifier nos meilleurs éléments de la population initiale, on va donc créer une population élite qui sauvegardera nos meilleurs éléments pour la sélection des survivants.

1. Définition d'une méthode de copie dans la classe des individus
    <details>
    <summary>Spoiler warning</summary>
        
    Attention ne pas oublier que les listes et les arrays numpy sont référencés par rapport à leur adresse mémoire.
    </details>
    
2. Sauvegarde des meilleurs élements par copie avant les mutations
3. Mutation sur toute la population

## Amélioration du problème du voyageur de commerce

#### Nouvelle méthode de mutation

1. Méthode de 'Displacement' 

Description de l'algorithme :

![Displacement algorithm](./images/Displacement.PNG)

Displacement mutation is also called cut mutation (Banzhaf 1990).

#### Nouvelle méthode de crossover

1. Méthode 'OX1'

Description de l'algorithme :

![OX1 algorithm](./images/OX1.PNG)

[Publication originale pour les deux nouvelles méthodes](https://link.springer.com/content/pdf/10.1023/A:1006529012972.pdf)




