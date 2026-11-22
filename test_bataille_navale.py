import pytest
import random
from termcolor import colored
from bataille_navale import (
    NB_LIGNES,
    NB_COLONNES,
    TYPES_BATEAUX,
    jouer,
    nouvelle_partie,
)


def test_placement_aleatoire_valide():
    g = nouvelle_partie()
    assert len(g.bateaux) == 4
    total = sum(len(b.positions()) for b in g.bateaux)
    assert total == sum(t.longueur for t in TYPES_BATEAUX)
    assert len(g.cases_occupees()) == total  # pas de chevauchement
    for l, c in g.cases_occupees():
        assert 0 <= l < NB_LIGNES and 0 <= c < NB_COLONNES
