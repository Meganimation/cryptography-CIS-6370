from Crypto.Random import random
from Crypto.Util.number import getPrime, inverse
from Crypto.PublicKey import ElGamal
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import questionary
import json
import os
import pyperclip

KEY_FILE = "elgamal_keys.json"

def generate_keys():
    userInput = questionary.select("Please choose a key size for your new encryption (larger sizes are more secure but slower):",choices=["125", "256", "512"]).ask()
    userInputAsInt = int(userInput)
    keys = elgamal_keygen(userInputAsInt)
    public_key = {'p': keys['p'], 'g': keys['g'], 'y': keys['y']}
    private_key = {'x': keys['x']}
    print("Generated new public key.")
    save_data(public_key, None)  # Clear previous ciphertext
    pyperclip.copy(str(private_key['x']))
    askToView = questionary.select("Your private key has been copied to your clipboard. Would you like to view it here as well?", choices=["Yes", "No"]).ask()
    if askToView == "Yes":
        print ('********************************')
        print("Your private key is:", private_key['x'])
        print ('********************************')
        print("Remember to save it somewhere safe as this is the only time you'll see it!")
    if askToView == "No":
        print("Okay, just remember to save it somewhere safe while it's copied!")


def save_data(public_key, ciphertext):
    with open(KEY_FILE, "w") as f:
        json.dump({"public_key": public_key, "ciphertext": ciphertext}, f)


def load_data():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "r") as f:
            data = json.load(f)
            return data.get("public_key"), data.get("ciphertext")
    return None, None

# ElGamal key generation
def elgamal_keygen(bits=256):
    p = getPrime(bits)
    g = random.randint(2, p - 2)
    x = random.randint(2, p - 2)  # Private key
    y = pow(g, x, p)              # Public key
    return {'p': p, 'g': g, 'x': x, 'y': y}

# ElGamal encryption
def elgamal_encrypt(m, public_key):
    p, g, y = public_key['p'], public_key['g'], public_key['y']
    k = random.randint(2, p - 2)
    a = pow(g, k, p)
    b = (m * pow(y, k, p)) % p
    return {'a': a, 'b': b}

# ElGamal decryption
def elgamal_decrypt(ciphertext, private_key, public_key):
    p, x = public_key['p'], private_key['x']
    a, b = ciphertext['a'], ciphertext['b']
    s = pow(a, x, p)
    m = (b * inverse(s, p)) % p
    return m

def main():
    while True:
        public_key, ciphertext = load_data()
        private_key = None
        if public_key is None:
            generate_keys()
            public_key, ciphertext = load_data()

        choice = questionary.select("What would you like to do?", choices=["Encrypt", "Decrypt", os.path.exists(KEY_FILE) and "Generate New Private Key", "View Public Key", "View Ciphertext", "View Private Key", "Exit"]).ask()
        if choice == 'Encrypt':
            if public_key:
                print("Please be aware that encrypting a new string will overwrite the previous ciphertext stored in the file.")
            string = input("Enter a string to encrypt: ")
            message = int.from_bytes(string.encode(), 'big')
            print("Your Plaintext is:", string) 
            print("Converting to integers, which is:", message)

            # Encrypt
            ciphertext = elgamal_encrypt(message, public_key)
            save_data(public_key, ciphertext)
            print("New message encrypted! Remember to use your private key to decrypt it.")

        elif choice == 'Decrypt':
            x = int(input("Enter your private key: "))
            private_key = {'x': x}
            if ciphertext is None:
                print("No ciphertext found in file. Please encrypt a message first!")
                continue
            decrypted = elgamal_decrypt(ciphertext, private_key, public_key)
            print("Decrypted message (as integer):", decrypted)
            byte_length = (decrypted.bit_length() + 7) // 8
            try:
                decrypted_string = decrypted.to_bytes(byte_length, 'big').decode()
                print ('********************************')
                print("Decrypted message (as string):", decrypted_string)
                print ('********************************')
            except Exception as e:
                print("Error decoding decrypted message:", e)
        elif choice == 'Generate New Private Key':
            print ("Generating a new key pair will overwrite your existing keys and ciphertext.")
            confirm = questionary.select(
                "Are you sure you want to proceed?",
                choices=["Yes", "No"]
            ).ask()
            if confirm == "Yes":
                generate_keys()
        elif choice == 'View Public Key':
            print ('********************************')
            print("Public Key:", public_key)
            print ('********************************')
        elif choice == 'View Private Key':
            if private_key is None:
                print ('********************************')
                print("No private key found! That's good because it shouldn't be stored here. You need to enter it when decrypting. Did you forget it? (Tip: It might be copied to your clipboard!)")
                print ('********************************')
            else:
                print("If you're seeing this, something went terribly wrong as private_key shouldn't even exist!", private_key)
                print ('********************************')
        elif choice == 'View Ciphertext':
            if ciphertext is None:
                print ('********************************')
                print("No ciphertext found in file.")
                print ('********************************')
            else:
                print ('********************************')
                print("Ciphertext:", ciphertext)
                print ('********************************')
        elif choice == 'Exit':
            print("Goodbye!")
            break

main()
    


