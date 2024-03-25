import numpy as np
"""
class Matrice : 
    def __init__(self,h=0,l=0):
        self.hauteur = h
        self.largeur = l
        self.plateau = [[0 for i in range(l)] for i in range(h)]
        return None
        
    def addPolyomino(self,poly,x,y) -> None:
        assert(poly.hauteur-y>0 and h+y
"""   


def fromTabToCoord(tableau):
    res = []
    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            if tableau[i][j]==1:
                res.append((i,j))
    return res
    
def fromCoordToTab(coordonnees):
     return [[1 if (i,j) in coordonnees else 0 for j in range(len(self.tab[i]))] for i in range(len(self.tab))]     
class Polyomino:
    def __init__(self,h=0,l=0,t=0,c=[]):
        self.hauteur = h
        self.largeur = l
        self.taille = t
        self.tab = c
        
    def copie(self):
        res = Polyomino(self.hauteur, self.largeur, self.taille)
        res.tableau = [[self.tableau[i][j] for j in range(self.l)] for i in range(self.h)]
        return res
        
    def rotation(self):
        res = []
        for i in range(len(self.tab)):
            res.append([])
            for j in range(len(self.tab[i]):
                res[j][len(self.tab) - i -1] = self.tab[i][j]
        return self.tab = res


    

        
        
