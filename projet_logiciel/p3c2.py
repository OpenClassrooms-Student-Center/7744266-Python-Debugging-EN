# -*- coding: utf8 -*-

from random import randint 

class RockPaperScissors :
    def __init__(self, new_player_score, new_ai_score, player_label, ai_label):
        self.player_score = 0
        self.artificial_intelligence_score = 0
        self.new_player_score = new_player_score
        self.new_ai_score = new_ai_score
        self.player_label = player_label
        self.ai_label = ai_label

    def update_scores(self, ai_choice, player_choice):
        if ai_choice == 1 and player_choice == 2:
            self.player_score += 1
        elif ai_choice == 2 and player_choice == 1:
            self.artificial_intelligence_score += 1
        elif ai_choice == 1 and player_choice == 3:
            self.artificial_intelligence_score += 1
        elif ai_choice == 3 and player_choice == 1:
            self.player_score += 1
        elif ai_choice == 3 and player_choice == 2:
            self.artificial_intelligence_score += 1
        elif ai_choice == 2 and player_choice == 3:
            self.player_score += 1

    def play(self, player_choice):
        ai_choice = randint(1,3)
        if ai_choice==1:
            self.ai_label.configure(image=rock)
        elif ai_choice==2:
            self.ai_label.configure(image=paper)
        else:
            self.ai_label.configure(image=scissors)
        self.update_scores(ai_choice,player_choice)
        self.new_player_score.configure(text=str(self.player_score))
        self.new_ai_score.configure(text=str(self.artificial_intelligence_score))
    
    def play_rock(self):
        self.play(1)
        self.player_label.configure(image=rock)

    def play_paper(self):
        self.play(2)
        self.player_label.configure(image=paper)

    def play_scissors(self):
        self.play(3)
        self.player_label.configure(image=scissors)

    def play_again(self):
        self.player_score = 0
        self.artificial_intelligence_score = 0
        self.new_player_score.configure(text=str(self.player_score))
        self.new_ai_score.configure(text=str(self.artificial_intelligence_score))
        self.player_label.configure(image=zero)
        self.ai_label.configure(image=zero)

from tkinter import PhotoImage, TclError, Tk, Label, Button, W, E

window = Tk()
window.title("Rock Paper Scissors")

try:
    versus = PhotoImage(file ='vs.gif')
    rock = PhotoImage(file ='rock.gif')
    paper = PhotoImage(file ='paper.gif')
    scissors = PhotoImage(file ='scissors.gif')
except RuntimeError:
    print("Tu as utilisé la fonction PhotoImage trop tôt. Fait le après Tk()")

try:
    zero = PhotoImage(file ='zero.gif')
except TclError:
    print("Il semble que le type d'image jpg n'est pas supporté par PhotoImage")

try:
    texte1 = Label(fenetre, text="Vous", font=("Arial", "20", "bold"))
    texte1.grid(row=0,column=0)

    texte2 = Label(fenetre, text="Intelligence artificielle", font=("Arial", 20, "bold"))
    texte2.grid(row=0,column=2)

    texte3 = Label(fenetre, text="Pour jouer, cliquez sur une des icônes ci-dessous.",font=("Arial", 20, "bold"))
    texte3.grid(row=3, columnspan =3, pady =5)

    nouveau_score_joueur = Label(fenetre, text="0", font=("Arial", 20, "bold"))
    nouveau_score_joueur.grid(row=1, column=0)

    nouveau_score_ia = Label(fenetre, text="0", font=("Arial", 20, "bold"))
    nouveau_score_ia.grid(row=1, column=2)

    label_joueur = Label(fenetre, image=zero)
    label_joueur.grid(row =2, column =0)

    label_vs = Label(fenetre, image=versus)
    label_vs.grid(row =2, column =1)

    label_ia = Label(fenetre, image=zero)
    label_ia.grid(row =2, column =2)
except NameError:
    print("Il semble que la fonction Label() n'a pas été importée.")

try:
    jeu = PierreFeuilleCiseaux(nouveau_score_joueur, nouveau_score_ia, label_joueur, label_ia)
except NameError:
    print("La variable 'nouveau_score_joueur' n'est pas encore définie.")

try:
    bouton_pierre = Button(fenetre,command=jeu.jouer_pierre)
    bouton_pierre.configure(image=pierre)
    bouton_pierre.grid(row =4, column =0)

    bouton_feuille = Button(fenetre,command=jeu.jouer_feuille)
    bouton_feuille.configure(image=feuille)
    bouton_feuille.grid(row =4, column =1,)

    bouton_ciseaux = Button(fenetre,command=jeu.jouer_ciseaux)
    bouton_ciseaux.configure(image=ciseaux)
    bouton_ciseaux.grid(row =4, column =2)

    bouton_recommence = Button(fenetre,text='Rejouer',command=jeu.rejouer,font=("Courier", 20, "bold"))
    bouton_recommence.grid(row =5, column =0, pady =10, sticky=E)

    bouton_quitter = Button(fenetre,text='Quitter',command=quit,font=("Courier", 20, "bold"))
    bouton_quitter.grid(row =5, column =2, pady =10, sticky=W)
except NameError:
    print("Il manque des variables")
    
fenetre.mainloop()
