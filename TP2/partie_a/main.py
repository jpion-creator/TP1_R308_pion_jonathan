
from classes import Grille

grille = Grille()

grille.afficher()

grille.jouer(1,1,"X")
grille.jouer(2,0,"O")
grille.jouer(0,0,"X")
grille.jouer(0,1,"O")
print(grille.est_pleind())
grille.jouer(1,2,"X")
grille.jouer(1,0,"O")
grille.jouer(2,2,"X")
grille.jouer(2,1,"O")
grille.jouer(0,2,"X")
grille.afficher()
print(grille.est_pleind())
print(grille.est_gagnant("X"))
print(grille.est_gagnant("O"))
