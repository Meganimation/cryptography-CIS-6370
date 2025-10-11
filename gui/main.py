from tkinter import *
from create_account import attempt_to_create_account
from login import attempt_to_login
from home import home

def show_main_menu():
    askLabel.pack(pady=(50, 30))
    newUserButton.pack(pady=10)
    returningUserButton.pack(pady=10)

def show_create_account():
    askLabel.pack_forget()
    newUserButton.pack_forget()
    returningUserButton.pack_forget()
    attempt_to_create_account(root, show_main_menu)
    
def show_login():
    print("Login functionality to be implemented.")
    attempt_to_login(root, show_main_menu, show_landing_page)
    askLabel.pack_forget()
    newUserButton.pack_forget()
    returningUserButton.pack_forget()
    main_frame.pack_forget()
    
def show_landing_page(root, username):
    for widget in root.winfo_children():
        widget.destroy()
    home(root, username)

root = Tk()
root.title("Data Security Project")
root.configure(bg="black")
root.geometry("600x400")


main_frame = Frame(root, bg="black")
main_frame.pack(expand=True, fill="both")

askLabel = Label(main_frame, text="Are you a new user or returning user?", 
                fg="green", bg="black", font=("Arial", 14, "bold"))
newUserButton = Button(main_frame, text="New User", padx=30, pady=15, 
                      command=show_create_account, bg="black", fg="green", 
                      font=("Arial", 12), borderwidth=2, relief="solid",
                      activebackground="green", activeforeground="black")
returningUserButton = Button(main_frame, text="Returning User", padx=30, pady=15, 
                           command=show_login, bg="black", fg="green", 
                           font=("Arial", 12), borderwidth=2, relief="solid",
                           activebackground="green", activeforeground="black")

show_main_menu()

root.mainloop()
