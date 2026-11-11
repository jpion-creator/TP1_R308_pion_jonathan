from classes import Livre, Utilisateur
from function import verifier_disponibilite, afficher_separateur

# --- JEU D'ESSAI DEMANDÉ ---
l = Livre("1984", "Orwell", 1949)

print(l.emprunter("Ana")) # Renvoie True
print(l.emprunter("Léo")) # Renvoie False
print(l.rendre())         # Renvoie True

afficher_separateur()

# --- TESTS COMPLÉMENTAIRES DES CLASSES ET FONCTIONS ---

# Affichage des informations du livre
l.afficher()

afficher_separateur()

# Création des utilisateurs
user1 = Utilisateur("Ana")
user2 = Utilisateur("Léo")

# Test d'emprunt par l'utilisateur Ana
user1.emprunter_livre(l)
user1.afficher_emprunts()

afficher_separateur()

# Tentative d'emprunt du même livre par Léo
user2.emprunter_livre(l)

afficher_separateur()

# Vérification du statut du livre via le fichier function
print("Disponibilité du livre :", verifier_disponibilite(l))

afficher_separateur()

# Retour du livre par Ana
user1.rendre_livre(l)
user1.afficher_emprunts()