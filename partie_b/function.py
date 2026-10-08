from random import randint

int_alea = 0

def initialiser_nombre(borne_sup , borne_inf,):
    assert type(borne_sup) == int and type(borne_inf) == int 
    """ fonction prenant en paramètre deux nombre entier en tant que  bornes  permettant d'initialiser une valeur aleatoire à découvrir avec la fonction devine_nombre()"""
    global int_alea
    assert borne_sup != 0 and borne_inf != 0 
    assert borne_inf <= borne_sup
    int_alea = randint(borne_inf, borne_sup)

def devine_nombre(nombre_choisi):
    """ fonction prenant en paramètre un nombre entier renvoyant Bon nombre !  si le nombre entré est celui initalisé aléatoirement Trop petit si le nombre choisis est trop petit, Trop grand dans le cas contraire"""
    if nombre_choisi == int_alea:
        return "Bon nombre ! "
    if nombre_choisi < int_alea:
        return "Trop petit ! "
    return "Trop grand !"
