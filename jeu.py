from labigenerator import *
from sessions import *
from msvcrt import *
from time import time

jeu = True


action = ' '
action2 = ' '

while jeu is True:
    while action not in '123456':
        effacer_ecran()
        print("Bonjour, choisissez ce que vous voulez faire")
        print("Créer un nouveau compte et jouer...................1")
        print("Se connecter à un compte déjà existant et jouer....2")
        print("Voir les crédits...................................3")
        print("Voir les meilleurs scores..........................4")
        print("Voir les scores....................................5")
        print("Quitter............................................6")
        action = demander(plage='123456')
        effacer_ecran()

        if action == '1':
            identifiants = creer_compte(verbose=True)

        if action == '2':
            identifiants = connexion()
            if identifiants is False:
                input()
                action = ' '

        if action == '3':
            afficher_credits()
            action = ' '
        
        if action == '4':
            try:
                afficher_meilleurs_scores()
            except:
                print("Il n'y a pas de meilleur score")
                input()
            action = ' '

        if action == '5':
            voir_scores()
            input()
            action = ' '
        
        if action == '6':
            jeu = False
            break
    if action == '6':
        break

    userName = identifiants['user_name']
    password = identifiants['password']

    effacer_ecran()

    if action2 != '2':
        effacer_ecran()
        print("choisissez la taille du labyrinthe")
        print("choisissez une hauteur")
        hauteur = choisir_une_taille(4, 60)
        print("Choisissez une largeur")
        largeur = choisir_une_taille(4, 50)

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
        dep = getch().decode()
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
            duree_partie = date_fin - date_debut
            if largeur >= hauteur:
                facteurX = hauteur / largeur
            else:
                facteurX = largeur / hauteur
            score = round(((largeur*hauteur)*3 / ((nbrCoups+duree_partie) / 2)) * ((facteurX + 1)/2), 2)
            duree_partie = round(date_fin - date_debut, 2)
            print('Vous avez gagné')
            print("La partie a durée", duree_partie, "secondes")
            print("Vous avez mis", nbrCoups, "coups")
            print('Votre score est de', score, 'points')
            enregistrer_score(userName, password, score)
            if determiner_si_meilleur_score(score) is True:
                ajouter_meilleurs_scores(userName, score)
                print("Vous venez de battre votre reccord")
            input()
            print('Si vous voulez recommencer une partie tapez..................1')
            print("Si vous voulez recommencer avec les mêmes paramètres tapez...2")
            print("Pour voir vos scores et recommencer une partie tapez.........3")
            print("Pour retourner au menu tapez.................................4")
            print("Appuyez sur 'entrer' pour valider")
            action2 = demander(plage='1234')
            if action2 == '3':
                voir_scores('autre', userName, password)
                action = '2'
                input()
            elif action2 == '4':
                action = ' '
