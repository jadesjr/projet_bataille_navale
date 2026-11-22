"""
User story : « Plouf dans l'eau »
Utilisateur : un joueur
Story : on veut pouvoir gérer les tirs de l'adversaire.
Actions :
    1. créer une grille de 5 lignes et 8 colonnes
    2. afficher la grille à l'écran
    3. demander à l'utilisateur de rentrer deux coordonnées
    4. tirer à l'endroit indiqué sur la grille
    5. retour en 2
(taper « q » pour quitter)
"""

from grille import Grille

g = Grille(5, 8)
while True:
    print(g)
    saisie = input("Tirer en (ligne colonne, à partir de 0) ou q : ")
    if str(saisie) == "q":
        break
    else:
        ligne, colonne = (int(x) for x in saisie.split())
        print(g.tirer(ligne, colonne))
