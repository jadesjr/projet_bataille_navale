import pytest

from bateau import Bateau, Torpilleur
from grille import Grille


def test_creation():
    g = Grille(5, 8)
    assert g.nb_lignes == 5 and g.nb_colonnes == 8
    assert len(g.cases) == 40
    assert all(c == Grille.vide for c in g.cases)


def test_affichage_bateau_cache():
    g1 = Grille(2, 3)
    g1.ajouter(Bateau(0, 0, longueur=2, vertical=False))
    assert str(g1) == "∿∿∿\n∿∿∿"


def test_affichage_et_depassement():
    g2 = Grille(2, 3)
    g2.ajouter(Bateau(1, 0, longueur=2, vertical=True))
    g2.ajouter(Bateau(1, 0, longueur=4, vertical=True))
    assert str(g2) == "∿∿∿\n∿∿∿"


def test_tir_deja_joue():
    g = Grille(3, 3)
    g.tirer(1, 1)
    assert g.tirer(1, 1) == Grille.DEJA_JOUE


def test_ajout_valide():
    g = Grille(5, 5)
    g.ajouter(Bateau(0, 0, False, 3))
    assert len(g.bateaux) == 1


def test_ajout_depasse():
    g = Grille(5, 5)
    with pytest.raises(ValueError):
        g.ajouter(Bateau(0, 3, False, 3))
    with pytest.raises(ValueError):
        g.ajouter(Bateau(3, 0, True, 3))


def test_ajout_chevauchement():
    g = Grille(5, 5)
    g.ajouter(Bateau(0, 0, False, 3))
    assert not g.peut_ajouter(Bateau(0, 2, True, 3))
    assert g.peut_ajouter(Bateau(1, 0, False, 3))


def test_plouf():
    g = Grille(4, 4)
    assert g.tirer(0, 0) == Grille.PLOUF


def test_touche_puis_coule():
    g = Grille(4, 4)
    b = Torpilleur(1, 1, False)
    g.ajouter(b)
    assert g.tirer(1, 1) == Grille.TOUCHE
    assert g.get(1, 1) == Grille.touche
    assert not g.tous_coules()
    assert g.tirer(1, 2) == Grille.COULE
    assert g.get(1, 1) == b.marque and g.get(1, 2) == b.marque
    assert g.tous_coules()
