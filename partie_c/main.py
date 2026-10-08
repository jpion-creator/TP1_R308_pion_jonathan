from function import masque
from function import choisir_mot

LISTE_MOT = ["POMME","PYTHON","ARBRE","RESEAU","TELECOMMUNICATION"]

# On vérifie que le mot choisi est aléatoire 
mot_alea = choisir_mot(LISTE_MOT)
print(mot_alea)

print(masque(mot_alea))
