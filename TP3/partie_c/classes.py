import csv

class Livre():
    def __init__(self, titre, auteur, annee):
        # Verification des types d'arguments
        assert isinstance(titre, str)
        assert isinstance(auteur, str)
        assert isinstance(annee, int)
        
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = True
        self.emprunteur = None

    def afficher(self):
        """ Fonction intégrée dans la classe Livre permettant d'afficher les informations du livre avec des print """
        print("Titre : " + str(self.titre))
        print("Auteur : " + str(self.auteur))
        print("Année : " + str(self.annee))
        if self.disponible == True:
            print("Statut : Disponible")
        else:
            print("Statut : Indisponible (Emprunté par : " + str(self.emprunteur) + ")")

    def emprunter(self, nom_emprunteur):
        """ Fonction permettant d'emprunter un livre. Renvoie True si l'emprunt réussit, False sinon """
        assert isinstance(nom_emprunteur, str)
        if self.disponible == True:
            self.disponible = False
            self.emprunteur = nom_emprunteur
            return True
        else:
            return False

    def rendre(self):
        """ Fonction permettant de rendre un livre. Renvoie True si le livre a été rendu, False sinon """
        if self.disponible == False:
            self.disponible = True
            self.emprunteur = None
            return True
        else:
            return False


class Utilisateur():
    def __init__(self, nom):
        # Verification du nom de l'utilisateur
        assert isinstance(nom, str)
        self.nom = nom
        self.emprunts = []

    def emprunter_livre(self, livre):
        """ Fonction permettant à un utilisateur d'emprunter un livre """
        assert isinstance(livre, Livre)
        if livre.emprunter(self.nom) == True:
            self.emprunts.append(livre)
            print("Livre ajouté aux emprunts de " + str(self.nom))
        else:
            print("Impossible d'emprunter ce livre pour " + str(self.nom))

    def rendre_livre(self, livre):
        """ Fonction permettant à un utilisateur de rendre un livre qu'il a emprunté """
        assert isinstance(livre, Livre)
        if livre in self.emprunts:
            if livre.rendre() == True:
                self.emprunts.remove(livre)
                print("Livre retiré des emprunts de " + str(self.nom))
        else:
            print("Ce livre ne fait pas partie des emprunts de " + str(self.nom))

    def afficher_emprunts(self):
        """ Fonction permettant d'afficher la liste des livres empruntés par l'utilisateur """
        print("--- Emprunts de " + str(self.nom) + " ---")
        if len(self.emprunts) == 0:
            print("Aucun emprunt en cours.")
        else:
            for livre in self.emprunts:
                livre.afficher()


