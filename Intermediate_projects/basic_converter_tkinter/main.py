from tkinter import *


def button_clicked():
    num = float(user_input.get())
    result = round(num * 1.609, 2)
    my_label2["text"] = result


window = Tk()
window.title("Miles to Km")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

my_label = Label(text="Miles")
my_label.grid(column=2, row=0)
my_label1 = Label(text="is equal to")
my_label1.grid(column=0, row=1)
my_label2 = Label(text="0")
my_label2.grid(column=1, row=1)
my_label3 = Label(text="Km")
my_label3.grid(column=2, row=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


user_input = Entry(width=15)
print(user_input.get())
user_input.grid(column=1, row=0)

window.mainloop()
