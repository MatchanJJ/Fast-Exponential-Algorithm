import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSpacerItem, QToolButton
import components.component as ct
import components.font_manager as fm
from PyQt5.QtGui import QIcon, QFont

class MenuWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu")
        self.setMinimumSize(1280,820)
        self.setObjectName("MainWidget")
        self.setStyleSheet('#MainWidget {background-color: #141920; border: 2px solid #333; border-radius: 15px;}')
        
        self.poppins = fm.FontManager.get_poppins(16)
        
        
        
        # config
        self.border_radius = 20
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.left_icon = os.path.normpath(os.path.join(current_dir, '..', '..', 'icons', 'visualization_icon.svg'))
        self.right_icon = os.path.normpath(os.path.join(current_dir, '..', '..', 'icons', 'simulation_icon.svg'))
        
        icon = os.path.normpath(os.path.join(current_dir, '..', '..', 'icons', 'window_icon.png'))
        self.setWindowIcon(QIcon(icon))
        
        # set font
        self.poppins = fm.FontManager.get_poppins(16)
        self.btn_stylesheet = """
            QToolButton {
                padding-top: 150px; 
                padding-bottom: 200px;
                border: 0;
                background-color: #2E3441;
                border-radius: 15px;
                text-align: center;
                
                color: white;
                font-size: 20px;
                font-weight: bold;
            }
            QToolButton:hover {
                background-color: #03BF8D;
            }
        """
        self.btn_size = QSize(290, 290)
        
        self.setup_ui()
        
    def setup_ui(self):
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(25)
        
        # Add buttons to the layout
        layout.addWidget(self.left_button())
        layout.addWidget(self.right_button())

        # Set layout to the main window
        self.setLayout(layout)
        
    def left_button(self):
        self.left_btn = QToolButton()
        self.left_btn.setText("Fast-Expo Visualization")
        
        self.left_btn.setIcon(QIcon(self.left_icon))
        self.left_btn.setIconSize(self.btn_size)
        
        self.left_btn.setFixedSize(555, 725)
        
        self.left_btn.setStyleSheet(self.btn_stylesheet)
        self.left_btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  # icon on top, text at bottom
        return self.left_btn

    def right_button(self):
        self.right_btn = QToolButton()
        self.right_btn.setText("Analyze Time Complexity")
        
        self.right_btn.setIcon(QIcon(self.right_icon))
        self.right_btn.setIconSize(self.btn_size)
        
        self.right_btn.setFixedSize(555, 725)
        
        self.right_btn.setStyleSheet(self.btn_stylesheet)
        self.right_btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        return self.right_btn
    
def main():
    app = QApplication([])
    window = MenuWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()