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

    def afficher(self):
        """ Fonction intégrée dans la classe Livre permettant d'afficher les informations du livre avec des print """
        print("Titre : " + str(self.titre))
        print("Auteur : " + str(self.auteur))
        print("Année : " + str(self.annee))
        if self.disponible == True:
            print("Statut : Disponible")
        else:
            print("Statut : Indisponible")

    def emprunter(self, nom_emprunteur):
        """ Fonction permettant d'emprunter un livre. Renvoie True si l'emprunt réussit, False sinon """
        assert isinstance(nom_emprunteur, str)
        if self.disponible == True:
            self.disponible = False
            return True
        else:
            return False

    def rendre(self):
        """ Fonction permettant de rendre un livre. Renvoie True si le livre a été rendu, False sinon """
        if self.disponible == False:
            self.disponible = True
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