from tkinter import *
def click(value):
    curret = entry.get()
    entry.delete(0, END)
    entry.insert(0,curret + str(value))

def clear():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

root = Tk()
root.title("calculator")
#root.config(bg="#22203c")
# root.resible(False, FALSE)
entry = Entry(root, width=20, font=("Arial", 20), justify=RIGHT)
entry.grid(row=0,column=0, columnspan=4,padx=10,pady=10)

buttons = [
    ("9", 1, 0), ("8", 1, 1), ("7", 1, 2), ("/", 1, 3),
    ("6", 2, 0), ("5", 2, 1), ("4", 2, 2), ("*", 2, 3),
    ("3", 3, 0), ("2", 3, 1), ("1", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for text, row, col in buttons:
    if text == "=":
        btn = Button(root, text=text, width=5, height=2, font=("Arial", 14), command=calculate)

    else: btn = Button(root, text=text, width=5, height=2, font=("Arial", 14), command=lambda t=text: click(t))
    btn.grid(row=row, column=col, padx=5,pady=5)


clear_btn = btn = Button(root, text="C", width=23, height=2, font=("Arial", 14), command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()