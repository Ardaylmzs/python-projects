from tkinter import *
from passwordgenerater import *
import json
from tkinter import messagebox

window = Tk()
window.title("Password Manager")
window.geometry("500x400")
window.config(padx=10, pady=10)

window.count = 0
canvas = Canvas(window, width=200, height=200 , )
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# functions
def control_char(text,input_1,input_2):
    characters = "çğıöşüÇĞİÖŞÜ[]{}^&*()$#!+=%?><:'$,/;"
    pass_characters = "çğıöşüÇĞİÖŞÜ"
    for char in characters:
        if char in text:
            return True
    for char in characters:
        if char in input_1:
            return True
    for char in pass_characters:
        if char in input_2:
            return True
    return False

def generating():
    window.count += 1
    if window.count % 2 == 0:
        password_entry.delete(0 ,END)
    if window.count % 2 == 1 or window.count == 1:
        password_entry.insert(0,password_function())
def save():
    site = password_entry_name.get()
    email = user_input.get()
    passwords = password_entry.get()

    if len(site) == 0 or len(email) == 0 or len(passwords) == 0:
        messagebox.showerror("Error", "Please fill all the fields")
    elif control_char(site,email,passwords):
        messagebox.showerror("Error", "Please only use english letters")
        password_entry.delete(0, END)
        user_input.delete(0, END)
        password_entry_name.delete(0, END)
    else:
        key = f"{site}--->{email}"
        information = {
            key: {
                "password name": site,
                "email / username": email,
                "password": passwords
            }
        }
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(information, file , indent=6)
            print("File is created")
        else:
            data.update(information)

            with open("data.json", "w") as file:
                json.dump(data, file, indent=6)
        finally:
            password_entry.delete(0, END)
            user_input.delete(0, END)
            password_entry_name.delete(0, END)
def recall_function():
    site = password_entry_name.get()
    email = user_input.get()

    key = f"{site}--->{email}"

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error!", message="No data found!")
        return

    if key in data:
        passwords = data[key]["password"]
        password_entry.delete(0, "end")
        password_entry.insert(0, passwords)
        messagebox.showinfo(title="password", message=f"{site} password: {passwords}")
    else:
        messagebox.showerror(title="Error!", message="No data found!!")

#Entries
password_entry_name = Entry(window)
password_entry_name.grid(row=1, column=1)
password_entry = Entry(window ,width=20)
password_entry.grid(row=3, column=1)
user_input = Entry(window)
user_input.grid(row=2, column=1)

#Label
password_text = Label(window, text="Password Name", fg="black")
password_text.grid(row=1, column=0)
user_email = Label(window, text="Email Address/ Username", fg="black")
user_email.grid(row=2, column=0)
password = Label(window, text="Password", fg="black")
password.grid(row=3, column=0)

# Buttons
password_generate = Button(text="generate" ,width=10 ,padx=-20 , command=generating)
password_generate.grid(row=3, column=2 )
save_password = Button(text="save" , width=16 , command=save)
save_password.grid(row=4, column=1 )
recall_button = Button(text="recall" ,width=10, command=recall_function)
recall_button.grid(row=4, column=2 )
window.mainloop()