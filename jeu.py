#ajouter moyenne joueur
#ajouter les meilleurs scores
#sécuriser les inputs

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
    print("Voir les crédits...................................3")
    action = input()
    effacer_ecran()

    if action == '1':
        identifiants = creer_compte(verbose=True)

    if action == '2':
        identifiants = False
        while identifiants is False:
            identifiants = connexion()

    if action == '3':
        afficher_credits()
        action = ' '

userName = identifiants['user_name']
password = identifiants['password']
print(userName)
print(password)
input()

effacer_ecran()

print("choisissez la taille du labyrinthe")
effacer_ecran()
print("choisissez une hauteur")
hauteur = choisir_une_taille(4,60)
print("Choisissez une largeur")
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
        score = round((largeur*hauteur)*3 / (((nbrCoups)+(duree_partie)) / 2))
        print('Vous avez gagné')
        print("La partie a durée", duree_partie, "secondes")
        print("Vous avez mis", nbrCoups, "coups")
        print('Votre score est de', score, 'points')
        enregistrer_score(userName, password, score)