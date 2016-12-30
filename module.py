def afficher_matrice(matrice):
    for h in range(len(matrice)):
        for l in range(len(matrice[0])):
            if l == len(matrice[0])-1:
                print(matrice[h][l])
            else:
                print(matrice[h][l], ' ', end='')

# Fonction encore en développement utilisé pour l'affichage graphique (en cours d'implémentation)
def retourner_laby_str(matrice):
    labi = ''
    for h in range(len(matrice)):
        for l in range(len(matrice[0])):
            labi += matrice[h][l]
            if l == len(matrice[0])-1:                
                labi += '\n'
            else:
                labi += ' '
    return labi

def choisir_une_taille(min, max):
    bonneTaille = False
    while bonneTaille is False:
        try:
            taille = int(demander())
            if taille < min:
                print("Trop petit")
            elif taille > max:
                print("Trop grand")
            else:
                bonneTaille = True
        except:
            print("C'est pourtant pas compliqué de choisir une taille normale non ?")
    return taille

def trouver_X(matrice, joueur='X'):
    for h in range(len(matrice)):
        for l in range(len(matrice[0])):
            if matrice[h][l] == joueur:
                return [h,l]

def effacer_ecran():
    from os import system
    try:
        system('cls')
        sys = 'dos'
    except:
        system('clear')
        sys = 'unix'
    if sys == 'dos':
        system('cls')
    else:
        system('clear')

def afficher_credits():
    print("Bienvenue dans ce jeu du labyrinthe.")
    print("Il a été intégralement dévellopé en Python 3.5 par Louis Saglio.")
    print("Le code source a été à 100% inventé par Louis Saglio et n'est aucunement issu de copier-collé (ou autre) de code d'un tiers")
    print("Dans ce jeu vous devrez rejoindre le point marqué 'A' se trouvant en-bas à droite du labyrinthe")
    print("Le labyrinthe sera généré par un script, et vous pourrez en choisir la taille")
    print("Le jeu a été originelement développé pour MS-DOS mais normalement il fonctionne également sous UNIX")
    print("Vous êtes libre de copier, modifier, vendre ou distribuer ce programme à condition de mentionner son auteur, 24/12/16")
    input("Appuyez sur 'entrée' pour continuer")

def chiffrage(mot, clef, sens='chiffrage'):
    i = 0
    mot_chiffree = ''
    for lettre in mot:        
        if sens == 'chiffrage':
            etape = ord(lettre) + ord(clef[i])            
        else:
            etape = ord(lettre) - ord(clef[i])
        mot_chiffree += chr(etape % 127)
    i += 1
    if i == len(clef):
        i = 0
    return mot_chiffree

def gen_mot_rand():
    from random import randint
    mot = ''
    alpha = "azertyuiopqsdfghjklmwxcvbn0123456789"
    for i in range(randint(1,15)):
        c = alpha[randint(0,len(alpha)-1)]
        mot += c
    return mot

def demander(message='', erreur='Entree invalide', plage="azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN0123456789,?;.:/!"):
    valide = False
    while valide is False:
        try:
            entree = input(message)
            if entree == 'exit':
                return 'interruption'
            for lettre in entree:
                if lettre in plage:
                    valide = True
                else:
                    valide = False
                assert valide is True
        except:
            if erreur is not False:
                print(erreur)
    return entree


if __name__ == "__main__":
    for i in range(1):
        mot = gen_mot_rand()
        clef = gen_mot_rand()
        a = chiffrage(mot, clef)
        b = chiffrage(a, clef, 'dechiffrage')
        assert b == mot