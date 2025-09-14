import questionary
from create_account import create_account
from display_menu import display_menu

print('Are you a new user or returning user?')

user_type = questionary.select(
    "Choose an option:",
    choices=["New User", "Returning User"]
).ask()

if user_type == "New User":
    print("Welcome, new user!")
    create_account()
else:
        #Todo: add login functionality here, verify username and password
    print("Welcome back!")
    temp_password = "thisistemp"
    #convert temp_password via aes encryption
    encrypted_password = aes_encrypt(temp_password)
    display_menu()
