# Fichier regroupant les fonctions du projet 
from classes import Etudiant
def ajouter_etudiant(dico,nom, note):
    """ Fonction prennant en argument un dictionnaire un nom ( chaine de caractere) et une note ( Entier ou flotant ) permettant d'ajouter un etudiant dans le dictionnaire en paramètre
        Le dictionnaire pris en compte"""
    assert type(nom) == str
    assert type(note) == float or type(note) == int
    
    nouveau_etudiant = Etudiant(nom,note)
    dico[nouveau_etudiant.nom ] = nouveau_etudiant

def moyenne_classe(dico):

    """ Fonction renvoyant la moyenne des etudiants (Flottant ou entier) stocke dans le dictionnaire en parametre. Renvoie None si le dictionnaire est vide ou qu'une donnée est invalide  """

    if len(dico) == 0 :
        return None
    
    moyenne = 0
    for etudiant in dico :
        if type(dico[etudiant] ) != Etudiant :
            return None
        moyenne += dico[etudiant].note

    return moyenne / len(dico)

def meilleur_etudiant(dico):
    """Fonction renvoyant l'étudiant avec la meilleure note (nom, note).
    Renvoie None si le dictionnaire est vide ou qu'une donnée est invalide.
    """
    if not dico:
        return None

    etudiant_meilleur = None
    maxi = -1  #La meilleur note sera toujours comprise entre 0 et 20 c'est une note pour définir la variable mais qui ne sera jamais renvoyé avec la valeur -1

    for eleve in dico.values():
        if not isinstance(eleve, Etudiant): #Renvoie None si la donnée analysée n'est pas un etudiant 
            return None
        if eleve.note > maxi:
            maxi = eleve.note
            etudiant_meilleur = eleve

    return (etudiant_meilleur.nom, etudiant_meilleur.note)