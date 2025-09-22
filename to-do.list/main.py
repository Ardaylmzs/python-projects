from tkinter import *
import json
from tkinter import messagebox

TEXT_COLOR = "#E62727"
TEXT_COLOR_2 ="#FF9A00"
TEXT_COLOR_3 ="#FF0066"
counter = 0
count = 0
TEXT_COLOR_1 = "#B4E50D"

tk = Tk()
tk.title("TO-DO List")
tk.minsize(400, 400)

# functions
def save():
    global counter
    counter += 1
    user_text = user_input.get()
    user_day = day_input.get()
    if len(user_text) > 0 and len(user_day) > 0:
        print("your schedule is saved successfully !")
        if counter % 2 == 1:
            counter = 0
            user_input.delete(0, END)
        information_day = f"{user_day}"
        information = {
            information_day: {
                f"{user_day}": f"{user_text}",
        }
        }
        try:
            with open("schedule.json", "r") as schedule:
                data = json.load(schedule)
        except FileNotFoundError:
            with open("schedule.json", "w") as schedule:
                json.dump(information,schedule, indent=6)
                print("File is created because of not existing schedule.json")
        else:
            data.update(information)
            with open("schedule.json", "w") as schedule:
                json.dump(data,schedule, indent=6)
                print("Schedule is saved successfully !")
        finally:
            user_input.delete(0, END)
            day_input.delete(0, END)
    else:
        print("Please enter your schedule and your day")
        user_progres.config(text="please enter your schedule and your day",fg=TEXT_COLOR)
        user_progres.place(x=-80, y=110)

def find():
    global count
    count +=1
    find_day = day_input.get()
    information_day = f"{find_day}"
    if len(find_day) > 0:

        try:
            with open("schedule.json", "r") as schedule:
                data = json.load(schedule)
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found !")
            return
        if information_day in data:
            print("your schedule is found successfully !")
            information_days = data[information_day][f"{find_day}"]
            information_programs = find_day
            to_do_user.config(text=information_programs + ":",fg=TEXT_COLOR_2)
            to_do_user.place(x=100, y=140)


            user_programs.config(text="➡️ " + information_days, fg=TEXT_COLOR_3)
            user_programs.place(x=90, y=180)
    else:
        print("don't exist such day")
        messagebox.showerror("Error", "No such day")

# gui - designs
text_label = Label(tk, text="TO-DO List")
text_label.config(font=("Arial", 20))
text_label.grid(row=0, column=0)
user_input = Entry(tk)
user_input.grid(row=1, column=1)
user_input.focus()
input_text = Label(tk , text="your schedule" ,font=("Arial", 18),fg=TEXT_COLOR)
input_text.grid(row=1, column=0 )
save_button = Button(tk, text="SAVE" , command=save)
save_button.grid(row=1, column=3 )
day_input = Entry(tk)
day_input.grid(row=2, column=1)
day_information = Label(tk , text="your day", font=("Arial", 18),fg=TEXT_COLOR)
day_information.grid(row=2, column=0)
user_progres = Label(tk , text="your progres", font=("Arial", 18),fg=TEXT_COLOR_1)
user_progres.grid(row=3, column=0)
find_button = Button(tk,text="show schedule", command=find)
find_button.grid(row=2, column=3)
to_do_user = Label(tk,text="✅", font=("Arial", 18))
to_do_user.grid(row=4, column=1)


user_programs = Label(tk, text="", font=("Arial", 18), wraplength=250, justify="left")

tk.mainloop()
