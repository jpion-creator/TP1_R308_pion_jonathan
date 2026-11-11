from classes import Bibliotheque

def verifier_fichier_csv(nom_fichier):
    """ Fonction auxiliaire permettant de vérifier si le nom du fichier possède une extension .csv """
    assert isinstance(nom_fichier, str)
    if nom_fichier.endswith(".csv"):
        return True
    else:
        return False

def afficher_separateur():
    """ Fonction auxiliaire permettant d'afficher une ligne de séparation dans la console """
    print("----------------------------------------")