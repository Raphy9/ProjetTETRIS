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

def Pavage_1D(liste_res, liste_temp, n=4, t=[1, 2, 3]):
     """
    paramètres : 
    - n un entier représentant la longueur du rectangle à paver 
    - t un tableau d'entiers representant l'ensemble des longueurs des polyominos rectangulaires de la forme (1,k)
    return : le nombre de manières de paver le rectangle considéré
     """
     if(t == None):
         return None
     liste_ut = np.array([t[i] for i in range(len(t)) if t[i] <= n ])
     for poly_long in liste_ut:
         a = n // poly_long
         b = n % poly_long
         liste_temp = [poly_long for i in range(a)]
         print(liste_temp)
         #temp = t.copy()
         #print(temp)
         if(b == 0):                 
             liste_res.append(liste_temp)
             liste_temp.pop()
             Pavage_1D(liste_res, liste_temp, (n-(a-1)*poly_long), t.pop(poly_long))#temp.pop(poly_long))
         else :
             Pavage_1D(liste_res, liste_temp, n-(a*poly_long), t.pop(poly_long)) #temp.pop(poly_long)
     return liste_res
     """
     for i in range(len(liste_ut)):
         for j in range(liste_ut[i]):
             grille[j] = i
     """
        
l = []
lt = []
Pavage_1D(l, lt, 10, [2,3,5])

t = [1,2,3]
print(t.pop(2))
print(t)
 

 
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
