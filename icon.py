import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

def main():
    app = QApplication(sys.argv)
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(current_dir, 'window_icon.ico')  # Ensure it's an .ico file
    
    if os.path.exists(icon_path):
        print(f"Icon Path: {icon_path}")
        app.setWindowIcon(QIcon(icon_path))
    else:
        print("Icon not found.")

    window = QMainWindow()
    window.setWindowTitle("Main Window")
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()