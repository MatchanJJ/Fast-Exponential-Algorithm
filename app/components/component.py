
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon
import os

class BackButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__("Back", parent)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.normpath(os.path.join(current_dir, '..', '..', 'icons', 'arrow_left.svg'))
        self.setIcon(QIcon(icon_path))
        
        self.setFixedHeight(50)
        self.setStyleSheet("""
                            QPushButton {
                                background-color: #2a2f3c;
                                border: none;
                                border-radius: 24px;
                                padding: 10px 20px;
                                
                                color: white;
                                font-size: 20px;
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
        
        self.setFixedSize(46,46)
        self.setStyleSheet("""
                            QPushButton {
                                background-color: #C3330A;
                                border: 0;
                                border-radius: 23px;
                                padding: 10px 20px;
                            }
                            
                            QPushButton:hover {
                                background-color: #e93d0b;
                            }
                            
                            QPushButton:pressed {
                                background-color: #ff520c;
                            }
                        """)
    
class PlayButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__("PLAY", parent)
        
        self.setFixedHeight(46)
        self.setStyleSheet("""
                            QPushButton {
                                background-color: #07C08E;
                                border: 0;
                                border-radius: 23px;
                                padding: 10px 24px;
                                
                                color: white;
                                font-size: 16px;
                            }
                            
                            QPushButton:hover {
                                background-color: #08e6aa;
                            }
                            
                            QPushButton:pressed {
                                background-color: #08ffcc;
                            }
                        """)