# Créer un compte
# enregistrer scores
# consulter compte
# chiffrer le mdp

def creer_compte():
    from pickle import Pickler
    from os import getcwd, chdir
    chdir('saved_game')
    user_name = input("Entrez un nom d'utilisateur")
    password = input("Choisissez un mot-de-passe")
    data = {
        'password': password,
        'scores' : ['rien']
        }
    with open(user_name, 'wb') as fichier:
        mon_pickler = Pickler(fichier)
        mon_pickler.dump(password)
    chdir('..')

def lire_compte(user_name, password):
    from pickle import Unpickler
    from os import chdir
    chdir('saved_game')
    with open(user_name, 'rb') as fichier:
        depickler = Unpickler(fichier)
        data = depickler.load()
        print(data)
    chdir('..')
    return data

def test_sessions():
    creer_compte()
    a = lire_compte('louis', 'erty')
    print(a)

test_sessions()