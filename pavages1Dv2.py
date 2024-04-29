def Pavage_1D(n, tiles):
    """
    1. Fonction Pavage_1D

    La fonction Pavage_1D est une fonction récursive qui trouve toutes les
    combinaisons possibles de pavages pour une longueur donnée n et une liste de
     tailles de tuiles disponibles tiles.
     
    2. Cas de base

    Le cas de base de la récursion est lorsque la longueur à pavée n est égale à 
    zéro. Dans ce cas, il n'y a pas besoin de placer de tuiles, donc la fonction 
    renvoie simplement une liste contenant une liste vide [], ce qui signifie qu'une 
    solution a été trouvée.

    if n == 0:
        return [[]]  # Retourne une liste contenant une liste vide (solution trouvée)

    3. Génération des solutions récursivement

    Pour chaque taille de tuile dans la liste tiles, la fonction vérifie si cette taille
    de tuile peut être utilisée pour le pavage, c'est-à-dire si elle est inférieure ou 
    égale à la longueur restante n.

    for tile in tiles:
        if tile <= n:
            # Récursion : trouve toutes les solutions possibles pour le reste de la longueur
            sub_solutions = Pavage_1D(n - tile, tiles)
            # Pour chaque sous-solution, ajoute la tuile actuelle
            for sub_solution in sub_solutions:
                solutions.append([tile] + sub_solution)

    Si la taille de la tuile peut être utilisée, la fonction appelle récursivement Pavage_1D 
    pour trouver toutes les solutions possibles pour la longueur restante après avoir placé 
    cette tuile. Elle stocke ensuite cette sous-solution dans sub_solutions.

    Pour chaque sous-solution, la fonction ajoute la taille de la tuile actuelle à la liste 
    et ajoute cette nouvelle solution à la liste des solutions solutions.

    4. Retour des solutions

    Une fois que toutes les combinaisons possibles de pavages ont été trouvées pour la longueur
    n, la fonction retourne la liste des solutions.

    EXEMPLE :

    Étape 1: Appel initial

    solutions = Pavage_1D(4, [1, 2])

    La fonction est appelée avec une longueur à pavée de 4 et des tuiles de tailles [1, 2].

    Étape 2: Récursion

    Iteration 1: Tile = 1

        tile = 1 est inférieur ou égal à la longueur à pavée 4, donc on explore cette possibilité.
        On appelle récursivement Pavage_1D(4 - 1, [1, 2]) pour trouver toutes les combinaisons 
        possibles de pavages pour la longueur restante (3) avec les mêmes tuiles disponibles.

    Iteration 2: Tile = 2

        tile = 2 est inférieur ou égal à la longueur à pavée 4, donc on explore cette possibilité.
        On appelle récursivement Pavage_1D(4 - 2, [1, 2]) pour trouver toutes les combinaisons 
        possibles de pavages pour la longueur restante (2) avec les mêmes tuiles disponibles.

    Étape 3: Retour des sous-solutions

    Pour Pavage_1D(3, [1, 2]):

        Les combinaisons possibles sont [1, 1, 1] et [1, 2].

    Pour Pavage_1D(2, [1, 2]):

        Les combinaisons possibles sont [1, 1] et [2].

    Étape 4: Construction des solutions

    Pour chaque sous-solution, on ajoute la taille de la tuile actuelle et on combine cela avec 
    les sous-solutions trouvées précédemment.

        Pour [1, 1, 1], on ajoute tile à chaque solution pour obtenir [1, 1, 1, 1] et [1, 1, 2].
        Pour [1, 2], on ajoute tile à chaque solution pour obtenir [1, 2, 1] et [1, 2, 2].

    """
    if n == 0:
        return [[]]  # Retourne une liste contenant une liste vide (solution trouvée)
    
    solutions = []  # Initialise une liste pour stocker les solutions
    
    for tile in tiles:
        if tile <= n:
            # Récursion : trouve toutes les solutions possibles pour le reste de la longueur
            sub_solutions = Pavage_1D(n - tile, tiles)
            # Pour chaque sous-solution, ajoute la tuile actuelle
            for sub_solution in sub_solutions:
                solutions.append([tile] + sub_solution)
    
    return solutions

# Exemple d'utilisation
solutions = Pavage_1D(4, [1, 2])

if solutions:
    print("Solutions valides:")
    for sol in solutions:
        print(sol)
else:
    print("Aucune solution trouvée.")
