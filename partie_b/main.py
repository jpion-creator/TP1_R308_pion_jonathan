from function import initialiser_nombre
from function import devine_nombre

borne_sup = 10
borne_inf = 1
initialiser_nombre(borne_sup ,borne_inf )

# on vérifie que le résultat est bien aléatoire et qu'il détecte quand on entre le bon nombre 
for i in range(borne_inf,borne_sup):
    if devine_nombre(i) == "Bon nombre ! ":

        print("le nombre était")
        print(i)
        break
# On vérifie que la fonction renvoie bien Trop petit ou trop grand quand cela est necessaire
print(devine_nombre(0))
print(devine_nombre(11))