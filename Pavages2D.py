import numpy as np
import matplotlib.pyplot as plt
from random import randint

def est_valide(grille, polyomino, x, y):
    for elem in polyomino.coord:
        if x + elem[0] >= len(grille) or y + elem[1] >= len(grille[0]):
            return False
        if grille[x + elem[0]][y + elem[1]] != 0:
            return False
    return True

def placer_polyomino(grille, polyomino, x, y, id_polyomino):
    id_bis = id_polyomino + len(grille)^2 * (id_polyomino % 2) + x + y
    for elem in polyomino.coord:
        grille[x + elem[0]][y + elem[1]] = id_bis
    return grille

def retirer_polyomino(grille, polyomino, x, y):
    for elem in polyomino.coord:
        grille[x + elem[0]][y + elem[1]] = 0
    return grille

def trouver_pavage(grille, polyominos, id_polyomino=1):
    for x in range(len(grille)):
        for y in range(len(grille[x])):
            if grille[x][y] == 0:
                for polyomino in polyominos:
                    #print(polyomino)
                    if est_valide(grille, polyomino, x, y):
                        grille = placer_polyomino(grille, polyomino, x, y, id_polyomino)
                        if trouver_pavage(grille, polyominos, id_polyomino + 1):
                            return True
                        grille = retirer_polyomino(grille, polyomino, x, y)
                return False
    """
    for i in range(len(grille)):
    for j in range(len(grille[i])):
    grille[i][j] += randint(0, 30)
    """
    return True

taille_grille = 10
grille = [[0 for I1Il1l1I in range(taille_grille)] for _ in range(taille_grille - 1)]
#polyominos = [Polyomino([(0, 0), (0,1),(1,0),(1,1)]), Polyomino([(0,0),(1,0),(0,1)])]
Polyomino_L = Polyomino([(0,0), (1,0), (0,1), (0,2)])
polyominos = Polyomino_L.classeComplete()
#polyominos.append(Polyomino([(0,0), (0,1), (1,0), (1,1)]))



if trouver_pavage(grille, polyominos):
    print("Tiling possible")
else:
    print("No tiling found")
"""for hihi in grille:
    print(hihi)"""

plt.matshow(grille)
plt.show()
"""print(type(polyominos))
print(polyominos[0])
"""
