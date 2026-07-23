from tkinter import *
def click(valiu):
    ...

def shut_down():
    ...

def cooler():
    ...
    
def turn_on():
    ...







root = Tk()
root.title("cooler control")
entry = Entry(root,width=15,font=("Arial", 22), justify=CENTER)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
entry.insert(0,"24°C")
root.geometry("250x300")

buttons = [
    ("↑",1,0), ("↓",1,3),("turn on",8,3)
]


for text, row, col in buttons:
    if text== "turn on":
        btn = Button(root, text=text, width=5, height=2, font=("Arial", 14), command=turn_on)
    else:
        btn = Button(root, text=text, width=5, height=2, font=("Arial", 14), command=lambda t=text: click(t))
    btn.grid(row=row, column=col, padx=3,pady=5)


shutdown = Button(root, text="shut down", width=8, height=2, font=("Arial", 14), command=shut_down)
shutdown.grid(row=7, column=0, columnspan=2, padx=5, pady=5)


root.mainloop()