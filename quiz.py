from tkinter import *
from tkinter import ttk,messagebox
import random

def new_quistion():
    global num1, num2, answer
    max_num = 10 + score // 20
    num1 = random.randint(1, max_num)
    num2 = random.randint(1, max_num)
    answer = num1 + num2
    quistuion_lable.config(text=f"{num1} + {num2}")
    answer_entry.delete(0, END)



def check_answer():
    global score, answer, high_score
    try:
        user_answer = int(answer_entry.get())
    except ValueError:
        messagebox.showwarning("Invalid input please hust number")
        return
    
    if user_answer == answer:
        score += 5
    else:
        score -= 10

    score_lable.config(text=f"Score: {score}")
    prtogress['value'] = score

    if score > high_score:
        high_score = score
        high_score_lable.config(text=f"High score: {high_score}")
    
    if score > 50:
        win_game()
    else:
        new_quistion()


def win_game():
    win_window = Toplevel()
    win_window.title("Winnerr!!")
    win_window.geometry("300x150")
    win_window.configure(bg="green")

    win_lable = Label(win_window, text="You winn!!!", font=("Arial", 18),bg="green", fg="white")
    win_lable.pack(expand=TRUE)
def count_down():
    global time_left, score
    if time_left > 0:
        timer_label.config(text=f"Time Left: {time_left}s")
        time_left-= 1
        root.after(1000, count_down)
    else:
        score -= 5
        score_lable.config(text=f"Score: {score} ")
        new_quistion()
        reset_timer()

def reset_timer():
    global time_left
    time_left = 10
    count_down()


high_score = 0
#time_left = 10
score = 0
answer = 0
root = Tk()
root.title("Qiuz")
root.geometry("500x300")

timer_label = Label(root, text="Time Left: 10s", font=("Arial", 12), fg="red")
timer_label.pack()

score_lable = Label(root, text="Score: 0 ",font=("Arial", 12))
score_lable.pack()

prtogress = ttk.Progressbar(root, length=250, maximum=50)
prtogress.pack(pady=10)

Label(root, text="Qiustion:", font=("Arial", 12)).pack()
quistuion_lable = Label(root, text="", font=("Arial",12))
quistuion_lable.pack()

Label(root, text="your answe:", font=("Arial", 12)).pack()
answer_entry = Entry(root, font=("Arial", 12))
answer_entry.pack()

check_button = Button(root, text="check", font=("Arial", 12), bg="orange", command=check_answer)
check_button.pack()

high_score_lable = Label(root, text="High score: 0", font=("Arial", 12), fg="blue")
high_score_lable.pack()





reset_timer()
new_quistion()
root.mainloop()