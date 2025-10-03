How to install and run the AES encryption mini-program.

## Prerequisites

- Python 3.7 or higher installed

## About

This app is a high-security feature which allows you to implement the Elgamal Encryption and store a message which is (hopefully) impossible to descript without knowing the private key!

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
python3 elgamal_encrypt.py
```

If this is your first time using the program, you will be prompted to generate your keys. ONLY your public key and ciphertext should be stored. Your Private Key should not be stored in this repo so when you receive it please make sure it is copied! If you lose it, you will have to generate a new one.

If you get an error that 'python3' is not found, try using 'python' instead:

```sh
python elgamal_encrypt.py
```

If neither command works or you see a version lower than Python 3 when running `python --version`, you need to install Python 3 from https://www.python.org/downloads/.

## Notes and How I Would Improve 

This app should generate a JSON file upon your first public key generation. If that doesn't occurr then something went wrong. 
I didn't add many error handlers for when the users enters a particular edgecase, so my main revision would be there. 
I also would enhance the application to store multiple messages, or create an app which verifies authenticity through a digital signature.
