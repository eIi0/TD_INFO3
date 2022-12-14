# -*- coding:Latin-1 -*-
from turtle import *
from math import *

def carre(taille, couleur):
    "fonction qui dessine un carré de taille et de couleur déterminées"
    color(couleur)
    c =0
    while c <4:
        forward(taille)
        right(90)
        c = c +1


# Exercice 1

def triangle_eq(taille, couleur):
    "fonction qui dessine un triangle de taille et de couleur déterminées"
    color(couleur)
    c =0
    while c <3:
        forward(taille)
        right(120)
        c = c +1

#exercie 2

def triangle_iso(taille, couleur, angle):
    "fonction qui dessine un triangle de couleur, taille et angle non détérminé"
    color(couleur)
    tai = taille * sin(pi/4)
    left(angle)
    forward(taille)
    left(135)
    forward(tai)
    left(90)
    forward(tai)

    

i = 0
while i<2:
    down()
    triangle_iso(150,'blue', 70) #appel de la fonction triangle libre
    up()
    forward(30)
    i = i+1
g = input() #attente