from classes import Livre

def verifier_disponibilite(livre):
    """ Fonction permettant de vérifier si un livre est disponible """
    assert isinstance(livre, Livre)
    if livre.disponible == True:
        return True
    else:
        return False

def afficher_separateur():
    """ Fonction auxiliaire permettant d'afficher une ligne de séparation dans la console """
    print("----------------------------------------")