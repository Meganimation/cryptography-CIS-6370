from tkinter import *
from create_account import attempt_to_create_account
from login import attempt_to_login
from home import home

# Global variables to hold different frames
main_frame = None
create_account_frame = None
login_frame = None
landing_frame = None

def hide_all_frames():
    """Hide all frames"""
    frames = [main_frame, create_account_frame, login_frame, landing_frame]
    for frame in frames:
        if frame and frame.winfo_exists():
            frame.pack_forget()

def show_main_menu():
    """Show the main menu frame"""
    hide_all_frames()
    main_frame.pack(expand=True, fill="both")

def show_create_account():
    """Show the create account page"""
    hide_all_frames()
    # Create frame if it doesn't exist
    global create_account_frame
    if not create_account_frame or not create_account_frame.winfo_exists():
        create_account_frame = Frame(root, bg="black")
    create_account_frame.pack(expand=True, fill="both")
    attempt_to_create_account(create_account_frame, show_main_menu)
    
def show_login():
    """Show the login page"""
    print("Login functionality to be implemented.")
    hide_all_frames()
    # Create frame if it doesn't exist
    global login_frame
    if not login_frame or not login_frame.winfo_exists():
        login_frame = Frame(root, bg="black")
    login_frame.pack(expand=True, fill="both")
    attempt_to_login(login_frame, show_main_menu, show_landing_page)
    
def show_landing_page(root, username):
    """Show the landing page"""
    hide_all_frames()
    global landing_frame
    if landing_frame and landing_frame.winfo_exists():
        landing_frame.destroy()
    landing_frame = Frame(root, bg="black")
    landing_frame.pack(expand=True, fill="both")
    home(landing_frame, username)

root = Tk()
root.title("Data Security Project")
root.configure(bg="black")
root.geometry("600x400")

# Create the main menu frame with persistent widgets
main_frame = Frame(root, bg="black")

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

# Pack the widgets in the main frame
askLabel.pack(pady=(50, 30))
newUserButton.pack(pady=10)
returningUserButton.pack(pady=10)

# Show the main menu initially
show_main_menu()

root.mainloop()
