import random
from tkinter import *
from tkinter import messagebox

choices = ["rock","paper","scissors"]
user_score = 0
computer_score = 0
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
        self.btn_rock = Button(root, text="🗿", command=lambda:self.play("rock"))
        self.btn_rock.pack(pady=5)

        self.btn_paper = Button(root, text="📃", command=lambda:self.play("paper"))
        self.btn_paper.pack(pady=5)

        self.btn_scissors = Button(root, text="✂️", command=lambda:self.play("scissors"))
        self.btn_scissors.pack(pady=5)

        self.result_lable = Label(root, text="")
        self.result_lable.pack(pady=5)

        self.score_lable = Label(root, text="score = 0 - 0")
        self.score_lable.pack(pady=5)

        self.animate()

    def animate(self):
        color = self.title.cget("fg")
        new_color = "red" if color == "black" else "black"
        self.title.config(fg=new_color)
        self.root.after(500, self.animate)

    def play(self, user_chioce):
        global user_score, computer_score, round_number

        user_history.append(user_chioce)
        computer_choice = ai_chioce()

        result = check_winner(user_chioce, computer_choice)

        if result == "draw":
            self.result_lable.config(text=f"Draw")

        elif result == "user":
            user_score +=1
            self.result_lable.config(text=f"You win")

        else:
            computer_score += 1
            self.result_lable.config(text=f"Computer Win!!")

        self.score_lable.config(text=f"Score: 🙍‍♂️ {user_score} - {computer_score}🐱‍🚀")
        round_number += 1

        if round_number > max_round:
            self.end_game()


    
    def end_game(self):
        ...

root = Tk()
app = RPSGame(root)
root.mainloop()