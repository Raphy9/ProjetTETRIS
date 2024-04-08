

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
    
def fromCoordToTab(hauteur,largeur,coordonnees):
     return [[1 if (i,j) in coordonnees else 0 for j in range(largeur)] for i in range(hauteur)]
 
def copie(tab):
    res =[0 for i in range(len(tab))]
    for i in range(len(tab)):
        res[i] = tab[i]
    return res

     
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
        res = Polyomino(self.hauteur, self.largeur, self.taille)
        res.tableau = [[self.tableau[i][j] for j in range(self.l)] for i in range(self.h)]
        return res
        
    def __str__(self):
        res = ""
        tab = fromCoordToTab(self.hauteur+1, self.largeur+1, self.coord)
        for elem in tab:
            res+="\n"
            for val in elem:
                res += str(val) + " "
        return res
        
    def rotate(self):
        """Modifie le polyomino en le pivotant de 90 degrés."""
        tab = fromCoordToTab(self.hauteur+1,self.largeur+1,self.coord)
        tab_rotate =  np.rot90(np.array(tab))
        self.coord = fromTabToCoord(tab_rotate)
        self.hauteur, self.largeur = self.largeur, self.hauteur
        return None
    
    
    def symetrie(self,axis=0):
        """Renvoie la symétrie de la matrice. axis = 0 : axe horizontal, axis=1 : axe vertical"""
        tab = fromCoordToTab(self.hauteur+1,self.largeur+1,self.coord)
        if axis == 0:
            for i in range(len(tab)):
                for j in range(len(tab[i])//2):
                    tab[i][j], tab[i][len(tab[i])-j-1] = tab[i][len(tab[i])-j-1],tab[i][j]
        if axis == 1:
            for i in range(len(tab)//2):
                tab[i],tab[len(tab)-i-1] = tab[len(tab)-i-1] , tab[i]
        self.coord = fromTabToCoord(tab)
        return None
        
    
        

MatL = [[1,0,0,0,0],
        [1,0,0,0,0],
        [1,1,0,0,0]]
        
        
MatC = [[1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]]
        
MatI = [[1,0,0,0],
        [1,0,0,0],
        [1,0,0,0],
        [1,0,0,0]]

test = [[0,0, 1],[1,1,1]]
"""
for elem in test:
    print(elem)"""
coordL = fromTabToCoord(MatL)
tab = fromCoordToTab(3, 2, coordL)



a = Polyomino(coordL)
print(a)
a.symetrie(0)

print(a)

    

        
        
