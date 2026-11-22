"""
User story : « chevauchement »
Utilisateur : un joueur
Story : positionner des bateaux sans qu'ils se chevauchent.
Actions :
    1. créer un bateau
    2. créer un deuxième bateau
    3. vérifier si les deux bateaux se chevauchent
"""

from bateau import Bateau

b1 = Bateau(2, 1, vertical=False, longueur=3)
b2 = Bateau(0, 2, vertical=True, longueur=4)
b3 = Bateau(5, 5, vertical=True, longueur=2)

print("b1 :", b1.positions())
print("b2 :", b2.positions())
print("b3 :", b3.positions())
print("b1 et b2 se chevauchent ?", b1.chevauche(b2))  # True
print("b1 et b3 se chevauchent ?", b1.chevauche(b3))  # False
