from module import *

def creer_compte(user_name, password):
    from pickle import Pickler
    password = chiffrage(password, password)
    data = {
        'password': password,
        'scores' : []
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
    password = chiffrage(password, password)
    if password == data['password']:
        data['scores'].append(newScore)
        with open('saved_game/' + user, 'wb') as fichier:
            mon_pickler = Pickler(fichier)
            mon_pickler.dump(data)
    else:
        print('mot de passe incorrect')

def verifier_password(user_name, password, demander=False):
    if demander is False:
        data = lire_compte(user_name)
        real_password = data['password']
    else:
        real_password = input("Mot-de-passe ?")
    if chiffrage(password, password) == real_password:
        return True
    else:
        return False

if __name__ == "__main__":
    # test de creer_compte, enregistrer_score, lire_compte, vérifier_password
    from os import remove
    user = gen_mot_rand()
    password = gen_mot_rand()
    creer_compte(user, password)
    enregistrer_score(user, password, 25)
    enregistrer_score(user, password, 34)
    assert verifier_password(user, password) is True
    remove('saved_game/' + user)