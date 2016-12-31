from module import *

def creer_compte(user_name='', password='', verbose=False):
    from pickle import Pickler
    if verbose is True:
        user_name = demander("Choisissez un nom d'utilisateur", plage='AZERTYUIOPQSDFGHJKLMWXCVBN?./,;:azertyuiopqsdfghjklmwxcvbn0123456789')
        password = demander("Choisissez un mot de passe")
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

def verifier_password(user_name, password='', demande=False):
    if demande:
        password = demander("Mot-de-passe ?")
    data = lire_compte(user_name)
    real_password = data['password']
    if chiffrage(password, password) == real_password:
        return True
    else:
        return False

def connexion(mode='verbose', user_name='', password=''):
    if mode == 'verbose':
        user_name = demander("Quel est votre nom d'utilisateur ?")
        password = demander("Mot-de-passe ?")
        if user_name == 'exit':
            return False
    try:
        assert verifier_password(user_name, password) is True
        return {'user_name' : user_name, 'password' : password}
    except:
        if mode == 'verbose':
            print("Nom d'utilisateur ou mot de passe invalide")
        return False

def voir_scores(mode='verbose', user='', password=''):
    identifiants = False
    while identifiants is False:
        identifiants = connexion(mode, user, password)
    userName = identifiants['user_name']
    data = lire_compte(userName)
    scores = data['scores']
    moyenne = round(moyenne_iter(scores), 2)
    strScores = ''
    for score in scores:
        strScores += (str(score) + '; ')
    print("Voici les scores de", userName, '\n', strScores)
    print("Ce qui fait une moyenne de", moyenne)

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

def ajouter_meilleurs_scores(user, score, fichier='meilleurs_scores'):
    from pickle import Pickler
    try:
        data = lire_compte(fichier)
    except:
        data = creer_meilleurs_scores(fichier)
    lstScores = data['scores']
    lstUsers = data['user_name']
    if len(lstUsers) >= 5:
        mini = min(lstScores)
        i = lstScores.index(mini)
        lstScores[i] = score
        lstUsers[i] = user
    else:
        lstScores.append(score)
        lstUsers.append(user)
    data = {
        'user_name': lstUsers,
        'scores' : lstScores
        }
    with open('saved_game/' + fichier, 'wb') as fichier:
            mon_pickler = Pickler(fichier)
            mon_pickler.dump(data)

def afficher_meilleurs_scores(fichier='meilleurs_scores', retourner=False):
    data = lire_compte(fichier)
    if retourner is False:
        for i in range(len(data['scores'])):
            print(data['user_name'][i], ' : ', data['scores'][i])
    else:
        return data
    input()

def determiner_si_meilleur_score(score, fichier='meilleurs_scores'):
    try:
        data = afficher_meilleurs_scores(fichier, True)
        if score > min(data['scores']):
            return True
        else:
            return False
    except:
        return True

if __name__ == "__main__":    
    # test de creer_compte, enregistrer_score, lire_compte, vérifier_password
    from os import remove
    from random import randint
    user = gen_mot_rand()
    password = gen_mot_rand()
    creer_compte(user, password)
    enregistrer_score(user, password, randint(0,15))
    enregistrer_score(user, password, randint(0,15))
    assert verifier_password(user, password) is True
    connexion('autre', user, password)
    connexion('autre', gen_mot_rand(), gen_mot_rand())
    ajouter_meilleurs_scores(user, randint(0,15), 'meilleurs_scores_test')
    ajouter_meilleurs_scores(user, randint(0,15), 'meilleurs_scores_test')
    ajouter_meilleurs_scores(user, randint(0,15), 'meilleurs_scores_test')
    afficher_meilleurs_scores('meilleurs_scores_test', True)
    determiner_si_meilleur_score(randint(0,15), 'meilleurs_scores_test')
    voir_scores('autre', user, password)
    remove('saved_game/' + user)
    remove('saved_game/meilleurs_scores_test')
    effacer_ecran()