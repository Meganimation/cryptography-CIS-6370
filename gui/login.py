
from tkinter import *
from tkinter import StringVar
import bcrypt
import json

def attempt_to_login(frame, show_main_menu, show_landing_page):
    # Clear the frame first
    for widget in frame.winfo_children():
        widget.destroy()
        
    password_var = StringVar()
    warning_var = StringVar()

    titleLabel = Label(frame, text="Login", fg="green", bg="black", font=("Arial", 18, "bold"))
    
    accountLabel = Label(frame, text="Username:", fg="green", bg="black", font=("Arial", 12))
    eUserInput = Entry(frame, width=40, bg="black", fg="green", borderwidth=2, 
                      relief="solid", font=("Arial", 11), insertbackground="green")
    passwordLabel = Label(frame, text="Password:", fg="green", bg="black", font=("Arial", 12))
    ePasswordInput = Entry(frame, width=40, bg="black", fg="green", borderwidth=2, 
                          textvariable=password_var, show="*", relief="solid", 
                          font=("Arial", 11), insertbackground="green")
    warningLabel = Label(frame, textvariable=warning_var, fg="red", bg="black", font=("Arial", 10))
    
    # Create buttons
    myButton = Button(frame, text="Login", padx=30, pady=12,
                     bg="black", fg="green", font=("Arial", 12, "bold"), 
                     borderwidth=2, relief="solid", activebackground="green", 
                     activeforeground="black")
    myBackButton = Button(frame, text="Back", padx=30, pady=12,
                         bg="black", fg="green", font=("Arial", 12), 
                         borderwidth=2, relief="solid", activebackground="green", 
                         activeforeground="black")
    
    def go_back():
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
                    show_landing_page(frame.master, account)
                else:
                    print("Login failed.")
                    warning_var.set("Invalid username or password.")
                return
        
        print("Account not found.")
        warning_var.set("Invalid username or password.")

    # Configure button commands after functions are defined
    myButton.config(command=on_submit)
    myBackButton.config(command=lambda: [clear_warning(), go_back()])

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
    




