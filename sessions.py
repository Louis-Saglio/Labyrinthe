# Créer un compte
# enregistrer scores
# consulter compte

def creer_compte():
    from pickle import Pickler
    from os import getcwd, chdir
    chdir('saved_game')
    user_name = input("Entrez un nom d'utilisateur")
    password = input("Choisissez un mot-de-passe")
    with open(user_name, 'w') as fichier:
        mon_pickler = Pickler(fichier)
        mon_pickler.dump('password : ' + password + '/n')