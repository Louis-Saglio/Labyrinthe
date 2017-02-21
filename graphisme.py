# Ce module est encore en cours d'implémentation

from tkinter import *
from labigenerator import *
from module import *

matrice = creer_laby()
matrice = retourner_laby_str(matrice)

fenetre = Tk()
laby = Label(fenetre, text=matrice, justify=LEFT)
laby.pack()
fenetre.mainloop()
