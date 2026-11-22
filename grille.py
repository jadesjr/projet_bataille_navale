class Grille:
    vide = "∿"
    rate = "x"
    touche = "💣"

    # résultats possibles d'un tir
    PLOUF = "plouf"
    TOUCHE = "touché"
    COULE = "coulé"
    DEJA_JOUE = "déjà joué"

    def __init__(self, nb_lignes, nb_colonnes):
        self.nb_lignes = nb_lignes
        self.nb_colonnes = nb_colonnes
        self.cases = [self.vide] * (nb_lignes * nb_colonnes)
        self.bateaux = []

    def _indice(self, ligne, colonne):
        return ligne * self.nb_colonnes + colonne

    def get(self, ligne, colonne):
        return self.cases[self._indice(ligne, colonne)]

    def cases_occupees(self):
        occupees = []
        for bateau in self.bateaux:
            for pos in bateau.positions():
                occupees.append(pos)
        return occupees

    def dans_grille(self, ligne, colonne):
        return 0 <= ligne < self.nb_lignes and 0 <= colonne < self.nb_colonnes

    def peut_ajouter(self, bateau):
        positions = bateau.positions()
        occupees = self.cases_occupees()
        for p in positions:
            l, c = p
            if not self.dans_grille(l, c):
                return False
            if p in occupees:
                return False
        return True

    def ajouter(self, bateau):
        if self.peut_ajouter(bateau):
            self.bateaux.append(bateau)

    def bateau_en(self, ligne, colonne):
        for bateau in self.bateaux:
            if (ligne, colonne) in bateau.positions():
                return bateau
        return None

    def tirer(self, ligne, colonne):
        indice = self._indice(ligne, colonne)
        if self.cases[indice] != self.vide:
            return self.DEJA_JOUE

        bateau = self.bateau_en(ligne, colonne)
        if bateau is None:
            self.cases[indice] = self.rate
            return self.PLOUF
        else:
            bateau.tirer(ligne, colonne)
            self.cases[indice] = self.touche
            if bateau.est_coule():
                for l, c in bateau.positions():
                    self.cases[self._indice(l, c)] = bateau.marque
                return self.COULE
            return self.TOUCHE

    def tous_coules(self):
        return all(b.est_coule() for b in self.bateaux)

    def __str__(self):
        resultat = ""
        for l in range(self.nb_lignes):
            for c in range(self.nb_colonnes):
                resultat += str(self.cases[self._indice(l, c)])
            if l < self.nb_lignes - 1:
                resultat += "\n"
        return resultat
