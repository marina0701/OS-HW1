"""Calling the functions to perform the conversion"""

from test import test_roem
from utils import roem

zahl = int(input("Bitte gebe eine Zahl ein die als Römische Zahl dargestellt werden soll:"))
print("info: I=5, V=5, X=10, L=50, C=100, D=500, M=1000")
print(roem(zahl))
print(test_roem(zahl))
