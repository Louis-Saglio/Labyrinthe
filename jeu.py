#ajouter le score au stat du joueur

from labigenerator import *
from module import *
from sessions import *
from time import time

action = ' '
while action not in ('123'):
    effacer_ecran()
    print("Bonjour, choisissez ce que vous voulez faire")
    print("Créer un nouveau compte et jouer...................1")
    print("Se connecter à un compte déjà existant et jouer....2")
    print("Voir les crédits et jouer..........................3")
    action = input()

if action == '1':
    effacer_ecran()
    creer_compte(verbose=True)


if action == '2':
    effacer_ecran()
    user = False
    while user is False:
        user = connexion()

if action == '3':
    effacer_ecran()
    afficher_credits()
    input()

effacer_ecran()

print("choisissez la taille du labyrinthe")
effacer_ecran()
print("Choisissez une largeur")
hauteur = choisir_une_taille(4,60)
print("choisissez une hauteur")
largeur = choisir_une_taille(4,50)

effacer_ecran()
input("Utilisez les touches 's' 'z' 'd' 'q' pour vous diriger puis 'entrée' pour valider\nentrée pour continuer")

matrice = creer_laby(hauteur, largeur)

nbrCoups = 0
hl = trouver_X(matrice)
h = hl[0]
l = hl[1]

date_debut = time()
victoire = False
while victoire is False:
    effacer_ecran()
    afficher_matrice(matrice)
    hnew = h
    lnew = l
    dep = input()
    nbrCoups += 1
    if dep == 'z':
        hnew -= 1
    elif dep == 's':
        hnew += 1
    elif dep == 'd':
        lnew += 1
    elif dep == 'q':
        lnew -= 1
    if matrice[hnew][lnew] == ' ':
        matrice[h][l] = ' '
        h = hnew
        l = lnew
        matrice[h][l] = 'X'
    elif matrice[hnew][lnew] == 'A':
        matrice[h][l] = ' '
        matrice[hnew][lnew] = 'X'
        victoire = True
        effacer_ecran()
        afficher_matrice(matrice)
        date_fin = time()
        duree_partie = round(date_fin - date_debut)
        print('Vous avez gagné')
        print("La partie a durée", duree_partie, "secondes")
        print("Vous avez mis", nbrCoups, "coups")
        print('Votre score est de', round((largeur*hauteur)*3 / (((nbrCoups)+(duree_partie)) / 2)), 'points')