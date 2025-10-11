How to install and run this project

## About

This is a data encryption program that can be accessed by main users. You can create an account and your password will be safely stored via hashing using the bcrypt package.

Once logged in, you will be able to see a list of currently stored files, as well as having the ability to upload your own, which will use hybrid encryption scheme via AES and RSA to encrypt your file. Each file will then generate its own independent private key via RSA algorithm using the pycryptodome package - You must copy this to your clipboard and save the key. Without it you can no longer decrypt the file!

If you forget the key, your only other option is to delete the file. To do this, you can enter the same password you used to log in with.

I guess a good potential use case of this would be maybe using it as a way to safely store files and share them amongst peers by sharing the private key with them.

I created an account and uploaded a file. This time I won't provide the passwords and hopefully you shouldn't be able to access them

Some updates I would make if I had more time:

-Add error handling
-Add helper texts to inputs
-Prevevent account name from being case sensitive
-Add more edgecase handling (for example, preventing account names from being too long or short)
-Adding more encryption options like size amounts and other hashing options
-Allowing files to be renamed
-Better UI

## Prerequisites

- Python 3.7 or higher installed

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

Make sure you're in the gui file

```sh
  cd gui
```

```sh
python3 main.py
```

If you get an error that 'python3' is not found, try using 'python' instead:

```sh
python main.py
```

If neither command works or you see a version lower than Python 3 when running `python --version`, you need to install Python 3 from https://www.python.org/downloads/.

## Notes

- Do not include the `.venv` folder when sharing your project. Each user should create their own virtual environment.
- If you need additional dependencies, add them to `requirements.txt`.
