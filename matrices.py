
import matplotlib.pyplot as plt
import numpy as np

"""Fonctions globales"""

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

        
        
    
MatA = [[1,3,3,3,5,5],
        [1,1,3,5,5,7],
        [1,2,8,8,7,7],
        [2,2,4,8,8,7],
        [2,4,4,4,10,10],
        [9,9,9,9,10,10]]    

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
   
#plt.matshow(MatA)
#plt.show()
        
a = Polyomino(fromTabToCoord(MatL))
c = Polyomino(fromTabToCoord(MatI))
b = a.classeComplete()
print()



for elem in b:
    #print(elem.coord)
    print(elem)
    print("----------------")
#print(c in b)


        
        
