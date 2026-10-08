# Dans cette partie b les fonctions et le corp principale seront contenu dans le même fichier 
from function import choisir_mot
from function import masque
# On réutilise la fonction pour choisir un mot aléatoirement de la partie C 
LISTE_MOT = ["POMME","PYTHON","ARBRE","RESEAU","TELECOMMUNICATION"]

nombre_essai = 7
nombre_erreur = 0 

lettre_devine = 0 
lettre_choisi = []
#Variable qui stocke le mot aléatoire à deviner 
mot_deviner = choisir_mot(LISTE_MOT)
# Variable qui stocke le masque du mot : On la modifie dans le passage de la boucle While
mot_masque = masque(mot_deviner)
print(mot_masque)

# La boucle s'arrete si le mot est entièrement découvert ou qu'il n'y a plus d'essais
while nombre_essai > 0: 
    print("Mot :", mot_masque)
    print("Erreurs :", nombre_erreur)
    print("Lettres proposées :", lettre_choisi)
    
    # On met la saisie en majuscule dès le départ
    lettre = input("Entrée une lettre à deviner : ").upper()

    # On vérifie que c'est un seul caractère ET une majuscule valide
    if len(lettre) != 1 or not lettre.isupper():
        print("ce n'est pas une lettre !")
        continue
        
    if lettre in lettre_choisi: 
        print("lettre déjà choisi pas d'erreur de plus")
        continue
    else:
        lettre_choisi.append(lettre)
        
    copie_lettre_devine = lettre_devine

    for i in range(len(mot_deviner)):
        if lettre == mot_deviner[i]: 
            mot_masque[i] = lettre
            lettre_devine += 1

    if copie_lettre_devine == lettre_devine: 
        nombre_erreur += 1 
        nombre_essai -= 1
    # Condition de victoire on regarde si le masque à été modifé entièrement
  
    # Comme mot_deviner stocke les mots en entier "POMME" ou "ARBRE" on utilise list pour séparer chaque lettre pour le résultat ['P','O','M','M','E']
    if mot_masque == list(mot_deviner) :
        print(list(mot_deviner))
        print('Gagné !')
        break 

#Le while se finit on a plus d'essais
if nombre_essai == 0:
    print("Perdu :(  )")