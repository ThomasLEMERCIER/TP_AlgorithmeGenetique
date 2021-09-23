# TP : Algorithme génétique

## Fonctions vectorielles (level 1 à level 6)

### Compléter la définition de la classe d'un individu vectoriel

L'ensemble des fonctions à completer se trouve dans le fichier individual_vector.py.

#### Méthode d'initialisation
1. Définir les attributs nécessaires
    <details>
    <summary>Spoiler warning</summary>
    
    * Dimension du vecteur (_shape_)
    * Intervalle de recherche (_starting_interval_), l'implémentation est libre mais si vous ne savez pas comment faire un simple réel fera l'affaire.
    On prendra par exemple, ensuite chaque composante du vecteur de chromosomes dans [-_starting_interval_, _starting_interval_].
    * Score de l'individu (_fitness_score_)
    * Fonction de score (_fitness_function_)
    * Chromosomes de l'individu (_chromosomes_)
    
    </details>

2. Création des chromosomes associés à l'individu
   <details>
    <summary>Spoiler warning</summary>
    
    * Création d'un array numpy de taille shape contenant des réels aléatoires compris dans l'intervalle _starting_interval_
    
    </details>
3. Initialialisation du score de l'individu

#### Méthode de crossover

1. Pour commencer une moyenne pondérée entre _self_ et _individual_ sur chaque composantes devrait suffire
    <details>
    <summary>Spoiler warning</summary>
    
    * Ne pas oublier de calculer le score des enfants
    
    </details>

#### Méthode de mutation


1. Libre à vous de choisir quelle fonction de bruit utiliser
    <details>
    <summary>Spoiler warning</summary>
    
    * Une gaussienne donne des résultats satisfaisants
    * Ne pas oublier de mettre à jour le score de l'individu
    
    </details>


### Completer la définition de la classe de l'algorithme génétique

L'ensemble des fonctions à completer se trouve dans le fichier AlgoGen.py.

#### Méthode d'initialisation :
1. Définir les attributs nécessaires
    <details>
    <summary>Spoiler warning</summary>
    
    * Population (population)
    * Taille de la population (pop_size)
    * Fréquence de mutation (mutation_rate)
    * Fréquence de crossover (crossover_rate)
    * Meilleur individu (best_indv)
    
    </details>
2. Génération de la population initiale
   <details>
    <summary>Spoiler warning</summary>
    
    * On créé une liste contenant les individus voulus grâce à l'argument _Indiv_ de la fonction _init_
    qui correspond à la classe _individual\_vector_ ou _individual\_path_ en fonction des besoins.

    Exemple : 

        Indiv(shape=shape, fitness_function=fitness_function, starting_interval=starting_interval)
    
    </details>


#### Méthode _parents_selection_  : Sélection des parents
1. Dans un premier temps la méthode du tournoi suffira
    <details>
    <summary>Spoiler warning</summary>

        * Pour trier un sous-ensemble de la population en fonction
        du score de l'individu on pourra utiliser :

        
            topk = sorted(sous_ensemble, key=lambda x: x.score)[-k:]
        
    </details>

#### Méthode _survivor_selection_ : Sélection des survivants

1. Utiliser la sélection par le score
    <details>
    <summary>Spoiler warning</summary>

    * Pour trier un sous-ensemble de la population en fonction
    du score de l'individu on pourra utiliser :

            topk = sorted(sous_ensemble, key=lambda x: x.score)[-k:]
        
    </details>

#### Méthode _step_ : Une itération de l'algorithme
1. Effectuer les crossovers pour peupler la population
2. Muter  population
3. Définir la nouvelle population grâce à la méthode de sélection des survivants


## Approximation du problème du voyageur de commerce

[Description du problème](https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_voyageur_de_commerce)

Pour représenter un chemin possible en passant par les n villes du problème on numérote les villes de 0 à n-1. Puis on prend une permutation de [0;n-1].

Exemple:
Pour n = 5,

[1,2,3,4,0] -> Le voyageur commence à la ville 1 puis 2 etc... jusqu'à revenir en 1 après la ville 0.

L'ensemble des fonctions à completer se trouve dans le fichier individual_path.py.

### Completer la définition de la classe d'un individu chemin

#### Méthode d'initialisation
1. Définir les attributs nécessaires
    <details>
    <summary>Spoiler warning</summary>
    
    * Nombre de villes (shape)
    * Score de l'individu (fitness_score)
    * Fonction de fitness (fitness_function)
    * Chromosomes de l'individu (chromosomes)

    </details>

2. Création du chromosome associé à l'individu

3. Initialialisation du score de l'individu

#### Méthode de crossover

1. En première intention on peut prendre deux nouveux individus aléatoires

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
