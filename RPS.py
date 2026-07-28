import random
from tkinter import *
from tkinter import messagebox

choices = ["rock","paper","scissors"]
user_score = 0
coputer_score = 0
round_number = 1
max_round = 5
user_history = []

def ai_chioce():
    if not user_history:
        return random.choice(choices)

    most_common = max(set(user_history), key=user_history.count)
    if most_common == "rock":
        return"paper"
    if most_common == "paper":
        return "scissors"
    else:
        return "rock"

def check_winner(user, computer):
    if user == computer:
        return "draw"

    elif(user == "rock" and computer == "scissors") or \
        (user == "paper" and computer == "rock") or \
        (user == "scissors" and computer == "paper"):
            return "user"
    else:
        return "computer"

class RPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("rock paper scissers")

        self.title = Label(root, text="rock paper scissers", font=("Arial", 18))
        self.title.pack(pady=10)

        self.info = Label(root, text="choose your move: ", font=("Arial", 18))
        self.title.pack(pady=10)
        #buttons
        self.btn_rock = Button(root, text="🗿", command=...)
        self.btn_rock.pack(pady=5)

        self.btn_paper = Button(root, text="📃", command=...)
        self.btn_paper.pack(pady=5)

        self.btn_scissors = Button(root, text="✂️", command=...)
        self.btn_scissors.pack(pady=5)


root = Tk()
app = RPSGame(root)
root.mainloop()