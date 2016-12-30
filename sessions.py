from module import *

def creer_compte(user_name='', password='', verbose=False):
    from pickle import Pickler
    if verbose is True:
        user_name = input("Choisissez un nom d'utilisateur")
        password = input("Choisissez un mot de passe")
    password_clair = password
    password = chiffrage(password, password)
    data = {
        'password': password,
        'scores' : []
        }
    with open('saved_game/' + user_name, 'wb') as fichier:
        mon_pickler = Pickler(fichier)
        mon_pickler.dump(data)
    return {'user_name' : user_name, 'password' : password_clair}

def lire_compte(user_name):
    from pickle import Unpickler
    with open('saved_game/' + user_name, 'rb') as fichier:
        depickler = Unpickler(fichier)
        data = depickler.load()
    return data

def enregistrer_score(user, password='', newScore=0):
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
        return {'user_name' : user_name, 'password' : password}
    except:
        if mode == 'verbose':
            print("Nom d'utilisateur ou mot de passe invalide")
        return False

def creer_meilleurs_scores(fichier='meilleurs_scores'):
    from pickle import Pickler
    data = {
        'user_name': [],
        'scores' : []
        }
    with open('saved_game/' + fichier, 'wb') as fichier:
        mon_pickler = Pickler(fichier)
        mon_pickler.dump(data)
    return data

def ajouter_meilleurs_scores(user, score):
    from pickle import Pickler
    data = lire_compte('meilleurs_scores')
    lstScores = data['scores']
    print(lstScores)
    lstUsers = data['user_name']
    print(lstUsers)
    lstScores.append(score)
    print(lstScores)
    lstUsers.append(user)
    print(lstUsers)
    data = {
        'user_name': [lstUsers],
        'scores' : [lstScores]
        }
    print(data)
    with open('saved_game/meilleurs_scores', 'wb') as fichier:
            mon_pickler = Pickler(fichier)
            mon_pickler.dump(data)

def afficher_meilleurs_scores(fichier='meilleurs_scores'):
    data = lire_compte(fichier)
    for i in range(len(data['scores'])):
        print(data['user_name'][i], ' : ', data['scores'][i])

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
    creer_meilleurs_scores()
    ajouter_meilleurs_scores(user, 15)
    ajouter_meilleurs_scores(user, 15)
    ajouter_meilleurs_scores(user, 15)
    afficher_meilleurs_scores()