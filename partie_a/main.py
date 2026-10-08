# Partie A Du TP
from classes import Etudiant
from function import ajouter_etudiant
from function import moyenne_classe
from function import meilleur_etudiant


# Dans ce fichier, on realisera les test finaux et on utilisera les fonctions definies dans les autres fichier

dico_etudiant  = {}

ajouter_etudiant(dico_etudiant, "Alice", 12)
ajouter_etudiant(dico_etudiant, "Bob", 15)
ajouter_etudiant(dico_etudiant, "Claire", 9.5)


print(moyenne_classe(dico_etudiant))
print("\n")
print(meilleur_etudiant(dico_etudiant))