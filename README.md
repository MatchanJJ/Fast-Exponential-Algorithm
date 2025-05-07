# Compare Exponentiation Methods
source ~/python_venv/bin/activate
This project compares two methods of exponentiation: the **naive method** and **fast exponentiation (exponentiation by squaring)**. The program measures execution time for both methods and calculates a speedup factor.

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

## Running the Script

1. **Clone or Download the Project:**
   ```sh
   git clone https://github.com/MatchanJJ/Fast-Exponential-Algorithm
   cd Fast-Exponential-Algorithm
   ```
   *(Alternatively, you can manually download the file to your desired directory.)*

2. **Run the Python File:**
   ```sh
   python fast-expo.py
   ```
   *(Use `python3` instead of `python` if needed.)*

3. **Choose Input Type:**
   - Enter `1` to manually input a base and exponent.
   - Enter `2` to use randomly generated values.

4. **View Results:**
   - The script will display the execution time for both methods and the speedup factor.

## Example Output
```
Choose input type: (1) Manual (2) Random: 2
Generated Base: 5, Exponent: 230
Base: 5, Exponent: 230
Naive Method Time: 0.002345 seconds
Fast Exponentiation Time: 0.000012 seconds
Fast Exponentiation is 195.42x faster.
```

Install dependencies

python -m venv .venv
source .venv/bin/activate  # or `.venv\Scripts\activate` on Windows
pip install -r requirements.txt
