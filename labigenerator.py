from random import randint


def get_random_stream(mini, maxi):
    stream = [randint(mini, maxi) for i in range(100000)]
    while True:
        for i in stream:
            yield i


STREAM = get_random_stream(0, 2)


def creer_matrice(hauteur=15, largeur=25, remplissage='M'):
    matrice = []
    for i in range(hauteur):
        matrice.append([])
        for c in range(largeur):
            matrice[i].append(remplissage)
    return matrice


def dessiner_bordure(matrice, bordure='B'):
    hauteur = len(matrice)
    largeur = len(matrice[0])
    for h in range(hauteur):
        matrice[h][0] = bordure
        matrice[h][largeur - 1] = bordure
    for l in range(largeur):
        matrice[0][l] = bordure
        matrice[hauteur - 1][l] = bordure
    return matrice


def placer_depart_arrivee(matrice):
    matrice[1][1] = 'X'
    matrice[len(matrice) - 2][len(matrice[0]) - 2] = 'A'
    return matrice


def renvoyer_cases_contact(matrice, h, l, case):
    contacts = [
        matrice[h - 1][l],  # en-haut
        matrice[h + 1][l],  # en-bas
        matrice[h][l - 1],  # à gauche
        matrice[h][l + 1]  # à droite
    ]
    return contacts.count(case)


def determiner_si_devenir_chemin(matrice, h, l, mur, chemin, bordure):
    return next(STREAM) == 0 and renvoyer_cases_contact(matrice, h, l, mur) + renvoyer_cases_contact(matrice, h, l, bordure) == 3 and matrice[h][l] != bordure


def creer_chemin(matrice, mur, chemin, bordure):
    hauteur = len(matrice)
    largeur = len(matrice[0])
    for h in range(hauteur - 1):
        for l in range(largeur - 1):
            if determiner_si_devenir_chemin(matrice, h, l, mur, chemin, bordure) is True:
                matrice[h][l] = chemin
    return matrice


def creer_laby(hauteur=15, largeur=15):
    nbrTours = round(((hauteur * largeur) / 10) * 1.5)
    chemin_fini = False
    while chemin_fini is False:
        mat = creer_matrice(hauteur, largeur)
        mat = dessiner_bordure(mat)
        mat[1][1] = 0
        for i in range(nbrTours):
            mat = creer_chemin(mat, 'M', ' ', 'B')
        mat = placer_depart_arrivee(mat)
        if renvoyer_cases_contact(mat, len(mat) - 2, len(mat[0]) - 2, ' ') > 0:
            chemin_fini = True
        else:
            nbrTours += 20
    return mat


def as_string_tuple(height, width):
    return [''.join(row).replace('B', 'M').replace('A', ' ').replace('X', ' ') for row in creer_laby(height, width)]


if __name__ == '__main__':
    from time import time
    for i in (30, 40, 50, 60, 70, 80, 90, 100):
        deb = time()
        creer_laby(i, i)
        print(time() - deb)