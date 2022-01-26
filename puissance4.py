from tkinter import *
from tkinter import messagebox
# création d'une fenetre

windows=Tk()

#Declaration des variables
lx=[361,361,361,361,361,361,361]
ly=[421,421,421,421,421,421,421]
nbrclick=[0,0,0,0,0,0,0]
grille=[
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0]
]

ActivePlayer=1
image = PhotoImage(file="table1.png")
# paramétre de la fenetre :
titre=Frame(windows, bg='#4065A4')
#ajoute un titre dans la fenetre
windows.title("Le jeux puissance 4 ")
windows.geometry("700x700")
windows.maxsize(700, 700)
windows.minsize(700, 700)
windows.iconbitmap("icon.ico")
windows.config(background='#4065A4')

#creation de canavas
des = Canvas(windows, width=500, height=425,bg='#4065A4',bd=0,highlightthickness=0)


b=Frame(windows, bg='#4065A4')
Noms=Frame(b, bg='#4065A4')
# inserer le titre
titre1= Label(b, text="Puissance 4\n", font=("Goudy Stout",30,'underline'), bg='#4065A4', fg='#cbcdc8',bd=0)
titre1.grid(row=0, column=0, padx=150, pady=50,ipadx=0,ipady=0)
#inserer les noms des joueurs
#joueur 1
label1=Label(Noms,text="Le nom de joueur 1 :",font=("courrier",20), bg='#4065A4', fg='white',bd=0)
label1.grid(row=2, column=1, padx=0, pady=15, ipadx=0, ipady=0)
nom1=Entry(Noms,width=25,font=("courrier",15))
nom1.grid(row=2, column=2, padx=0, pady=0, ipadx=0, ipady=0)
#joueur 2
label2=Label(Noms,text="Le nom de joueur 2 :",font=("courrier",20), bg='#4065A4', fg='white',bd=5)
label2.grid(row=4, column=1, padx=10, pady=15, ipadx=0, ipady=0)
nom2=Entry(Noms,width=25,font=("courrier",15))
nom2.grid(row=4, column=2, padx=10, pady=0, ipadx=0, ipady=0)
Noms.grid()
#inserer la bouton JOUER
play=Button(b,text="JOUER",height=2, width=30, bg='white', fg='#4065A4', font=("arial", 18), command=lambda:puissance4())
play.grid(row=2, column=0, padx=0, pady=25, ipadx=0, ipady=0,sticky='s')
b.grid(column=2,row=10,padx=0, pady=70, ipadx=0, ipady=0)

