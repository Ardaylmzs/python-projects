from tkinter import *
import json
from tkinter import messagebox

TEXT_COLOR = "#E62727"
TEXT_COLOR_2 = "#FF9A00"
TEXT_COLOR_3 = "#FF0066"
TEXT_COLOR_1 = "#B4E50D"

tk = Tk()
tk.title("TO-DO List")
tk.minsize(400, 400)

# functions
def save():
    user_text = user_input.get().strip()
    user_day = day_input.get().strip()

    to_do_user.config(text="")
    user_programs.config(text="")

    if len(user_text) > 0 and len(user_day) > 0:
        information = {user_day: user_text}

        try:
            with open("schedule.json", "r") as schedule:
                data = json.load(schedule)
        except FileNotFoundError:
            data = {}

        data.update(information)

        with open("schedule.json", "w") as schedule:
            json.dump(data, schedule, indent=4)

        error_label.config(text="")
        messagebox.showinfo("Saved", f"Schedule saved for {user_day}!")
        user_input.delete(0, END)
        day_input.delete(0, END)

    else:
        error_label.config(text="Please enter your schedule and your day", fg=TEXT_COLOR)


def find():
    find_day = day_input.get().strip()

    error_label.config(text="")

    if len(find_day) > 0:
        try:
            with open("schedule.json", "r") as schedule:
                data = json.load(schedule)
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found!")
            return

        if find_day in data:
            task = data[find_day]
            to_do_user.config(text=f"{find_day}:", fg=TEXT_COLOR_2)
            user_programs.config(text="➡️ " + task, fg=TEXT_COLOR_3)
        else:
            error_label.config(text="No schedule found for that day", fg=TEXT_COLOR)
            to_do_user.config(text="")
            user_programs.config(text="")
    else:
        error_label.config(text="Please enter a day", fg=TEXT_COLOR)
        to_do_user.config(text="")
        user_programs.config(text="")


# gui - designs
Label(tk, text="TO-DO List", font=("Arial", 20)).grid(row=0, column=0, columnspan=2, pady=10)

Label(tk, text="Your schedule:", font=("Arial", 14), fg=TEXT_COLOR).grid(row=1, column=0, sticky="e")
user_input = Entry(tk, width=30)
user_input.grid(row=1, column=1)

Label(tk, text="Your day:", font=("Arial", 14), fg=TEXT_COLOR).grid(row=2, column=0, sticky="e")
day_input = Entry(tk, width=30)
day_input.grid(row=2, column=1)

Button(tk, text="SAVE", command=save).grid(row=3, column=0, pady=10)
Button(tk, text="SHOW", command=find).grid(row=3, column=1, pady=10)


error_label = Label(tk, text="", font=("Arial", 12), fg=TEXT_COLOR)
error_label.grid(row=4, column=0, columnspan=2, pady=5)

to_do_user = Label(tk, text="", font=("Arial", 16))
to_do_user.grid(row=5, column=0, columnspan=2, pady=10)

user_programs = Label(tk, text="", font=("Arial", 14), wraplength=300, justify="left")
user_programs.grid(row=6, column=0, columnspan=2)

tk.mainloop()
