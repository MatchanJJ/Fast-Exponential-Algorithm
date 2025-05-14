import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PyQt5.QtWidgets import QApplication
from app.app_controller import AppController
from PyQt5.QtGui import QIcon

def main():
    app = QApplication(sys.argv)
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(current_dir, '..', '..', 'icons', 'window_icon.png')
    app.setWindowIcon(QIcon(icon_path)) 
        
    controller = AppController()
    controller.run()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
