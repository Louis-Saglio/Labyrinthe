def compter_case(hauteur=15, largeur=15):
    from labigenerator import creer_laby
    laby = creer_laby(hauteur, largeur)
    data = {}
    hauteur = len(laby)
    largeur = len(laby[0])
    for h in range(hauteur):
        for l in range(largeur):
            try:
                data[laby[h][l]] += 1
            except:
                data[laby[h][l]] = 1
    return data


def generer_data(nbr_tours=100, random=True, hauteur=15, largeur=15):
    from module import additionner_dico, tirer_nbr_random
    total_data = {}
    for i in range(nbr_tours):
        print("##########", i)
        if random:
            random = tirer_nbr_random(2, mini=4, maxi=45)
            hauteur = random[0]
            largeur = random[1]
        data = compter_case(hauteur, largeur)
        total_data = additionner_dico(data, total_data)
    total_data["nbr_tours"] = nbr_tours
    return total_data


def extraire_inte_data(data):
    from module import pourcenter
    nbr_mur = data["M"] / data["nbr_tours"]
    nbr_chemin = data[" "] / data["nbr_tours"]
    return pourcenter({"avg_mur": nbr_mur, "avg_chemin": nbr_chemin})


def analyser_generation_toute_taille():
    rep = {}
    for taille in range(4, 45):
        print("\ntaille :", taille, "\n")
        rep[taille] = extraire_inte_data(generer_data(50, False, taille, taille))
        afficher_dictionnaire(rep)
    return rep


if __name__ == "__main__":
    from module import afficher_dictionnaire
    afficher_dictionnaire(analyser_generation_toute_taille())
