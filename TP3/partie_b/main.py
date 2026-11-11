from classes import Livre, Utilisateur, Bibliotheque
from function import verifier_existence_livre, afficher_separateur

# Création de l'instance principale de la bibliothèque
biblio = Bibliotheque()

# Instanciation de quelques livres et utilisateurs
l1 = Livre("1984", "Orwell", 1949)
l2 = Livre("Le Petit Prince", "Saint-Exupéry", 1943)

u1 = Utilisateur("Ana")
u2 = Utilisateur("Léo")

# Ajout à la bibliothèque
biblio.ajouter_livre(l1)
biblio.ajouter_livre(l2)
biblio.ajouter_utilisateur(u1)
biblio.ajouter_utilisateur(u2)

afficher_separateur()

# --- JEU D'ESSAI DEMANDÉ (Gestion des erreurs sans plantage) ---

print("1. Test : Emprunt réussi par Ana")
biblio.emprunter("Ana", "1984")

afficher_separateur()

print("2. Test : Tentative d'emprunt d'un livre déjà emprunté (Léo veut 1984)")
biblio.emprunter("Léo", "1984")

afficher_separateur()

print("3. Test : Utilisateur inconnu (Marc veut Le Petit Prince)")
biblio.emprunter("Marc", "Le Petit Prince")

afficher_separateur()

print("4. Test : Titre de livre inconnu (Ana veut Harry Potter)")
biblio.emprunter("Ana", "Harry Potter")

afficher_separateur()

# Vérification de l'affichage du catalogue (Disponibles vs Empruntés)
biblio.afficher_livres()

afficher_separateur()

print("5. Test : Retour du livre 1984 par Ana")
biblio.rendre("Ana", "1984")

afficher_separateur()

# Affichage final du catalogue pour valider le retour
biblio.afficher_livres()