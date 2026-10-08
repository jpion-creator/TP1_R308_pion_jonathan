
from random import randint

def choisir_mot(liste):
    """ Fonction permettant de choisir un mot aléatoirement parmis une liste de mot en majuscule"""
    assert type(liste) == list
    assert len(liste) != 0 
    #On renvoie le mot sous forme de liste et on retire 1 à la longueur de la liste car les listes comptes à partir de 0 
    return liste[randint(0,len(liste)-1)] 

def masque(mot):
    "Fonction permettant de créer un masque de la taille du mot donné, ne fonctionne pas si le mot est un caractère vide "" "
    # On vérifie le type 
    assert type(mot) == str
    # On vérifie que le mot n'est pas vide
    assert mot != ""
    masque = []
    for lettre in mot :
        masque += '_'
    return masque

