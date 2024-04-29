import numpy as np
import matplotlib.pyplot as plt
from random import randint
"""
2. Modélisation et explorations 

(1) : 1 seule dimension, On se place d’abord dans un espace à paver d’une seule dimension
(un rectangle de longueur n et de hauteur 1). Proposez un algorithme permettant de
tester si la ligne peut être pavée par un ensemble de polyominos donnés. Si oui, il
faudra donner la solution.

Vérifier que l'ensemble des polyominos considéré ne possède que des éléments de la forme suivante :
 dimensions (1,k) avec 1 <= k <= n.
Si oui,
"""

def Pavage_1D(n=4, t=[1, 2, 3]):
 """
paramètres : 
- n un entier représentant la longueur du rectangle à paver 
- t un tableau d'entiers representant l'ensemble des longueurs des polyominos rectangulaires de la forme (1,k)
return : le nombre de manières de paver le rectangle considéré
 """

 """
 liste_ut = np.array([t[i] for i in range(len(t)) if t[i] <= n ])
 if(len(liste_ut) == 0):
     return "Pas de pavage"
 else:
     liste_res = []
     for poly_long in liste_ut:
         while()
 """
 """
 for i in range(len(liste_ut)):
 for j in range(liste_ut[i]):
 grille[j] = i
 """
        
 
Pavage_1D()

def fromTabToCoord(tableau):
    res = []
    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            if tableau[i][j]==1:
                res.append((i,j))
    return res
    
def fromCoordToTab(hauteur,largeur,coordonnees):
     return [[1 if (i,j) in coordonnees else 0 for j in range(largeur)] for i in range(hauteur)]

"""Classe polyomino"""
     
class Polyomino:
    def __init__(self,c=[]):
        maxH = 0
        maxL = 0
        for i in range(len(c)):
            if(c[i][0]>maxH):
                maxH = c[i][0]
            if(c[i][1]>maxL):
                maxL = c[i][1]
        self.hauteur = maxH
        self.largeur = maxL
        self.taille = len(c)
        self.coord = c
            
            
        
    def copie(self):
        return Polyomino(self.coord)  
        

    def __str__(self):
        res = ""
        tab = fromCoordToTab(self.hauteur+1, self.largeur+1, self.coord)
        for elem in tab:
            res+="\n"
            for val in elem:
                res += str(val) + " "
        return res
    
    def dans(self,tab):
        for elem in tab:
            if set(elem.coord) == set(self.coord):
                return True
        return False

    
    #Q2
    def rotate(self):
        """Renvoie une copie du polyomino en le pivotant de 90 degrés."""
        tab = fromCoordToTab(self.hauteur+1,self.largeur+1,self.coord)
        tab_rotate =  np.rot90(np.array(tab))
        return Polyomino(fromTabToCoord(tab_rotate))
    
    def symetrie(self,axis=0):
        """Renvoie une copie de la symétrie de la matrice. axis = 0 : axe horizontal, axis=1 : axe vertical"""
        tab = fromCoordToTab(self.hauteur+1,self.largeur+1,self.coord)
        if axis == 1:
            for i in range(len(tab)):
                for j in range(len(tab[i])//2):
                    tab[i][j], tab[i][len(tab[i])-j-1] = tab[i][len(tab[i])-j-1],tab[i][j]
        if axis == 0:
            for i in range(len(tab)//2):
                tab[i],tab[len(tab)-i-1] = tab[len(tab)-i-1] , tab[i]
        return Polyomino(fromTabToCoord(tab))
        
    #Q3
    
    def classeComplete(self):
        """Generate all unique rotations and reflections of the polyomino."""
        res = [self]       
        p2 = self.copie()
       
        for i in range(3):
            p2 = p2.rotate()
            if not p2.dans(res):
                res.append(p2)
               
        p3 = self.copie()
        p3 = p3.symetrie(0) 

        if not p3.dans(res):
            res.append(p3)
      
        for i in range(3):
            p3 = p3.rotate()
            if not p3.dans(res):
                res.append(p3)

        #for poly in res:
         #   print(poly.coord)

        return res
        
 
"""
#coinSizes = [1, 2, 5, 10, 20, 50]
ways = [0] * (n + 1)
ways[0] = 1
for l in t:
    for i in range(l, n+1):
        ways[i] += ways[i-l]
    print(ways)
print(f"Il y a {ways[-1]} façons de paver {n} avec des polyominos de longueur {t}")
"""

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
