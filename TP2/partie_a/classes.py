class Grille():
    def __init__(self):
        self.liste = ( [None,None,None],
                        [None,None,None],
                         [None,None,None] )
    def afficher(self):
        """ Fonction intégrée dans la classe Grille permettant d'afficher le contenu de la grille avec des print"""
        # Taille de la grille 3*3 
        assert len(self.liste) == 3 
        afficher = ""
        for ligne in self.liste : 
            for elt in ligne : 
                if elt == None : 
                    afficher += "| |"
                if elt == "O":
                    afficher += "|O|"
                if elt == "X": 
                    afficher += "|X|"
            afficher += "\n"
            afficher += '----------'
            afficher += "\n"
        print(afficher)
    def jouer(self,x,y,symbole):
        """ Fonction permettant de modifier la grille de jeu : On ne prend en argument que des coordonnées comprises en 0 et 2, On ne peut jouer que des "O" ou des "X" ! """
        self.x = x
        self.y = y
        self.symbole = symbole
        assert x in [0,1,2] and y in [0,1,2]
        assert self.symbole in ["O","X"]
        if self.liste[x][y] == None:
           self.liste[x][y] = self.symbole
        else:
            print("Case déja jouée il faut en choisir une autre !")
    def est_pleind(self):
            """ Fonction qui renvoie True si la grille est pleine False dans le cas contraire """
            # Taille de la grille 3*3 
            assert len(self.liste) == 3 
            afficher = ""
            for ligne in self.liste : 
                for elt in ligne : 
                    if elt != None :
                       pass
                    else:
                       return False
            return True

    def est_gagnant(self, symbole):
     """Fonction permettant de vérifier si un symbole ('X' ou 'O') a gagné."""
     assert symbole in ["O", "X"]

     #Vérification des lignes
     for i in range(3):
       verif = 0
       for j in range(3):
         if self.liste[i][j] == symbole:
           verif += 1

       if verif == 3:
         return True

    #Vérification des colonnes
     for j in range(3):
       verif = 0
       for i in range(3):
         if self.liste[i][j] == symbole:
           verif += 1
       if verif == 3:
         return True

    #Vérification de la première diagonale (\)
     if (
         self.liste[0][0] == symbole
         and self.liste[1][1] == symbole
         and self.liste[2][2] == symbole
     ):
      return True

    #Vérification de la deuxième diagonale (/)
     if (
         self.liste[0][2] == symbole
         and self.liste[1][1] == symbole
         and self.liste[2][0] == symbole
     ):
      return True

     return False




           

        


