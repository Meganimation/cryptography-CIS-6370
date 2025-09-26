How to install and run the AES encryption mini-program.

## Prerequisites

- Python 3.7 or higher installed

## Installation

First, open the terminal and ensure you are in the /Assignment_01 directory

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
