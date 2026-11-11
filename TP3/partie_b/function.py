from classes import Bibliotheque

def verifier_existence_livre(biblio, titre):
    """ Fonction permettant de vérifier si un livre donné est présent dans le dictionnaire de la bibliothèque """
    assert isinstance(biblio, Bibliotheque)
    assert isinstance(titre, str)
    if titre in biblio.livres:
        return True
    else:
        return False

def afficher_separateur():
    """ Fonction auxiliaire permettant d'afficher une ligne de séparation dans la console """
    print("----------------------------------------")