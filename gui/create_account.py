from tkinter import *
from tkinter import StringVar

root = Tk()
root.title("Data Security Project")


accountLabel = Label(root, text="Account", fg="green", bg="black")
eUserInput = Entry(root, width=50, bg="black", fg="green", borderwidth=2)
passwordLabel = Label(root, text="Password", fg="green", bg="black")
password_var = StringVar()
ePasswordInput = Entry(root, width=50, bg="black", fg="green", borderwidth=2, textvariable=password_var, show="*")

confirmPasswordLabel = Label(root, text="Confirm Password", fg="green", bg="black")
confirm_password_var = StringVar()
eConfirmPasswordInput = Entry(root, width=50, bg="black", fg="green", borderwidth=2, textvariable=confirm_password_var, show="*")

warning_var = StringVar()
warningLabel = Label(root, textvariable=warning_var, fg="red", bg="black")

def clear_warning(event=None):
    warning_var.set("")

def attemptToCreateAccount():
    account = eUserInput.get()
    password = ePasswordInput.get()
    if len(password) < 8:
        warning_var.set("Hey! This is a project about data security and encryption! Your password can't be too short because it helps protect your account from brute-force attacks. Please choose a password at least 8 characters long.")
        return
    if password != eConfirmPasswordInput.get():
        warning_var.set("Passwords do not match. Please try again.")
        return
    print("Attempting login for account:", account)
    print("With password:", password)
    print("DO SOMETHING SECURE WITH THIS INFO (Ie encrypt it)")
    accountLabel.pack()
    eUserInput.pack()
    passwordLabel.pack()
    ePasswordInput.pack()
    confirmPasswordLabel.pack()
    eConfirmPasswordInput.pack()
    warningLabel.pack()
    myButton.pack()

myButton = Button(root, text="Click Me!", padx=20, pady=20, command=attemptToCreateAccount)








# Remove warning when user types in password field
ePasswordInput.bind("<Key>", clear_warning)



root.mainloop()
