
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon
import os

class BackButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__("Back", parent)

        current_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.normpath(os.path.join(current_dir, '..', '..', 'icons', 'arrow_left.svg'))
        self.setIcon(QIcon(icon_path))
        
        self.setStyleSheet("""
                            QPushButton {
                                background-color: #2a2f3c;
                                color: white;
                                font-size: 24px;
                                border: none;
                                border-radius: 24px;
                                padding: 10px 20px;
                            }
                            
                            QPushButton:hover {
                                background-color: #3C4455;
                                color: 
                            }
                            
                            QPushButton:pressed {
                                background-color: #505A6F;
                            }
                            """)
        
class StopButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__("", parent)
        
        self.styleSheet("""
                            QPushButton {
                                background-color: #C3330A;
                                border: none;
                                border-radius: 24px;
                                padding: 10px 20px;
                            }
                            
                            QPushButton:hover {
                                background-color: #3C4455;
                                color: 
                            }
                            
                            QPushButton:pressed {
                                background-color: #505A6F;
                            }
                        """)
    
class PlayButton(QPushButton):
    print