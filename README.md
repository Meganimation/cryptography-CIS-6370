How to install and run this project

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
