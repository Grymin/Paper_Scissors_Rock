from tkinter import Tk, Label, Button
from random import choice

PTS_PLAYER = 0
PTS_CPU = 0

def winner(player1, player2):
    beats = {"paper": "rock", "rock": "scissors", "scissors": "paper"}
    if player1 == player2:
        return None
    elif beats[player1] == player2:
        return True
    else:
        return False


def game(player_choice):
    global PTS_PLAYER, PTS_CPU
    global text_label

    cpu_choice = choice(possible_choices)
    wins = winner(player_choice, cpu_choice)

    if wins:
        PTS_PLAYER += 1
        color = 'green'
    elif wins is False:
        PTS_CPU += 1
        color = 'red'
    else:
        color = 'black'

    score_color = "green" if PTS_PLAYER > PTS_CPU else "black" if PTS_PLAYER == PTS_CPU else "red"

    text = "You win" if wins else "You loose" if wins is False else "Draw"
    text += f"\nYOU chose {player_choice}\nCPU chose {cpu_choice}\n"
    text_label.config(text=text, fg=color)
    score_label.config(text=f"{PTS_PLAYER} : {PTS_CPU}", fg=score_color)


root = Tk()
root.title("Paper rock scissors")
root.geometry("400x200")

text_label = Label(root, text="Let's play!", font=10, fg="green")
text_label.pack()

score_label = Label(root, text="Let's play!", font=10, fg="green")
score_label.pack(side="bottom")


possible_choices = ["paper", "rock", "scissors"]

button1 = Button(root, text="PAPER", width=8, command=lambda: game("paper"))
button2 = Button(root, text="ROCK", width=8, command=lambda: game("rock"))
button3 = Button(root, text="SCISSORS", width=8, command=lambda: game("scissors"))

button1.pack(side="left",  padx=30)
button2.pack(side="left", padx=30)
button3.pack(side="left", padx=30)

root.mainloop()
