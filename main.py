from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


app = Tk()
app.title("Password Manager")
img =Image.open('/Users/omkar/Documents/desktop pic//sum.jpg')
bg = ImageTk.PhotoImage(img)

app.geometry("650x500")


# Add image
label = Label(app, image=bg)
label.place(x = 0,y = 0)

website_label = Label(text="Website:",bg='purple',bd=3,cursor="dot",relief=SUNKEN).place(x=150,y=200)

email_label = Label(text="Email:",bg='purple',bd=3,cursor="dot",relief=SUNKEN,padx=8).place(x=150,y=250)

password_label = Label(text="Password:",bg='purple',bd=3,cursor="dot",relief=SUNKEN).place(x=150,y=300)


# Entries
website_entry = Entry(width=21)
website_entry.place(x=250,y=200)
website_entry.focus()
email_entry = Entry(width=21)
email_entry.place(x=250,y=250)
email_entry.insert(0, "oholomkar@40gmail.com")
password_entry = Entry(width=21,bg="black")
password_entry.place(x=250,y=300)

# Add text
# Buttons
search_button = Button(text="Search", width=5, command=find_password,bg="blue",fg='blue',cursor="arrow",relief=SUNKEN).place(x=460,y=200)


generate_password_button = Button(text="Generate Password",width=12, command=generate_password,bg='blue',fg='blue').place(x=460,y=300)

add_button = Button(text="Add", width=10, command=save,bg="blue",fg="green",relief=RIDGE).place(x=270,y=370)



# Execute tkinter
app.mainloop()