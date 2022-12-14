# -- Exercice 1 --
# from tkinter import *
# fen1 = Tk()
# tex1 = Label(fen1, text='Bonjour tout le monde !', fg='red')
# tex1.pack()
# bou1 = Button(fen1, text='Quitter', command = fen1.destroy)
# bou1.pack()
# fen1.mainloop()




# -- EXERCICE 3 --
# # Petit exercice utilisant la bibliothèque graphique tkinter
# from tkinter import *
# from random import randrange
# # --- définition des fonctions gestionnaires d'événements : ---
# def drawline():
#     "Tracé d'une ligne dans le canevas can1"
#     global x1, y1, x2, y2, coul
#     can1.create_line(x1,y1,x2,y2,width=2,fill=coul)
#     # modification des coordonnées pour la ligne suivante :
#     y2, y1 = y2+10, y1-10
# def changecolor():
#     "Changement aléatoire de la couleur du tracé"
#     global coul
#     pal=['purple','cyan','maroon','green','red','blue','orange','yellow']
#     c = randrange(8) # => génère un nombre aléatoire de 0 à 7
#     coul = pal[c]
# def changecolorCMG():   # exercice 4.1
#     "Changement aléatoire de la couleur du tracé"
#     global coul
#     pal=['cyan','maroon','green']
#     c = randrange(3) # => génère un nombre aléatoire de 0 à 3
#     coul = pal[c]
# def drawlineHP():       # Exercice 4.2
#     "Tracé d'une ligne dans le canevas can1"
#     global x1, y1, x2, y2, coul
#     can1.create_line(x1,y1,x2,y2,width=2,fill=coul)
#     # modification des coordonnées pour la ligne suivante :
#     y2, y1 = y2+10, y1+10;
# def drawline2():
#     "Tracé d'une croix rouge ==> viseur"
#     global x1, y1, x2, y2, x3, y3, x4, y4
#     can1.create_line(x1,y1,x2,y2,width=2,fill='red')
#     can1.create_line(x3, y3, x4, y4, width=2, fill='red')


# #------ Programme principal -------
# # les variables suivantes seront utilisées de manière globale :
# #x1, y1, x2, y2 = 10, 190, 190, 10 # coordonnées de la ligne
# #x1, y1, x2, y2 = -100, 10, 300, 10 # coordonnées de la ligne pour l'ex 4.2
# #x1, y1, x2, y2 = -100, 10, 750, 10 # coordonnées de la ligne pour l'ex 4.3
# x1, y1, x2, y2, x3, y3, x4, y4 = -100, 325, 600, 325, 250, -100, 250, 750 # coordonnées de la ligne pour l'ex 4.4

# coul = 'dark green' # couleur de la ligne
# # Création du widget principal ("maître") :
# fen1 = Tk()
# # création des widgets "esclaves" :
# # can1 = Canvas(fen1,bg='dark grey',height=200,width=200)   #Exercice 4.3
# # can1.pack(side=LEFT)
# can1 = Canvas(fen1,bg='dark grey',height=650,width=500)     #Exercice 4.4
# can1.pack(side=LEFT)                                         
# bou1 = Button(fen1,text='Quitter',command=fen1.quit)
# bou1.pack(side=BOTTOM)
# bou2 = Button(fen1,text='Tracer une ligne',command=drawlineHP)
# bou2.pack()
# bou3 = Button(fen1,text='Autre couleur',command=changecolorCMG)
# bou3.pack()
# bou4 = Button(fen1,text='Viseur',command=drawline2)
# bou4.pack()
# fen1.mainloop() # démarrage du réceptionnaire d'événements
# fen1.destroy() # destruction (fermeture) de la fenêtre


# -- Exercice 4 --

from tkinter import *
from random import randrange
# définition des gestionnaires
# d'événements :
def move():
    "deplacement de la balle"
    global x1, y1, dx, dy, flag
    x1, y1 = x1 +dx, y1 + dy
    if x1 >210:
        x1, dx, dy = 210, 0, 15
    if y1 >210:
        y1, dx, dy = 210, -15, 0
    if x1 <10:
        x1, dx, dy = 10, 0, -15
    if y1 <10:
        y1, dx, dy = 10, 15, 0
    can1.coords(oval1,x1,y1,x1+30,y1+30)
    if flag >0:
        fen1.after(50,move) # => boucler, après 50 millisecondes
def move_Billard():
    "deplacement de la balle"
    global x1, y1, dx, dy, flag
    x1, y1 = x1 +dx, y1 + dy
    if x1 >210:
        x1, dx, dy = 210, 15, 0
    #if y1 >210:
    #    y1, dx, dy = 210, -15, 0
    if x1 <10:
        x1, dx, dy = 10, 15, 0
    #if y1 <10:
    #    y1, dx, dy = 10, 15, 0
    #can1.coords(oval1,x1,y1,x1+30,y1+30)
    if flag >0:
        fen1.after(50,move_Billard) # => boucler, après 50 millisecondes

def stop_it():
    "arret de l'animation"
    global flag
    flag =0
def start_it():
    "demarrage de l'animation"
    global flag
    if flag ==0: # pour ne lancer qu'une seule boucle
        flag =1
        move_Billard()
#========== Programme principal =============
# les variables suivantes seront utilisées de manière globale :
x1, y1 = 10, 10 # coordonnées initiales
dx, dy = 15, 0 # 'pas' du déplacement
flag =0 # commutateur
# Création du widget principal ("parent") :
fen1 = Tk()
fen1.title("Exercice d'animation avec tkinter")
# création des widgets "enfants" :
can1 = Canvas(fen1,bg='dark grey',height=250, width=250)
can1.pack(side=LEFT, padx =5, pady =5)
oval1 = can1.create_oval(x1, y1, x1+30, y1+30, width=2, fill='red')
bou1 = Button(fen1,text='Quitter', width =8, command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1, text='Demarrer', width =8, command=start_it)
bou2.pack()
bou3 = Button(fen1, text='Arreter', width =8, command=stop_it)
bou3.pack()
# démarrage du réceptionnaire d'événements (boucle principale) :
fen1.mainloop()
