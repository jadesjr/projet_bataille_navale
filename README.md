# Projet "Bataille navale"

## À propos

Une version  de la bataille navale en python, pour un joueur.

Le jeu se déroule sur une grille de 8 lignes et 10 colonnes. Quatre bateaux sont placés aléatoirement sans se chevaucher : un porte-avion (longueur 4), un croiseur (longueur 3), un torpilleur (longueur 2) et un sous-marin (longueur 2). Le joueur tire case par case jusqu'à avoir coulé tous les bateaux, puis le nombre de coups est affiché.



## Utilisation

Exécutez le fichier `main.py`.


À chaque tour, tapez la ligne puis la colonne séparées par un espace (numérotées à partir de 1), par exemple `3 5`.

Légende de la grille :

- `∿` : case vierge
- `x` : tir raté
- `💣` : bateau touché
- la marque du bateau (🚢, ⛴, 🚣, 🐟) : bateau coulé



## Structure du projet

- `main.py` : lance le jeu
- `bataille_navale.py` : placement aléatoire des bateaux et boucle de jeu
- `grille.py` : la classe `Grille`
- `bateau.py` : la classe `Bateau` et ses sous-classes (`PorteAvion`, `Croiseur`, `Torpilleur`, `SousMarin`)
- `test_*.py` : les tests
- `story_*.py` : les user stories
- `requirements.txt` : les modules nécessaires
