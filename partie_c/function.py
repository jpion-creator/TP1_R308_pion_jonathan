
from random import randint

def choisir_mot(liste):
    """ Fonction permettant de choisir un mot aléatoirement parmis une liste de mot en majuscule"""
    assert type(liste) == list
    assert len(liste) != 0 

    return liste[randint(0,len(liste)-1)] 

def masque(mot):
    "Fonction permettant de créer un masque de la taille du mot donné, ne fonctionne pas si le mot est un caractère vide "" "
    assert type(mot) == str
    assert mot != ""
    masque = []
    for lettre in mot :
        masque.append(['_'])
    return masque

