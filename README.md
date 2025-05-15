# Implementing Fast-Expo Algorithm
This project implements the Fast-Expo Algorithm and compares two methods of exponentiation: the **naive method** and **fast exponentiation (exponentiation by squaring)**. The program graphs the operation time or run time of both algorithm. A visualization of the Fast-Expo Algorithm is also available. 

## Installation

### Windows
1. Download Python from the official website:
   - Visit [https://www.python.org/downloads/](https://www.python.org/downloads/)
   - Select the latest version for Windows and download the installer.
   - Run the installer and check **"Add Python to PATH"** before proceeding.
   - Click **Install Now** and wait for the installation to complete.

2. Verify the installation:
   - Open Command Prompt (`cmd`) and run:
     ```sh
     python --version
     ```
   - If Python is installed correctly, it will display the installed version.

### Mac/Linux
1. Open the terminal and install Python using the following commands:
   - **For macOS:**
     ```sh
     brew install python
     ```
   - **For Linux (Debian-based distributions):**
     ```sh
     sudo apt update && sudo apt install python3
     ```

2. Verify the installation:
   ```sh
   python3 --version
   ```

## Install dependencies and create venv
   ```
   python -m venv .venv
   source .venv/bin/activate  # or `.venv\Scripts\activate` on Windows
   pip install -r requirements.txt
   ```

## Running the Script

1. **Clone or Download the Project:**
   ```sh
   git clone https://github.com/MatchanJJ/Fast-Exponential-Algorithm
   cd Fast-Exponential-Algorithm
   ```
   *(Alternatively, you can manually download the file to your desired directory.)*

2. **Run the Python File:**
   ```sh
   python app/main.py
   ```
   *(Use `python3` instead of `python` if needed.)*
   
This project was created for course code CS6: Algorithm And Complexity as a Final Project. 
-robroi