class Bibliotheque():
    def __init__(self):
        # Initialisation des dictionnaires pour stocker les livres et utilisateurs
        self.livres = {}
        self.utilisateurs = {}

    def ajouter_livre(self, livre):
        """ Fonction permettant d'ajouter un objet Livre au dictionnaire de la bibliothèque """
        assert isinstance(livre, Livre)
        if livre.titre in self.livres:
            print("Attention : Le livre '" + str(livre.titre) + "' existe déjà.")
        else:
            self.livres[livre.titre] = livre
            print("Livre '" + str(livre.titre) + "' ajouté à la bibliothèque.")

    def ajouter_utilisateur(self, utilisateur):
        """ Fonction permettant d'ajouter un objet Utilisateur au dictionnaire de la bibliothèque """
        assert isinstance(utilisateur, Utilisateur)
        if utilisateur.nom in self.utilisateurs:
            print("Attention : L'utilisateur '" + str(utilisateur.nom) + "' existe déjà.")
        else:
            self.utilisateurs[utilisateur.nom] = utilisateur
            print("Utilisateur '" + str(utilisateur.nom) + "' inscrit à la bibliothèque.")

    def emprunter(self, nom, titre):
        """ Fonction gérant l'emprunt d'un livre via le nom de l'utilisateur et le titre du livre """
        assert isinstance(nom, str)
        assert isinstance(titre, str)

        # Verification si l'utilisateur existe
        if nom not in self.utilisateurs:
            print("Échec emprunt : L'utilisateur '" + str(nom) + "' est inconnu.")
            return False

        # Verification si le livre existe dans la bibliothèque
        if titre not in self.livres:
            print("Échec emprunt : Le livre '" + str(titre) + "' est inconnu.")
            return False

        utilisateur = self.utilisateurs[nom]
        livre = self.livres[titre]

        # Verification de la disponibilité
        if livre.disponible == False:
            print("Échec emprunt : Le livre '" + str(titre) + "' est déjà emprunté.")
            return False

        utilisateur.emprunter_livre(livre)
        return True

    def rendre(self, nom, titre):
        """ Fonction gérant le retour d'un livre par un utilisateur """
        assert isinstance(nom, str)
        assert isinstance(titre, str)

        # Verification de l'existence de l'utilisateur
        if nom not in self.utilisateurs:
            print("Échec retour : L'utilisateur '" + str(nom) + "' est inconnu.")
            return False

        # Verification de l'existence du livre
        if titre not in self.livres:
            print("Échec retour : Le livre '" + str(titre) + "' est inconnu.")
            return False

        utilisateur = self.utilisateurs[nom]
        livre = self.livres[titre]

        utilisateur.rendre_livre(livre)
        return True

    def afficher_livres(self):
        """ Fonction affichant la liste des livres de la bibliothèque séparés selon leur disponibilité """
        print("=== CATALOGUE DE LA BIBLIOTHÈQUE ===")
        
        # Affichage des livres disponibles
        print("-- Livres disponibles --")
        compteur_dispo = 0
        for titre in self.livres:
            livre = self.livres[titre]
            if livre.disponible == True:
                print("- " + str(livre.titre) + " (" + str(livre.auteur) + ", " + str(livre.annee) + ")")
                compteur_dispo += 1
        if compteur_dispo == 0:
            print("Aucun livre disponible.")

        # Affichage des livres empruntés
        print("-- Livres empruntés --")
        compteur_emprunte = 0
        for titre in self.livres:
            livre = self.livres[titre]
            if livre.disponible == False:
                print("- " + str(livre.titre) + " (" + str(livre.auteur) + ", " + str(livre.annee) + ") [Emprunté par : " + str(livre.emprunteur) + "]")
                compteur_emprunte += 1
        if compteur_emprunte == 0:
            print("Aucun livre emprunté.")

    def sauvegarder_csv(self, nom_fichier):
        """ Fonction permettant de sauvegarder l'état des livres dans un fichier CSV (titre, auteur, annee, disponible, emprunteur) """
        assert isinstance(nom_fichier, str)
        fichier = open(nom_fichier, mode="w", newline="", encoding="utf-8")
        writer = csv.writer(fichier)
        
        # Ecriture de l'en-tête CSV
        writer.writerow(["titre", "auteur", "annee", "disponible", "emprunteur"])
        
        # Parcours et écriture de chaque livre
        for titre in self.livres:
            livre = self.livres[titre]
            emprunteur_str = livre.emprunteur
            if emprunteur_str == None:
                emprunteur_str = "None"
            writer.writerow([livre.titre, livre.auteur, livre.annee, livre.disponible, emprunteur_str])
        
        fichier.close()
        print("Sauvegarde réussie dans " + str(nom_fichier))

    def charger_csv(self, nom_fichier):
        """ Fonction permettant de charger les livres depuis un fichier CSV dans une nouvelle bibliothèque """
        assert isinstance(nom_fichier, str)
        fichier = open(nom_fichier, mode="r", encoding="utf-8")
        reader = csv.reader(fichier)
        
        # Ignorer la ligne d'en-tête
        en_tete = next(reader, None)
        
        for ligne in reader:
            if len(ligne) >= 5:
                titre = ligne[0]
                auteur = ligne[1]
                annee = int(ligne[2])
                disponible_str = ligne[3]
                emprunteur_str = ligne[4]
                
                # Reconstitution de l'objet Livre
                livre = Livre(titre, auteur, annee)
                
                if disponible_str == "False":
                    livre.disponible = False
                    livre.emprunteur = emprunteur_str
                    
                    # Reconstruction automatique de l'utilisateur et de sa liste d'emprunts
                    if emprunteur_str != "None" and emprunteur_str != "":
                        if emprunteur_str not in self.utilisateurs:
                            u = Utilisateur(emprunteur_str)
                            self.utilisateurs[emprunteur_str] = u
                        
                        self.utilisateurs[emprunteur_str].emprunts.append(livre)
                
                self.livres[titre] = livre
        
        fichier.close()
        print("Chargement réussi depuis " + str(nom_fichier))