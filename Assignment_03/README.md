How to install and run the AES encryption mini-program.

## Prerequisites

- Python 3.7 or higher installed

## About

This Project implements a secure message encryption and decryption system using the AES-256 algorithm in CBC mode. When a user wants to send an encrypted message, they enter their plaintext and choose a password. The script generates a random salt and uses PBKDF2, a password-based key derivation function, to create a strong 256-bit AES key from the password and salt. The plaintext is then encrypted with this key, and the resulting ciphertext, initialization vector (IV), and salt are encoded and displayed for sharing. This ensures that only someone with the correct password and the shared values can decrypt the message. It also contains a secret message left for you!

## Installation

1. (Recommended) Create a virtual environment:
   ```sh
   python -m venv .venv
   ```
2. Activate the virtual environment:
   - On macOS/Linux:
     ```sh
     source .venv/bin/activate
     ```
   - On Windows:
     ```sh
     .venv\\Scripts\\activate
     ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

To run the program:

```sh
python3 aes_encrypt.py
```

If you get an error that 'python3' is not found, try using 'python' instead:

```sh
python aes_encrypt.py
```

If neither command works or you see a version lower than Python 3 when running `python --version`, you need to install Python 3 from https://www.python.org/downloads/.
