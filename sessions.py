from module import *

def creer_compte(user_name='', password='', verbose=False):
    from pickle import Pickler
    if verbose is True:
        user_name = input("Choisissez un nom d'utilisateur")
        password = input("Choisissez un mot de passe")
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

def verifier_password(user_name, password='', demander=False):
    if demander:
        password = input("Mot-de-passe ?")
    data = lire_compte(user_name)
    real_password = data['password']
    if chiffrage(password, password) == real_password:
        return True
    else:
        return False

def connexion(mode='verbose', user_name='', password=''):
    if mode == 'verbose':
        user_name = input("Quel est votre nom d'utilisateur ?")
        password = input("Mot-de-passe ?")
    try:
        assert verifier_password(user_name, password) is True
        return user_name
    except:
        if mode == 'verbose':
            print("Nom d'utilisateur ou mot de passe invalide")
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
    connexion('autre', user, password)
    connexion('autre', gen_mot_rand(), gen_mot_rand())
    remove('saved_game/' + user)