#defenir la fonction principale de jeu pour l'appeller dans le bouton JOUER
def puissance4():
    global image,play,titre1,nom1,nom2
    joueur1 = nom1.get()
    joueur2 = nom2.get()
    #supprimer le continue de page principale
    play.destroy()
    b.destroy()
    #insertion le titre de jeu avec le noms de joueur qui jouer
    titre1 = Label(windows, text="Puissance 4 \n Nom de joueur: " + joueur1, font=("courrier", 30), bg='#4065A4',fg='white', bd=5)
    titre1.grid(row=0, column=0, padx=0, pady=12, ipadx=0, ipady=0)

    #insertion de l'image tableau

    des.create_image(250, 215, image=image)
    des.grid(row=4, column=0, padx=100, pady=0,ipadx=0,ipady=0)
    #creation des boutons
    fra = Frame(windows, bg='#4065A4')

    b0 = Button(fra, text="0", height=1, width=3, bg='white', fg='#4065A4', font=("arial", 15), command=lambda :Fctbouton(0))
    b0.grid(row=3, column=0, padx=14, pady=0, ipadx=0, ipady=0, )
    b1 = Button(fra, text="1", height=1, width=3, bg='white', fg='#4065A4', font=("arial", 15), command=lambda :Fctbouton(1))
    b1.grid(row=3, column=1, padx=14, pady=0)
    b2 = Button(fra, text="2", height=1, width=3, bg='white', fg='#4065A4', font=("arial", 15), command=lambda :Fctbouton(2))
    b2.grid(row=3, column=2, padx=14, pady=0)
    b3 = Button(fra, text="3", height=1, width=3, bg='white', fg='#4065A4', font=("arial", 15), command=lambda :Fctbouton(3))
    b3.grid(row=3, column=3, padx=14, pady=0)
    b4 = Button(fra, text="4", height=1, width=3, bg='white', fg='#4065A4', font=("arial", 15), command=lambda :Fctbouton(4))
    b4.grid(row=3, column=4, padx=14, pady=0)
    b5 = Button(fra, text="5", height=1, width=3, bg='white', fg='#4065A4', font=("arial", 15), command=lambda :Fctbouton(5))
    b5.grid(row=3, column=5, padx=14, pady=0)
    b6 = Button(fra, text="6", height=1, width=3, bg='white', fg='#4065A4', font=("arial", 15), command=lambda :Fctbouton(6))
    b6.grid(row=3, column=6, padx=14, pady=0)
    fra.grid(row=3, column=0, padx=100, pady=12, ipadx=0, ipady=0)
    #fonction des boutons
    def Fctbouton(id):
        global ActivePlayer
        global liste,titre1

        if (ActivePlayer==1):
            #supprission de titre
            titre1.destroy()
            #insertion le titre de nouveau avec le noms de joueur qui jouer
            titre1 = Label(windows, text="Puissance 4 \n Nom de joueur: " + joueur2, font=("courrier", 30), bg='#4065A4', fg='white', bd=5)
            titre1.grid(row=0, column=0, padx=0, pady=12, ipadx=0, ipady=0)
            Creercercle(id,'black')
            cmp=determiner_ligne(id)
            grille[cmp][id]=1
            # Affichage de matrice
            for i in range(6):
                print(grille[i])
            print('\n')
            #changer le joueur
            ActivePlayer=2
        elif (ActivePlayer==2):
            titre1.destroy()
            titre1 = Label(windows, text="Puissance 4 \n Nom de joueur: " + joueur1, font=("courrier", 30), bg='#4065A4', fg='white', bd=5)
            titre1.grid(row=0, column=0, padx=0, pady=12, ipadx=0, ipady=0)
            Creercercle(id,'red')
            cmp=determiner_ligne(id)
            grille[cmp][id] = 2
            #Affichage de matrice
            for i in range(6):
             print(grille[i])
            print('\n')
            # changer le joueur
            ActivePlayer=1
        #appel de la fonction gagnant
        gagnant()

    #creation et positionner le jeton noire et rouge
    def Creercercle(id,couleur):
        global lx,ly,nbrclick,ActivePlayer
        if id==0:
            des.create_oval(6, lx[0], 66, ly[0], fill=couleur, width=0)
            lx[0] = lx[0] - 71
            ly[0] = ly[0] -71
            des.grid()
            nbrclick[0] += 1
            if nbrclick[0]==6:
                b0['state'] = DISABLED

        elif id==1:
            des.create_oval(77, lx[1], 137, ly[1], fill=couleur, width=0)
            lx[1]=lx[1]-71
            ly[1]=ly[1]-71
            des.grid()
            nbrclick[1] += 1
            if nbrclick[1] == 6:
                b1['state'] = DISABLED
        elif id==2:
            des.create_oval(148,lx[2],208,ly[2],fill=couleur,width=0)
            lx[2]=lx[2]-71
            ly[2]=ly[2]-71
            des.grid()
            nbrclick[2] += 1
            if nbrclick[2] == 6:
                b2['state'] = DISABLED
        elif id==3:
            des.create_oval(219,lx[3],279,ly[3],fill=couleur,width=0)
            lx[3]=lx[3]-71
            ly[3]=ly[3]-71
            des.grid()
            nbrclick[3] += 1
            if nbrclick[3] == 6:
                b3['state'] = DISABLED
        elif id==4:
            des.create_oval(290, lx[4], 350,ly[4], fill=couleur, width=0)
            lx[4]=lx[4]-71
            ly[4]=ly[4]-71
            des.grid()
            nbrclick[4] += 1
            if nbrclick[4] == 6:
                b4['state'] = DISABLED
        elif id==5:
            des.create_oval(361, lx[5], 421, ly[5], fill=couleur, width=0)
            lx[5]=lx[5]-71
            ly[5]=ly[5]-71
            des.grid()
            nbrclick[5] += 1
            if nbrclick[5] == 6:
                b5['state'] = DISABLED
        elif id==6:
            des.create_oval(432, lx[6], 492, ly[6], fill=couleur, width=0)
            lx[6]=lx[6]-71
            ly[6]=ly[6]-71
            des.grid()
            nbrclick[6] += 1
            if nbrclick[6] == 6:
                b6['state'] = DISABLED

    #definition de joueur a gagner
    def gagnant():
        if ((win_vertical() == 1) or (win_horizontal() == 1) or (win_diagonale() == 1)):
            messagebox.showinfo(title='Resultat', message=joueur1 + ' est le gagnant ')
        elif ((win_vertical() == 2) or (win_horizontal() == 2) or (win_diagonale() == 2)):
            messagebox.showinfo(title='Resultat', message=joueur2 + ' est le gagnant ')
        elif b0['state'] == DISABLED and b1['state'] == DISABLED and b2['state'] == DISABLED and b3['state'] == DISABLED and \
                b4['state'] == DISABLED and b5['state'] == DISABLED and b6['state'] == DISABLED:
            messagebox.showinfo(title='Resultat', message='NULL')


    # creation de menu
    def nov():
        global lx, ly, ActivePlayer, image, grille, nbrclick
        des.delete(ALL)
        des.create_image(250, 215, image=image)
        des.grid(row=4, column=0, padx=100, pady=0, ipadx=0, ipady=0)
        ActivePlayer = 1
        nbrclick = [0, 0, 0, 0, 0, 0, 0]
        if nbrclick[0] == 0 and nbrclick[1] == 0 and nbrclick[2] == 0 and nbrclick[3] == 0 and nbrclick[4] == 0 and \
                nbrclick[5] == 0 and nbrclick[6] == 0:
            b0['state'] = NORMAL
            b1['state'] = NORMAL
            b2['state'] = NORMAL
            b3['state'] = NORMAL
            b4['state'] = NORMAL
            b5['state'] = NORMAL
            b6['state'] = NORMAL
        lx = [361, 361, 361, 361, 361, 361, 361]
        ly = [421, 421, 421, 421, 421, 421, 421]
        grille = [[0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  ]


    menu = Menu(windows)
    f_m = Menu(menu, tearoff=0)
    f_m.add_command(label="Nouveau", command=nov)
    f_m.add_command(label="Quitter", command=windows.quit)

    menu.add_cascade(label="Fichier", menu=f_m)
    # ajoute de menu au fenetre
    windows.config(menu=menu)
#determiner le ligne qui n'a pas un jeton selon le bouton
def determiner_ligne(id):
    global grille
    for i in range(5,-1,-1):
        if grille[i][id] == 0:
            return (i)

#pour determiner le gagnant en horizontal , verticale et diagonale

def win_horizontal():
    for i in range(6):
        for j in range(4):
            if ((grille[i][j]==1) and (grille[i][j+1]==1) and (grille[i][j+2]==1) and (grille[i][j+3]==1)):
                return 1
            if ((grille[i][j]==2) and (grille[i][j+1]==2) and (grille[i][j+2]==2) and (grille[i][j+3]==2)):
                return 2

def win_vertical():
    for j in range(7):
        for i in range(3):
            if (grille[i][j]==1 and grille[i+1][j]==1 and grille[i+2][j]==1 and grille[i+3][j]==1):
                return 1
            if (grille[i][j]==2 and grille[i+1][j]==2 and grille[i+2][j]==2 and grille[i+3][j]==2):
                return 2
def win_diagonale():
    for i in range(3):
        for j in range(4):
            if ((grille[i][j]==1) and (grille[i+1][j+1]==1 )and (grille[i+2][j+2]==1) and (grille[i+3][j+3]==1)):
                return 1
            if ((grille[i][j]==2) and (grille[i+1][j+1]==2) and (grille[i+2][j+2]==2) and (grille[i+3][j+3]==2)):
                return 2
    for i in range(3,6):
        for j in range(4):
            if ((grille[i][j] == 1) and (grille[i - 1][j + 1] == 1) and (grille[i - 2][j + 2] == 1) and (grille[i - 3][j + 3] == 1)):
                return 1
            if ((grille[i][j] == 2 )and (grille[i -1][j + 1] == 2) and (grille[i - 2][j + 2] == 2) and (grille[i - 3][j + 3] == 2)):
                return 2



windows.mainloop()