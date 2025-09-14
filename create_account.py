import questionary
import bcrypt
import hashlib
import getpass

def create_account(username="", passwordVisibility=None):

    if username == "":
        new_username = input("Please enter your desired username: ")
    else:
        new_username = username

    passwordVisibility = passwordVisibility if passwordVisibility is not None else questionary.select(
        f"Hi {new_username}! Before we ask you to enter your password, would you like to view your password while typing it?",
        choices=["Yes", "No, hide it"]
    ).ask()

    new_password = passwordVisibility == "Yes" and input("Please enter your new password: ") or getpass.getpass("Please enter your new password: ")
    
    #if password is less than 8 characters, ask them to enter a new password
    while len(new_password) < 8:
        print("Hey! This is a project about data security and encryption! Your password can't be too short because it helps protect your account from brute-force attacks. Please choose a password at least 8 characters long.")
        new_password = passwordVisibility == "Yes" and input("Please enter your new password: ") or getpass.getpass("Please enter your new password: ")

    confirm_password = passwordVisibility == "Yes" and input("Please confirm your new password: ") or getpass.getpass("Please confirm your new password: ")

    if new_password != confirm_password:
        print("Passwords do not match. Please try again.")
        return create_account(new_username, passwordVisibility)
    choice = questionary.select(
        f"How would you like to encrypt your password?",
        choices=["bcrypt (recommended)", "sha256"]
    ).ask()

    if choice == "bcrypt (recommended)":
        hashed = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        print(f"Your bcrypt hashed password is {hashed.decode('utf-8')}")
    elif choice == "sha256":
        hashed_sha256 = hashlib.sha256(new_password.encode('utf-8')).hexdigest()
        print(f"Your sha256 hashed password is {hashed_sha256}")
