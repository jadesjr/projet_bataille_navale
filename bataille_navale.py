import random
from termcolor import colored
from bateau import PorteAvion, Croiseur, Torpilleur, SousMarin
from grille import Grille

NB_LIGNES = 8
NB_COLONNES = 10
TYPES_BATEAUX = [PorteAvion, Croiseur, Torpilleur, SousMarin]


def placer_aleatoirement(grille, types_bateaux):
    for type_bateau in types_bateaux:
        candidats = []
        for ligne in range(grille.nb_lignes):
            for colonne in range(grille.nb_colonnes):
                for vertical in (False, True):
                    bateau = type_bateau(ligne, colonne, vertical)
                    if grille.peut_ajouter(bateau):
                        candidats.append(bateau)

        grille.ajouter(random.choice(candidats))


def nouvelle_partie():
    grille = Grille(NB_LIGNES, NB_COLONNES)
    placer_aleatoirement(grille, TYPES_BATEAUX)
    return grille


def lire_coup(grille):
    # Demande une case au joueur (numérotée à partir de 1)
    while True:
        saisie = input(
            f"Tirez (ligne 1-{grille.nb_lignes} " f"colonne 1-{grille.nb_colonnes}) : "
        )

        ligne, colonne = (int(x) for x in saisie.split())

        return ligne - 1, colonne - 1


def jouer(grille=None):
    if grille is None:
        grille = nouvelle_partie()
    coups = 0
    print(" BATAILLE NAVALE ")
    while not grille.tous_coules():
        print()
        print(grille)
        ligne, colonne = lire_coup(grille)
        resultat = grille.tirer(ligne, colonne)
        if resultat == Grille.DEJA_JOUE:
            print("Vous avez déjà tiré ici")
            continue
        coups += 1
        if resultat == Grille.PLOUF:
            print(colored("Plouf...", "blue"))
        elif resultat == Grille.TOUCHE:
            print(colored("Touché ", "yellow"))
        else:
            print(colored((grille.bateau_en(ligne, colonne).message_coule, "red")))
    print()
    print(grille)
    print(colored(f"Bravo ! Tous les bateaux sont coulés en {coups} coups.", "green", attrs=["bold"]))
    return coups
