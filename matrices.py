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
        print(self.coord)
        
        a = fromCoordToTab(self.hauteur+1, self.largeur+1, self.coord)
        
        for elem in a:
            print(a)
        
        return ""
        
    def rotation(self):
        tab = fromCoordToTab(self.hauteur,self.largeur,self.tab)
        return np.rot90(np.array(tab))
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

coordL = fromTabToCoord(MatL)
"""
tab = fromCoordToTab(3,2,coordL)
for elem in tab :
    print(elem)

test = fromCoordToTab(3,2,coordL)
for elem  in test:
    print (elem)
"""
a = Polyomino(coordL)
#print(a.coord, a.hauteur, a.largeur)
print(a)

    

        
        
