def compter_case(hauteur=15, largeur=15):
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


def generer_data(nbr_tours=100):
    from module import additionner_dico, tirer_nbr_random
    total_data = {}
    for i in range(nbr_tours):
        print("##########", i)
        random = tirer_nbr_random(2, mini=4, maxi=45)
        data = compter_case(random[0], random[1])
        total_data = additionner_dico(data, total_data)
    total_data["nbr_tours"] = nbr_tours
    return total_data


def pourcenter(dico):
    rep = {}
    total = 0
    for item in dico:
        total += dico[item]
    for item in dico:
        rep[item] = round(((100 * dico[item]) / total), 1)
    return rep


def extraire_inte_data(data):
    nbr_mur = data["M"] / data["nbr_tours"]
    nbr_chemin = data[" "] / data["nbr_tours"]
    nbr_bord = data["B"] / data["nbr_tours"]
    return {"avg_mur": nbr_mur, "avg_chemin": nbr_chemin, "avg_bord": nbr_bord}


if __name__ == "__main__":
    from labigenerator import *
    print(pourcenter(extraire_inte_data(generer_data())))
