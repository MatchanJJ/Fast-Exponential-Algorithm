
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QLabel, QHBoxLayout, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
import os
import components.font_manager as fm
from PyQt5.QtCore import Qt
from PyQt5.QtSvg import QSvgWidget
         
class BackButton(QPushButton):

    def __init__(self, parent=None,):
        super().__init__("Back", parent)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.normpath(os.path.join(current_dir, '..', '..', 'icons', 'arrow_left.svg'))
        self.setIcon(QIcon(icon_path))
        
        # set font
        self.poppins = fm.FontManager.get_poppins(16)
        
        self.setFixedHeight(40)
        self.setStyleSheet(f"""
                            QPushButton {{
                                background-color: #2a2f3c;
                                border: none;
                                border-radius: 20px;
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
        
        self.setFixedSize(40,40)
        self.setStyleSheet("""
                            QPushButton {
                                background-color: #C3330A;
                                border: 0;
                                border-radius: 20px;
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
        
        self.setFixedSize(120, 40)
        self.setStyleSheet(f"""
                            QPushButton {{
                                background-color: #07C08E;
                                border: 0;
                                border-radius: 20px;
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
        
        self.poppins = fm.FontManager.get_poppins(16)
        
        self.text_field = QLineEdit()
        self.text_field.setFixedWidth(150)
        self.text_field.setFixedHeight(40)
        
        self.label = QLabel(text)
        self.label.setMinimumWidth(10)
        self.label.setMaximumWidth(150)
        self.label.setFixedHeight(40)
        
        self.label.setStyleSheet(f'font-size: 18px; font-family:"{self.poppins}", sans-serif; color: #FFFFFF;')
        self.text_field.setStyleSheet(f"""
                            QLineEdit {{
                                background-color: #1E232D;
                                border: 0;
                                border-radius: 9px;
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
        
    def get_input(self):
        user_input = self.text_field.text()
        return user_input
    
class NoDataFound(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedSize(1150, 570)

        # Create the inner content widget
        content_widget = QWidget()
        content_widget.setFixedSize(1149, 540)
        content_widget.setStyleSheet("background-color: #272b34; border-radius: 3px")

        # SVG, labels, and layout inside content_widget
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 80, 0, 0)
        layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        # SVG loading
        current_dir = os.path.dirname(os.path.abspath(__file__))
        svg_path = os.path.normpath(os.path.join(current_dir, '..', '..', 'icons', 'empty_state_no_data.svg'))

        svg = QSvgWidget(svg_path)
        svg.setFixedSize(235, 196)

        # Labels
        label_1 = QLabel("No Data")
        label_2 = QLabel("There is no data to show right now")

        try:
            from font_manager import FontManager  # Your module
            self.poppins = FontManager.get_poppins(16)
            font_family = self.poppins
        except:
            font_family = "Arial"

        label_1.setStyleSheet(f"color: #656C75; font-family: '{font_family}'; font-size: 20px;")
        label_2.setStyleSheet(f"color: #656C75; font-family: '{font_family}'; font-size: 16px;")
        label_1.setAlignment(Qt.AlignHCenter)
        label_2.setAlignment(Qt.AlignHCenter)

        # Assemble layout
        layout.addWidget(svg)
        layout.addWidget(label_1)
        layout.addWidget(label_2)
        content_widget.setLayout(layout)

        # Add to wrapper layout
        wrapper_layout = QHBoxLayout()
        wrapper_layout.setContentsMargins(0, 0, 0, 0)
        wrapper_layout.addWidget(content_widget)
        self.setLayout(wrapper_layout)
        
        
def main():
    app = QApplication([])
    window = NoDataFound()
    window.show()
    app.exec_()
    
if __name__ == "__main__":
    main()
        
        
        