from tkinter import *
from tkinter import messagebox
import random
import string
import csv
import os
def generate_captcha():
    letters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters) for i in range(5))

def refresh_captcha():
    new_captcha = generate_captcha()
    captcha_lable.config(text=new_captcha)
def show_hide_pass():
    if password_entry.cget("show") == "*":
        password_entry.config(show='')
        show_hide.config(text="hide")
    else:
        password_entry.config(show='*')
        show_hide.config(text="show")
def login_user():
    username = user_entry.get()
    password = password_entry.get()
    user_captcha = captcha_entry.get()
    current_captcha = captcha_lable.cget("text")

    if user_captcha != current_captcha:
        messagebox.showerror("error", "Incorrect Captcha")
        refresh_captcha()
        return
    
    if os.path.exists("user.csv"):
        with open("user.csv", "r") as file:
            reader =  csv.reader(file)
            for row in reader:
                if row and row[0] == username and row[1] == password:
                    messagebox.showinfo("Sucsses", "welcom to your account!")
                    return
        messagebox.showerror("error", "Invalid username oe password")
    else:
        messagebox.showerror("error", "No user registered yet")
    refresh_captcha()

def register_user():
    reg_window = Toplevel(root)
    reg_window.title("Register")
    reg_window.geometry("300x250")

    Label(reg_window ,text="username",bg="#5AF0D7",font=("arial", 16)).pack(pady=5)
    new_user = Entry(reg_window)
    new_user.pack(pady=5)

    Label(reg_window ,text="password", bg="#5AF0D7",font=("arial", 16)).pack(pady=5)
    new_pas = Entry(reg_window, show="*")
    new_pas.pack(pady=5)

    def save_to_csv():
        username = new_user.get()
        password = new_pas.get()

        if username == "" or password == "":
            messagebox.showwarning("warning", "connot be empty")
            return
        
        with open("user.csv", "a", newline='')as file:
            writer = csv.writer(file)
            writer.writerow([username, password])
        
        messagebox.showinfo("Succses", "Registeration successful!")
        reg_window.destroy()
    
    Button(reg_window, text="Register",command=save_to_csv).pack(pady=20)
root = Tk()
root.title("login")
root.geometry("340x500")
root.config(bg="#40E0D0")
Label(root,text="login",bg="#5AF0D7",font=("arial", 16, "bold")).pack()
#Frame
frame = Frame(root, bg="#D4FFF8",padx=25,pady=25,relief="flat")
frame.pack(padx=30, pady=10, fill=BOTH)
#username
Label(frame,text="username",bg="#D4FFF8",font=("arial", 16)).grid(row=0,column=0, sticky=W,pady=(0,3))
user_entry = Entry(frame)
user_entry.grid(row=1, column=0)

#password
Label(frame,text="password", bg="#D4FFF8",font=("arial", 16)).grid(row=2,column=0, sticky=W,pady=(0,3))
password_entry = Entry(frame, show="*", width=20)
password_entry.grid(row=3, column=0, sticky=W)
show_hide = Button(frame, text="show",font=("arial",12,"bold"),command=show_hide_pass)
show_hide.grid(row=3, column=1, sticky=W)



#-------------------------Capcha---------------------------------------------
Label(frame,text="captcha code",bg="#D4FFF8",font=("arial", 16)).grid(row=4,column=0,sticky=W)
captcha_lable = Label(frame,text=generate_captcha(),font=("arial", 20, "bold"), bg="white")
captcha_lable.grid(row=5, column=0)

captcha_entry = Entry(frame,width=20)
captcha_entry.grid(row=6, column=0, sticky=W)
Button(frame,text="⟲",font=("arial",12,"bold"), command=refresh_captcha).grid(row=6,column=1)



Button(frame, text="login",bg="#D4FFF8", command=login_user).grid(row=7,column=0)
Button(frame,text="register",bg="#D4FFF8", command=register_user).grid(row=9,column=0)

root.mainloop()