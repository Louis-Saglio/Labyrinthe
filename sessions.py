# consulter compte
# chiffrer le mdp
from module import chiffrage

def creer_compte(user_name, password):
    from pickle import Pickler
    data = {
        'password': password,
        'scores' : ['rien']
        }
    with open('saved_game/' + user_name, 'wb') as fichier:
        mon_pickler = Pickler(fichier)
        mon_pickler.dump(data)

def lire_compte(user_name):
    from pickle import Unpickler
    with open('saved_game/' + user_name, 'rb') as fichier:
        depickler = Unpickler(fichier)
        data = depickler.load()
    return data

def enregistrer_score(user, password, newScore):
    from pickle import Pickler
    data = lire_compte(user)
    if password == data['password']:
        data['scores'].append(newScore)
        with open('saved_game/' + user, 'wb') as fichier:
            mon_pickler = Pickler(fichier)
            mon_pickler.dump(data)
    else:
        print('mot de passe incorrect')

if __name__ == "__main__":
    from os import system
    creer_compte('louis', 'erty')
    enregistrer_score('louis', 'erty', 25)
    enregistrer_score('louis', 'erty', 34)
    a = lire_compte('louis')