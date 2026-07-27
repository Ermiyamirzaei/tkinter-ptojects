from tkinter import *

def temp_up():
    temp = entry.get()

    if temp == "OFF":
        return

    temp = temp.replace("°C", "")
    temp = int(temp)

    if temp < 30:
        temp = temp + 1

    entry.delete(0, END)
    entry.insert(0, str(temp) + "°C")


def temp_down():
    temp = entry.get()

    if temp == "OFF":
        return

    temp = temp.replace("°C", "")
    temp = int(temp)

    if temp > 16:
        temp = temp - 1

    entry.delete(0, END)
    entry.insert(0, str(temp) + "°C")


def shut_down():
    entry.delete(0, END)
    entry.insert(0, "OFF")


def turn_on():
    entry.delete(0, END)
    entry.insert(0, "24°C")


root = Tk()
root.title("Cooler Control")
root.geometry("250x300")

entry = Entry(root, width=15, font=("Arial", 22), justify=CENTER)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
entry.insert(0, "24°C")

up_btn = Button(root, text="↑", bg="#5ad941",
                width=5, height=2,
                font=("Arial", 14),
                command=temp_up)

up_btn.grid(row=1, column=0, padx=5, pady=5)

down_btn = Button(root, text="↓", bg="#bdd941",
                  width=5, height=2,
                  font=("Arial", 14),
                  command=temp_down)

down_btn.grid(row=1, column=3, padx=5, pady=5)

on_btn = Button(root, text="turn on", bg="#4b41d9",
                width=8, height=2,
                font=("Arial", 14),
                command=turn_on)

on_btn.grid(row=8, column=3, padx=5, pady=5)

off_btn = Button(root, text="shut down", bg="#d94141",
                 width=8, height=2,
                 font=("Arial", 14),
                 command=shut_down)

off_btn.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()