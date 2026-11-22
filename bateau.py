class Bateau:
    longueur = 1
    marque = "B"
    nom = "bateau"
    message_coule = "Un bateau a été coulé !"

    def __init__(self, ligne, colonne, vertical=False, longueur=None):
        if longueur is not None:
            self.longueur = longueur
        self.ligne = ligne
        self.colonne = colonne
        self.vertical = vertical
        self.touches = []

    def positions(self):
        if self.vertical:
            return [(self.ligne + i, self.colonne) for i in range(self.longueur)]
        else:
            return [(self.ligne, self.colonne + i) for i in range(self.longueur)]

    def tirer(self, ligne, colonne):
        if (ligne, colonne) in self.positions():
            if (ligne, colonne) not in self.touches:
                self.touches.append((ligne, colonne))
            return True
        return False

    def est_touche(self):
        return len(self.touches) > 0

    def est_coule(self):
        return len(self.touches) == self.longueur

    def chevauche(self, autre):
        return any(pos in autre.positions() for pos in self.positions())


class PorteAvion(Bateau):
    longueur = 4
    marque = "🚢"
    nom = "porte-avion"
    message_coule = "Le porte-avion est coulé !"


class Croiseur(Bateau):
    longueur = 3
    marque = "⛴"
    nom = "croiseur"
    message_coule = "Le croiseur est coulé !"


class Torpilleur(Bateau):
    longueur = 2
    marque = "🚣"
    nom = "torpilleur"
    message_coule = "Le torpilleur est coulé !"


class SousMarin(Bateau):
    longueur = 2
    marque = "🐟"
    nom = "sous-marin"
    message_coule = "Le sous-marin est coulé !"
