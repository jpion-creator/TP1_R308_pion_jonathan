import os
from classes import Bibliotheque, Livre, Utilisateur

def afficher_menu():
    """ Fonction permettant d'afficher le menu interactif de la bibliothèque """
    print("\n--- MENU BIBLIOTHÈQUE ---")
    print("1. Ajouter un livre")
    print("2. Ajouter un utilisateur")
    print("3. Emprunter un livre")
    print("4. Rendre un livre")
    print("5. Afficher les livres")
    print("6. Quitter et sauvegarder")

def saisir_annee():
    """ Fonction vérifiant si la saisie de l'année est bien numérique pour éviter le plantage """
    saisie = input("Entrez l'année de parution : ")
    if saisie.isdigit() == True:
        return int(saisie)
    else:
        print("Erreur : L'année doit être une valeur numérique !")
        return None

def charger_sauvegarde_si_existante(biblio, nom_fichier):
    """ Fonction qui charge automatiquement les données si le fichier CSV existe au démarrage """
    assert isinstance(biblio, Bibliotheque)
    assert isinstance(nom_fichier, str)
    if os.path.exists(nom_fichier) == True:
        biblio.charger_csv(nom_fichier)
    else:
        print("Aucune sauvegarde existante trouvée. Démarrage d'une nouvelle session.")

def afficher_separateur():
    """ Fonction auxiliaire permettant d'afficher une ligne de séparation """
    print("----------------------------------------")