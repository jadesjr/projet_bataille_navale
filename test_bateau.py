from bateau import Bateau, PorteAvion, Croiseur, Torpilleur, SousMarin


def test_positions_horizontal():
    assert Bateau(2, 3, longueur=3).positions() == [(2, 3), (2, 4), (2, 5)]


def test_positions_vertical():
    assert Bateau(2, 3, longueur=3, vertical=True).positions() == [
        (2, 3),
        (3, 3),
        (4, 3),
    ]


def test_touche_et_coule():
    b = Bateau(0, 0, False, 2)
    assert not b.est_touche() and not b.est_coule()
    assert b.tirer(0, 0) is True
    assert b.est_touche() and not b.est_coule()
    assert b.tirer(5, 5) is False
    b.tirer(0, 1)
    assert b.est_coule()


def test_tirer_deux_fois_meme_case_ne_coule_pas():
    b = Bateau(0, 0, False, 2)
    b.tirer(0, 0)
    b.tirer(0, 0)
    assert not b.est_coule()


def test_types_de_bateaux():
    assert PorteAvion.longueur == 4
    assert Croiseur.longueur == 3
    assert Torpilleur.longueur == 2
    assert SousMarin.longueur == 2
    marques = {c.marque for c in (PorteAvion, Croiseur, Torpilleur, SousMarin)}
    assert len(marques) == 4
    assert len(PorteAvion(0, 0).positions()) == 4
