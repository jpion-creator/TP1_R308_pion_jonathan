
from classes import Grille
from classes import JoueurHumain , JoueurIA


print("=== MORPION ===")
print("1 Mode 2 Joueurs Humains")
print("2 Simulation IA vs IA (20 parties)")

choix = input("Choisissez le mode (1 ou 2) : ")

  # ----------------------------------------------------
  # MODE 1 : 2 JOUEURS HUMAINS
  # ----------------------------------------------------
if choix == "1":
    g = Grille()
    j1 = JoueurHumain("Joueur 1", "X")
    j2 = JoueurHumain("Joueur 2", "O")
    joueurs = [j1, j2]
    tour = 0

    g.afficher()

    while not g.est_plein():
      # Si le nombre de tour est pair tour % 2 = 0 donc le joueur 1 joue sinon joueur 2 joue 
      joueur_actuel = joueurs[tour % 2]
      print(" Le joueur actuel est le joueur : " )
      print(joueur_actuel.nom, joueur_actuel.symbole)
  

      # Demande les coordonnées et joue la case
      x, y = joueur_actuel.prochain_coup(g, joueur_actuel.symbole)
      g.jouer(x, y, joueur_actuel.symbole)
      g.afficher()

      # Test de victoire
      if g.est_gagnant(joueur_actuel.symbole):
        print(" Nous avons un grand gagnant le plus fort et le plus beau : ")
        print(joueur_actuel)
        break

      # Test de match nul
      if g.est_plein():
        print("Match nul !")
        break

      tour += 1

  # ----------------------------------------------------
  # MODE 2 : SIMULATION IA vs IA (20 PARTIES)
  # ----------------------------------------------------
else:
    print("\n=== SIMULATION 20 PARTIES IA vs IA ===")
    victoires_X = 0
    victoires_O = 0
    matchs_nuls = 0

    for num_partie in range(1, 21):
      g = Grille()
      ia1 = JoueurIA("Robot_1", "X")
      ia2 = JoueurIA("Robot_2", "O")
      joueurs = [ia1, ia2]
      tour = 0

      while not g.est_plein():
        joueur_actuel = joueurs[tour % 2]

        x, y = joueur_actuel.prochain_coup(g, joueur_actuel.symbole)
        g.jouer(x, y, joueur_actuel.symbole)

        if g.est_gagnant(joueur_actuel.symbole):
          if joueur_actuel.symbole == "X":
            victoires_X += 1
            print("Victoire de Robot1 (X) a la partie")
            print(tour)
          else:
            victoires_O += 1
            print("Victoire de Robot2 1(O) a la partie")
            print(tour)
          break

        if g.est_plein():
          matchs_nuls += 1
          print("C'est un match nul pour la partie")
          print(tour)
          break

        tour += 1

    print("\n--- BILAN DES 20 PARTIES ---")
    print("Victoires Robot_1 (X) ")
    print(victoires_X)
    print("Victoires Robot_2 (O)")
    print(victoires_O)
    print("Matchs nuls")
    print(matchs_nuls)