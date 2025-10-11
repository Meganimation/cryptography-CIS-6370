
from tkinter import *
from tkinter import StringVar
import bcrypt
import json

def attempt_to_create_account(root, show_main_menu):
    password_var = StringVar()
    confirm_password_var = StringVar()
    warning_var = StringVar()
    
    accountLabel = Label(root, text="Account", fg="green", bg="black")
    eUserInput = Entry(root, width=50, bg="black", fg="green", borderwidth=2)
    passwordLabel = Label(root, text="Password", fg="green", bg="black")
    ePasswordInput = Entry(root, width=50, bg="black", fg="green", borderwidth=2, textvariable=password_var, show="*")
    confirmPasswordLabel = Label(root, text="Confirm Password", fg="green", bg="black")
    eConfirmPasswordInput = Entry(root, width=50, bg="black", fg="green", borderwidth=2, textvariable=confirm_password_var, show="*")
    warningLabel = Label(root, textvariable=warning_var, fg="red", bg="black")
    
    def save_account(username, hashed_password):
        data = {"username": username, "password": hashed_password.decode()}
        try:
            with open("accounts.json", "r") as f:
                accounts = json.load(f)
                if not isinstance(accounts, list):
                    accounts = []
        except (FileNotFoundError, json.JSONDecodeError):
            accounts = []
        accounts.append(data)
        with open("accounts.json", "w") as f:
            json.dump(accounts, f, indent=2)
    
    def go_back():
        accountLabel.pack_forget()
        eUserInput.pack_forget()
        passwordLabel.pack_forget()
        ePasswordInput.pack_forget()
        confirmPasswordLabel.pack_forget()
        eConfirmPasswordInput.pack_forget()
        warningLabel.pack_forget()
        myButton.pack_forget()
        myBackButton.pack_forget()
        show_main_menu()

    def clear_warning(event=None):
        warning_var.set("")

    def on_submit():
        account = eUserInput.get()
        password = ePasswordInput.get()
        confirm_password = eConfirmPasswordInput.get()
        if not account:
            warning_var.set("Account field cannot be empty.")
            return
        if len(password) < 8:
            warning_var.set("Hey! This is a project about data security and encryption! Your password can't be too short because it helps protect your account from brute-force attacks. Please choose a password at least 8 characters long.")
            return
        if password != confirm_password:
            warning_var.set("Passwords do not match. Please try again.")
            return
        warning_var.set("")
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        save_account(account, hashed)
        go_back()

    myButton = Button(root, text="Create Account", padx=20, pady=20, command=on_submit)
    myBackButton = Button(root, text="Back", padx=20, pady=20, command=lambda: [clear_warning(), go_back()])

    accountLabel.pack()
    eUserInput.pack()
    passwordLabel.pack()
    ePasswordInput.pack()
    confirmPasswordLabel.pack()
    eConfirmPasswordInput.pack()
    warningLabel.pack()
    myButton.pack()
    myBackButton.pack()

    ePasswordInput.bind("<Key>", clear_warning)
    eConfirmPasswordInput.bind("<Key>", clear_warning)




