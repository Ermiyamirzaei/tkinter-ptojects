from tkinter import *

is_on = True

def temp_up():
    global is_on

    if not is_on:
        return

    temp = int(entry.get().replace("°C", ""))

    if temp < 30:
        temp += 1

    entry.delete(0, END)
    entry.insert(0, f"{temp}°C")


def temp_down():
    global is_on

    if not is_on:
        return

    temp = int(entry.get().replace("°C", ""))

    if temp > 16:
        temp -= 1

    entry.delete(0, END)
    entry.insert(0, f"{temp}°C")


def shut_down():
    global is_on
    is_on = False
    entry.delete(0, END)
    entry.insert(0, "OFF")


def turn_on():
    global is_on
    is_on = True
    entry.delete(0, END)
    entry.insert(0, "24°C")


root = Tk()
root.title("Cooler Control")
root.geometry("250x300")

entry = Entry(root, width=15, font=("Arial", 22), justify=CENTER)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
entry.insert(0, "24°C")

buttons = [
    ("↑", 1, 0),
    ("↓", 1, 3),
    ("turn on", 8, 3)
]

for text, row, col in buttons:

    if text == "↑":
        btn = Button(root, text=text,bg="#5ad941", width=5, height=2,
                     font=("Arial", 14), command=temp_up)

    elif text == "↓":
        btn = Button(root, text=text, width=5,bg="#bdd941", height=2,
                     font=("Arial", 14), command=temp_down)

    elif text == "turn on":
        btn = Button(root, text=text,bg="#4b41d9" ,width=8, height=2,
                     font=("Arial", 14), command=turn_on)

    btn.grid(row=row, column=col, padx=5, pady=5)


shutdown = Button(root,
                  text="shut down",
                  bg="#d94141",
                  width=8,
                  height=2,
                  font=("Arial", 14),
                  command=shut_down)

shutdown.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()