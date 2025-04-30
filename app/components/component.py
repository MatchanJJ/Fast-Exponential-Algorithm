
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QHBoxLayout, QWidget
from PyQt5.QtGui import QIcon
import os
import components.font_manager as fm
         


class BackButton(QPushButton):

    def __init__(self, parent=None,):
        super().__init__("Back", parent)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.normpath(os.path.join(current_dir, '..', '..', 'icons', 'arrow_left.svg'))
        self.setIcon(QIcon(icon_path))
        
        # set font
        self.poppins = fm.FontManager.get_poppins(16)
        
        self.setFixedHeight(50)
        self.setStyleSheet(f"""
                            QPushButton {{
                                background-color: #2a2f3c;
                                border: none;
                                border-radius: 24px;
                                padding: 10px 20px;
                                
                                color: white;
                                font-family:'{self.poppins}';
                                font-size: 16px;
                                font-weight: bold;
                            }}
                            
                            QPushButton:hover {{
                                background-color: #3C4455;
                            }}
                            
                            QPushButton:pressed {{
                                background-color: #505A6F;
                            }}
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
        
        self.poppins = fm.FontManager.get_poppins(16)
        
        self.setFixedSize(90, 46)
        self.setStyleSheet(f"""
                            QPushButton {{
                                background-color: #07C08E;
                                border: 0;
                                border-radius: 23px;
                                padding: 10px 24px;
                                
                                color: white;
                                font-family:'{self.poppins}';
                                font-size: 16px;
                                font-weight: bold;
                            }}
                            
                            QPushButton:hover {{
                                background-color: #08e6aa;
                            }}
                            
                            QPushButton:pressed {{
                                background-color: #08ffcc;
                            }}
                        """)

class InputBox(QWidget):
    
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.setMaximumWidth(320)
        self.setMinimumWidth(100)
        self.setStyleSheet("#QWidget {background-color: #f1a335}")
        
        print(self.styleSheet())
        
        self.poppins = fm.FontManager.get_poppins(16)
        
        self.text_field = QLineEdit()
        self.text_field.setFixedWidth(150)
        self.text_field.setFixedHeight(46)
        
        self.label = QLabel(text)
        self.label.setMinimumWidth(10)
        self.label.setMaximumWidth(150)
        self.label.setFixedHeight(46)
        
        self.label.setStyleSheet(f'font-size: 18px; font-family:"{self.poppins}", sans-serif; color: #FFFFFF;')
        self.text_field.setStyleSheet(f"""
                            QLineEdit {{
                                background-color: #1E232D;
                                border: 0;
                                border-radius: 18px;
                                padding: 1px 4px;
                                
                                color: white;
                                font-family:'{self.poppins}';
                                font-size: 15px;
                            }}
                            """)
        
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,1,0)
        layout.setSpacing(10)
        
        layout.addWidget(self.label)
        layout.addWidget(self.text_field)
        
        self.setLayout(layout)
        
        