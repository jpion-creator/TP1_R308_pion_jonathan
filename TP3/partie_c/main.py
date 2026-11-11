from classes import Livre, Utilisateur, Bibliotheque
from function import verifier_fichier_csv, afficher_separateur

# Définition du nom du fichier de sauvegarde CSV
fichier_sauvegarde = "livres.csv"

# Verification du format du fichier
assert verifier_fichier_csv(fichier_sauvegarde) == True

print("=== ÉTAPE 1 : CRÉATION DE LA PREMIÈRE BIBLIOTHÈQUE ET EMPRUNT ===")

# Instanciation de la première bibliothèque
biblio1 = Bibliotheque()

# Création du livre et de l'utilisateur
l1 = Livre("1984", "Orwell", 1949)
u1 = Utilisateur("Ana")

# Ajout à la première bibliothèque
biblio1.ajouter_livre(l1)
biblio1.ajouter_utilisateur(u1)

afficher_separateur()

# Ana emprunte 1984
biblio1.emprunter("Ana", "1984")

# Verification de l'état avant sauvegarde
biblio1.afficher_livres()

afficher_separateur()

# Sauvegarde dans le fichier CSV
biblio1.sauvegarder_csv(fichier_sauvegarde)

afficher_separateur()

print("=== ÉTAPE 2 : NOUVELLE BIBLIOTHÈQUE ET RECHARGEMENT DES DONNÉES ===")

# Création d'une TOUTE NOUVELLE instance de bibliothèque vide
biblio2 = Bibliotheque()

# Rechargement des données depuis le fichier CSV
biblio2.charger_csv(fichier_sauvegarde)

afficher_separateur()

# Verification que '1984' est bien présent et emprunté par Ana
biblio2.afficher_livres()

afficher_separateur()

print("=== ÉTAPE 3 : TEST DU RETOUR DU LIVRE PAR ANA DANS LA NOUVELLE BIBLIOTHÈQUE ===")

# Ana rend le livre dans la nouvelle bibliothèque
biblio2.rendre("Ana", "1984")

afficher_separateur()

# Affichage final pour valider la remise en disponibilité
biblio2.afficher_livres()