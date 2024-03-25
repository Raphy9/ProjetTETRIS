#Regle : On représente un polyomino de taille n dans une matrice n*n.

MatL = [[1,0,0,0,0],
        [1,0,0,0,0],
        [1,1,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]]
        
        
MatC = [[1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]]
        
MatI = [[1,0,0,0],
        [1,0,0,0],
        [1,0,0,0],
        [1,0,0,0]]
        
def copie(tab):
    res =[0 for i in range(len(tab))]
    for i in range(len(tab)):
        res[i] = tab[i]
    return res

def rotaMatrice(Mat):
    """Prend une matrice et la pivote de 90° vers la droite"""
    res = [ [0 for i in range(len(Mat))] for j in range(len(Mat))]
    for i in range(len(Mat)):
        for j in range(len(Mat)):
            res[j][len(Mat) - i -1] = Mat[i][j]
    return recentre(res)

def symetrieHorizontale(Mat):
    res = copie(Mat)
    for i in range(len(res)//2):
        res[i],res[len(res)-i-1] = res[len(res)-i-1] , res[i]
    return recentre(res)
        
def symetrieVerticale(Mat):
    res = copie(Mat)
    for i in range(len(res)):
        for j in range(len(res[i])//2):
            res[i][j], res[i][len(res[i])-j-1] = res[i][len(res[i])-j-1],res[i][j]
    return recentre(res)
    
    
def decaleHaut(Mat, compt):
    res = copie(Mat)
    for i in range(compt, len(Mat)):
        res[i-compt] = res[i]
    for k in range(len(Mat) - compt, len(Mat)):
        res[k] = [0 for j in range (len(Mat[0]))]
    return res
    


def decaleGauche(Mat, compt):
    res = copie(Mat)
    for i in range(len(Mat)):
        for j in range(compt,len(Mat[i])):
            res[i][j-compt] = res[i][j]
        for j in range(len(Mat[i]) - compt, len(Mat[i])):
            res[i][j] = 0
    return res
    


def recentre(Mat):
    tmp = copie(Mat)
    centreHaut = False
    centreGauche = False
    comptGauche = 0
    comptHaut = 0
    ligne = 0
    colonne = 0
    while not centreHaut:
        if Mat[ligne][colonne]!=0:
            centreHaut = True
            
        elif colonne<len(Mat)-1 :
            colonne+=1
        else:
            colonne=0
            ligne+=1
            comptHaut+=1
    MatHaut = decaleHaut(tmp, comptHaut)
    ligne = 0
    colonne = 0
    while not centreGauche:
        if Mat[ligne][colonne] != 0:
            centreGauche = True
            
        elif ligne <len(Mat) - 1:
            ligne +=1
        else:
            ligne = 0
            colonne += 1
            comptGauche += 1
        
    MatGauche = decaleGauche(MatHaut, comptGauche)
        
    return MatGauche

        
"""
#Rotation

a = rotaMatrice(MatL)
b = rotaMatrice(a)
c = rotaMatrice(b)
d = rotaMatrice(c)


a_bis  = symetrieHorizontale(a)

for elem in MatL:
    print(elem)
print("-----a--------")
for elem in a :
    print(elem)
print("------a bis-------")
for elem in a_bis:
    print(elem)


print("-------b -------")
for elem in b :
    print(elem)
print("--------------")
for elem in c :
    print(elem)
print("--------------")
for elem in d :
    print(elem)
print("--------------")
"""

#Symetrie

a = symetrieHorizontale(MatL)

b = symetrieVerticale(MatL)


for elem in MatL:
    print(elem)


print("-----SYMETRIE HORIZONTALE------")
for elem in a:
    print(elem)

print("----SYMETRIE VERTICALE-------")
for elem in b:
    print(elem)

"""
test = [1,3,2,4,9]
for i in range(len(test)//2):
    test[i], test[len(test)-i-1] = test[len(test)-i-1],test[i]
print(test)
"""               
                



