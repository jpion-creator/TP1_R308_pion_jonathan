from classes import Bibliotheque, Livre, Utilisateur
from function import afficher_menu, saisir_annee, charger_sauvegarde_si_existante, afficher_separateur

# Fichier de sauvegarde
fichier_sauvegarde = "livres.csv"

# Initialisation de la bibliothèque et chargement automatique si le fichier existe déjà
biblio = Bibliotheque()
charger_sauvegarde_si_existante(biblio, fichier_sauvegarde)

continuer = True

while continuer == True:
    afficher_menu()
    choix = input("Votre choix (1-6) : ")
    afficher_separateur()

    if choix == "1":
        titre = input("Entrez le titre du livre : ")
        auteur = input("Entrez l'auteur du livre : ")
        annee = saisir_annee()
        
        # On ne crée le livre que si l'année saisie est valide
        if annee != None:
            nouveau_livre = Livre(titre, auteur, annee)
            biblio.ajouter_livre(nouveau_livre)

    elif choix == "2":
        nom = input("Entrez le nom de l'utilisateur : ")
        if nom != "":
            nouvel_utilisateur = Utilisateur(nom)
            biblio.ajouter_utilisateur(nouvel_utilisateur)
        else:
            print("Erreur : Le nom d'utilisateur ne peut pas être vide.")

    elif choix == "3":
        nom = input("Nom de l'emprunteur : ")
        titre = input("Titre du livre à emprunter : ")
        biblio.emprunter(nom, titre)

    elif choix == "4":
        nom = input("Nom de l'emprunteur : ")
        titre = input("Titre du livre à rendre : ")
        biblio.rendre(nom, titre)

    elif choix == "5":
        biblio.afficher_livres()

    elif choix == "6":
        print("Sauvegarde en cours et fermeture du programme...")
        biblio.sauvegarder_csv(fichier_sauvegarde)
        print("Au revoir !")
        continuer = False

    else:
        # Gestion des choix invalides (ex: choix "9") sans plantage du programme
        print("Choix invalide ! Veuillez saisir un nombre compris entre 1 et 6.")