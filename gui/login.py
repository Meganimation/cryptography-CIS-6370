
from tkinter import *
from tkinter import StringVar
import bcrypt
import json

def attempt_to_login(root, show_main_menu, show_landing_page):
    password_var = StringVar()
    warning_var = StringVar()

    titleLabel = Label(root, text="Login", fg="green", bg="black", font=("Arial", 18, "bold"))
    
    accountLabel = Label(root, text="Username:", fg="green", bg="black", font=("Arial", 12))
    eUserInput = Entry(root, width=40, bg="black", fg="green", borderwidth=2, 
                      relief="solid", font=("Arial", 11), insertbackground="green")
    passwordLabel = Label(root, text="Password:", fg="green", bg="black", font=("Arial", 12))
    ePasswordInput = Entry(root, width=40, bg="black", fg="green", borderwidth=2, 
                          textvariable=password_var, show="*", relief="solid", 
                          font=("Arial", 11), insertbackground="green")
    warningLabel = Label(root, textvariable=warning_var, fg="red", bg="black", font=("Arial", 10))
    
    # Create buttons first
    myButton = Button(root, text="Login", padx=30, pady=12,
                     bg="black", fg="green", font=("Arial", 12, "bold"), 
                     borderwidth=2, relief="solid", activebackground="green", 
                     activeforeground="black")
    myBackButton = Button(root, text="Back", padx=30, pady=12,
                         bg="black", fg="green", font=("Arial", 12), 
                         borderwidth=2, relief="solid", activebackground="green", 
                         activeforeground="black")
    
    def go_back():
        titleLabel.pack_forget()
        accountLabel.pack_forget()
        eUserInput.pack_forget()
        passwordLabel.pack_forget()
        ePasswordInput.pack_forget()
        warningLabel.pack_forget()
        myButton.pack_forget()
        myBackButton.pack_forget()
        show_main_menu()

    def clear_warning(event=None):
        warning_var.set("")

    def on_submit():
        account = eUserInput.get()
        password = ePasswordInput.get()
        if not account:
            warning_var.set("Account field cannot be empty.")
            return
        if not password:
            warning_var.set("Password field cannot be empty.")
            return
        warning_var.set("")
        print("Attempting login for account:", account)
        print("With password (hashed):", password)
        try:
            with open("accounts.json", "r") as f:
                accounts = json.load(f)
                if not isinstance(accounts, list):
                    accounts = []
        except (FileNotFoundError, json.JSONDecodeError):
            accounts = []
        
        for account_data in accounts:
            if account_data["username"] == account:
                if bcrypt.checkpw(password.encode(), account_data["password"].encode()):
                    print("Login successful!")
                    show_landing_page(root, account)
                else:
                    print("Login failed.")
                    warning_var.set("Invalid username or password.")
                return
        
        print("Account not found.")
        warning_var.set("Invalid username or password.")

    myButton = Button(root, text="Login", padx=30, pady=12, command=on_submit,
                     bg="black", fg="green", font=("Arial", 12, "bold"), 
                     borderwidth=2, relief="solid", activebackground="green", 
                     activeforeground="black")
    myBackButton = Button(root, text="Back", padx=30, pady=12, command=go_back,
                         bg="black", fg="green", font=("Arial", 12), 
                         borderwidth=2, relief="solid", activebackground="green", 
                         activeforeground="black")

    titleLabel.pack(pady=(30, 20))
    accountLabel.pack(pady=(10, 5))
    eUserInput.pack(pady=(0, 15))
    passwordLabel.pack(pady=(0, 5))
    ePasswordInput.pack(pady=(0, 10))
    warningLabel.pack(pady=(0, 15))
    myButton.pack(pady=10)
    myBackButton.pack(pady=5)


    ePasswordInput.bind("<Key>", clear_warning)
    eUserInput.bind("<Key>", clear_warning)
    




