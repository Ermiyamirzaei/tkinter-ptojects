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
    print()