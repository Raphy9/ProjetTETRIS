import numpy as np
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
 liste_ut = np.array([t[i] for i in range(len(t)) if t[i] <= n ])
 if(len(liste_ut) == 0):
     return "Pas de pavage"
 else:
     liste_res = []
     for poly_long in liste_ut:
         while()
         
     """
     for i in range(len(liste_ut)):
         for j in range(liste_ut[i]):
             grille[j] = i
     """
        
 
Pavage_1D()
 
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
