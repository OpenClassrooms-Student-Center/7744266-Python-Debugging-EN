# -*- coding: utf8 -*-

from random import randint 
import datetime

print("Welcome to the game Rock Paper Scissors")

name = "debugger"
current_year = datetime.datetime.now().strftime("%Y")
year_of_birth = 2000

print(f"Hello {name}, the year is {current_year}, so you are {int(current_year) - year_of_birth}.")

class RockPaperScissors :
    """
    A class for playing the game Rock Paper Scissors, updating the score
    depending on the user's choices, and playing again. 
    """
    def _init_(self, new_player_score, new_ai_score, player_label, ai_label):
        """
        Constructor of the class which initializes the variables
        """
        self.player_score = 0
        self.artificial_intelligence_score = 0
        self.new_player_score = new_player_score
        self.new_ai_score = new_ai_score
        self.player_label = player_label
        self.ai_label = ai_label

    def update_scores(self, ai_choice, player_choice):
        """
        Method which updates the score depending on the choices made
        """
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
        """
        Method which updates the label depending on the choices made
        """
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
    
    def play_rock():
        """
        Method for changing the image if rock is chosen
        """
        self.play(1)
        self.player_label.configure(image=rock)

    def play_paper(self):
        """
        Method for changing the image if paper is chosen
        """
        self.play(2)
        self.player_label.configure(image=paper)

    def play_scissors(self):
        """
        Method for changing the image if scissors are chosen
        """
        self.play(3)
        self.player_label.configure(image=scissors)

    def play_again(self):
        """
        Method which restarts the game when the button is pressed
        """
        self.player_score = 0
        self.artificial_intelligence_score = 0
        self.new_player_score.configure(text=str(self.player_score))
        self.new_ai_score.configure(text=str(self.artificial_intelligence_score))
        self.player_label.configure(image=zero)
        self.ai_label.configure(image=zero)

from tkinter import PhotoImage, Tk

versus = PhotoImage(file ='vs.gif')
rock = PhotoImage(file ='rock.gif')
paper = PhotoImage(file ='paper.gif')
scissors = PhotoImage(file ='scissors.gif')

window = Tk()
window.title("Rock Paper Scissors")

text1 = Label(window, text="You", font=("Arial", "20", "bold"))
text1.grid(row=0,column=0)

text2 = Label(window, text="Artificial intelligence", font=("Arial", 20, "bold"))
text2.grid(row=0,column=2)

text3 = Label(window, text="To play, click on one of the icons below.",font=("Arial", 20, "bold"))
text3.grid(row=3, columnspan =3, pady =5)

new_player_score = Label(window, text="0", font=("Arial", 20, "bold"))
new_player_score.grid(row=1, column=0)

new_ai_score = Label(window, text="0", font=("Arial", 20, "bold"))
new_ai_score.grid(row=1, column=2)

player_label = Label(window, image=zero)
player_label.grid(row =2, column =0)

vs_label = Label(window, image=versus)
vs_label.grid(row =2, column =1)

ai_label = Label(window, image=zero)
ai_label.grid(row =2, column =2)

zero = PhotoImage(file ='zero.jpg')

game = RockPaperScissors(new_player_score, new_ai_score, player_label, ai_label)

rock_button = Button(window,command=game.play_rock).configure(image=rock).grid(row =4, column =0)

paper_button = Button(window,command=game.play_paper)
paper_button.configure(image=paper)
paper_button.grid(row =4, column =1,)

scissors_button = Button(window,command=game.play_scissors)
scissors_button.configure(image=scissors)
scissors_button.grid(row =4, column =2)

play_again_button = Button(window,text='Play again',command=game.play_again,font=("Courier", 20, "bold"))
play_again_button.grid(row =5, column =0, pady =10, sticky=E)

quit_button = Button(window,text='Quit',command=quit,font=("Courier", 20, "bold"))
quit_button.grid(row =5, column =2, pady =10, sticky=W)

window.mainloop()
