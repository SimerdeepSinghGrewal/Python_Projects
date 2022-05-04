from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_l = [choice(letters) for num in range(randint(8, 10))]
    password_s = [choice(symbols) for num in range(randint(2, 4))]
    password_n = [choice(numbers) for num in range(randint(2, 4))]
    pass_list = password_l + password_s + password_n
    shuffle(pass_list)
    password = "".join(pass_list)
    pyperclip.copy(password)
    password_text.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    site_name = website_text.get()
    mail_id = email_text.get()
    pass_user = password_text.get()
    new_dict = {
        site_name: {
            "Email": mail_id,
            "Password": pass_user,
        }
    }
    if len(site_name) == 0 or len(mail_id) == 0 or len(pass_user) == 0:
        messagebox.showerror(title="Error", message="Please enter all the fields.")
    else:
        try:
            with open("password_manager.json", "r") as file:
                pass_data = json.load(file)
        except FileNotFoundError:
            with open("password_manager.json", "w") as file:
                json.dump(new_dict, file, indent=4)
        else:
            pass_data.update(new_dict)
            with open("password_manager.json", "w") as file:
                json.dump(pass_data, file, indent=4)
        finally:
            website_text.delete(0, 'end')
            password_text.delete(0, 'end')


# ----------------------------SEARCH SETUP-------------------------------#

def search():
    site_name = (website_text.get()).title()
    try:
        with open("password_manager.json", "r") as data_file:
            pass_data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Please add some data first.")

    try:
        user_info = {key: value for (key, value) in pass_data.items() if key == site_name}
    except KeyError:
        messagebox.showerror(title="Error", message="No data found")
    mail = user_info[site_name]["Email"]
    pas = user_info[site_name]["Password"]
    pyperclip.copy(pas)
    messagebox.showinfo(title=site_name, message=f"Email: {mail}\n Password: {pas}\n\npassword copied to clipboard")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=140, height=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(85, 100, image=pass_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky=E)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, sticky=E)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky=E)

website_text = Entry(width=23)
website_text.grid(column=1, row=1, sticky=W)
website_text.focus()
email_text = Entry(width=42)
# pre entered email id
email_text.insert(0, "@yahoo.com")
email_text.grid(column=1, row=2, columnspan=2, sticky=W)
password_text = Entry(width=23)
password_text.grid(column=1, row=3, sticky=W)

search_btn = Button(text="Search", width=15, command=search)
search_btn.grid(column=2, row=1, sticky=E)
gen_pass_btn = Button(text="Generate Password", width=15, command=gen_pass)
gen_pass_btn.grid(column=2, row=3, sticky=E)
add_btn = Button(text="Add", width=35, command=save_pass)
add_btn.grid(column=1, row=4, columnspan=2, sticky=W)

window.mainloop()
