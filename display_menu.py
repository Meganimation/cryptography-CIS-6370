
import questionary
# //import bcrypt.txt from encryption_topics directory

# 1. Symmetric Encryption  - AES (Advanced Encryption Standard)  - DES (Data Encryption Standard)  - 3DES (Triple DES)  - Blowfish, Twofish

# 2. Asymmetric Encryption (Public-Key)  - RSA (Rivest–Shamir–Adleman)  - ECC (Elliptic Curve Cryptography)  - DSA (Digital Signature Algorithm)  - ElGamal

# 3. Hash Functions (for integrity, not true encryption)  - SHA-256, SHA-3  - MD5 (not recommended for security)  - bcrypt, scrypt, Argon2 (for password hashing)
def encryption_topics():
            encryption_type = questionary.select(
            "Which topic would you like to learn about?",
            choices=["bcrypt", "sha256", "RSA", "DSA"]
        ).ask()
            if encryption_type == "bcrypt":
                    with open("encryption_topics/bcrypt.txt", "r") as file:
                            content = file.read()
                            print(content)
            elif encryption_type == "sha256":
                print("SHA-256 (Secure Hash Algorithm 256-bit) is a cryptographic hash function that produces a fixed-size 256-bit hash. It is widely used for data integrity verification but is not recommended for password hashing due to its speed and vulnerability to brute-force attacks. For secure password storage, consider using algorithms like bcrypt or Argon2.")
            elif encryption_type == "RSA":
                print("RSA (Rivest-Shamir-Adleman) is a widely used public-key cryptographic system that enables secure data transmission. It relies on the mathematical properties of large prime numbers and is commonly used for secure data exchange, digital signatures, and certificate generation. It is not typically used for password hashing but rather for encrypting data and establishing secure communication channels.")
            elif encryption_type == "DSA":
                print("DSA (Digital Signature Algorithm) is a federal standard for digital signatures, primarily used for authenticating the integrity and origin of digital messages. It is based on the mathematical properties of modular exponentiation and discrete logarithms, and is commonly used in various security protocols. DSA is not used for password hashing but rather for ensuring the authenticity of digital communications.")
            
            would_you_like_to_continue = questionary.select(
                "Would you like to learn about another topic or return to the main menu?",
                choices=["Learn about another topic", "Return to main menu"]
            ).ask()
            if would_you_like_to_continue == "Learn about another topic":
                encryption_topics()
            else:
                display_menu()

def display_menu():
    action = questionary.select(
        "What would you like to do?",
        choices=["Learn about Encryption", "Encrypt a Message", "Exit"]
    ).ask()

    if action == "Learn about Encryption":
        encryption_topics()
    elif action == "Encrypt a Message":
        print("Encrypt a Message functionality not yet implemented.")
    elif action == "Exit":
        print("Goodbye!")
        exit()