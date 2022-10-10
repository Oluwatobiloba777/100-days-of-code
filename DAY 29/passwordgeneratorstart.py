from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generatePassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    passwordLetters = [random.choice(letters) for let in range(random.randint(8, 10))]
    passwordSymbols = [random.choice(symbols) for sym in range(random.randint(2, 4))]
    passwordNumbers = [random.choice(numbers) for num in range(random.randint(2, 4))]

    passwordList = passwordLetters + passwordSymbols + passwordNumbers
    random.shuffle(passwordList)

    password = "".join(passwordList)
    passwordEntry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = websiteEntry.get()
    email = emailEntry.get()
    password = passwordEntry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")

    else:
        # this shows a popup
        prompt = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                               f"\nPassword: {password} \n Is it ok to save?")

        if prompt:
            data = open("data.txt", "a")
            data.write(f"{website} | {email} | {password}\n")
            # this deletes entries after clicking add button
            websiteEntry.delete(0, END)
            passwordEntry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

# canvas
canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# labels
websiteLabel = Label(text="Website:")
websiteLabel.grid(row=1, column=0)
emailLabel = Label(text="Email/Username:")
emailLabel.grid(row=2, column=0)
passwordLabel = Label(text="Password:")
passwordLabel.grid(row=3, column=0)

# entries

websiteEntry = Entry(width=35)
websiteEntry.grid(row=1, column=1, columnspan=2)
websiteEntry.focus()
emailEntry = Entry(width=35)
emailEntry.grid(row=2, column=1, columnspan=2)
emailEntry.insert(0, "iamtobihunkuten@gmail.com")
passwordEntry = Entry(width=21)
passwordEntry.grid(row=3, column=1)


# buttons
generatePassword = Button(text="Generate Password", command=generatePassword)
generatePassword.grid(row=3, column=2)
addButton = Button(text="Add", width=36, command=save)
addButton.grid(row=4, column=1, columnspan=2)

window.mainloop()
