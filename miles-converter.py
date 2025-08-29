from tkinter import *

window = Tk()
window.title("Mi - Km Converter")
window.geometry("210x220")


def convert():
    global label_km ,label_miles ,choice
    button_choice = choice.get()
    input_convert = float(input.get())
    if button_choice== 1:
        count = input_convert * 1.609
        label_count.config(text=f"{count} kilometers")
        label_count_2.config(text=f"{input_convert} miles")
    if button_choice == 2:
        count_1 = input_convert / 1.609
        label_count_2.config(text=f"{count_1} miles")
        label_count.config(text=f"{input_convert} kilometers")
label = Label(text="Mi <--> Km Converter",padx=10,pady=10)
label.grid(column=1, row=0)
input = Entry(width=10)
input.grid(column=1, row=1)

def radio_used():
    print(choice.get())

button = Button(text="Convert",border=3, command=convert)
button.grid(column=1, row=2)
label_km = Label(text="km")
label_km.grid(column=1, row=3)
label_count = Label(text="0")
label_count.grid(column=1, row=4)
label_miles = Label(text="miles")
label_miles.grid(column=1, row=5)
label_count_2 = Label(text="0")
label_count_2.grid(column=1, row=6)
choice = IntVar()
choice_btn = Radiobutton(text="km", variable=choice, value=1 , command=radio_used)
choice_btn_1 = Radiobutton(text="miles", variable=choice, value=2 , command=radio_used)
choice_btn_1.grid(column=1, row=7)
choice_btn.grid(column=1, row=8)

window.mainloop()