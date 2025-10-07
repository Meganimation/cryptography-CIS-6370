from tkinter import *
from tkinter import StringVar
from create_account import attemptToCreateAccount

def show_create_account():
    # Hide the main menu widgets
    askLabel.pack_forget()
    newUserButton.pack_forget()
    returningUserButton.pack_forget()
    


root = Tk()
root.title("Data Security Project")


##create a basic app asking if they want to create an account or login

askLabel = Label(root, text="Are you a new user or returning user?", fg="green", bg="black")

newUserButton = Button(root, text="New User", padx=20, pady=20)
returningUserButton = Button(root, text="Returning User", padx=20, pady=20, command=show_create_account)


askLabel.pack()
newUserButton.pack()
returningUserButton.pack()
