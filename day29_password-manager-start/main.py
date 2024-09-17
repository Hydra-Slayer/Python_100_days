from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- UI SETUP ------------------------------- #

WINDOW_DIM = 200
EN_WID = 35
window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)
 
label_website=Label(text="Website:")
label_website.grid(column=0, row=1)
label_email_uname = Label(text="Email/Username:")
label_email_uname.grid(column=0, row=2)
label_password = Label(text="Password:")
label_password.grid(column=0, row=3)
 
entry_website = Entry()
entry_email_uname = Entry()
entry_password = Entry()
entry_website.grid(column=1, row=1, columnspan=2, sticky="EW")
entry_website.focus()
entry_email_uname.grid(column=1, row=2, columnspan=2, sticky="EW", ipadx=10)
entry_email_uname.insert(END, "email@email.com")
entry_password.grid(column=1, row=3, sticky="EW")




# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = entry_website.get()
    email = entry_email_uname.get()
    password = entry_password.get()
    new_data = {
        website:{
            "email" : email,
            "password" : password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="The website or password cannot be empty")
    else:
        try:
            with open("data.json",'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", 'w') as data_file:
                json.dump(new_data,data_file)
        else:
            data.update(new_data)
            with open("data.json", 'w') as data_file:
                json.dump(data,data_file,indent=4)
        finally:
            entry_website.delete(0,END)
            entry_password.delete(0,END)
            messagebox.showinfo(title="Success", message="Password saved succesfully")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    entry_password.delete(0,END)
    entry_password.insert(0, password)
    pyperclip.copy(password)

def get_pwd():
    
    index = entry_website.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Password saved")
    else:
        try:
            password = data[index]["password"]
            pyperclip.copy(password)    
        except KeyError:
            messagebox.showerror(title="Error", message="No password saved for this website")
            return
        messagebox.showinfo(title="Success", message="Password copied to clipboard")
    
        
        

generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(column=2, row=3, sticky="EW")
add_btn = Button(text="Add", width=35, command=save_password)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")
get_btn = Button(text="Get", width=35,command=get_pwd)
get_btn.grid(row=5,column=1, columnspan=2,sticky="EW")
window.mainloop()

