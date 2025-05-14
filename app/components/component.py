import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QLabel, QHBoxLayout, QWidget, QVBoxLayout, QComboBox, QDialog
from PyQt5.QtGui import QIcon, QIntValidator
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
        
        self.setFixedHeight(45)
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
        super().__init__("Stop", parent)
        
        self.poppins = fm.FontManager.get_poppins(16)
        
        self.setFixedSize(110, 40)
        self.setStyleSheet(f"""
                            QPushButton {{
                                background-color: #443531;
                                border: 2 solid #C3330A;
                                border-radius: 18px;
                                padding: 10px 20px;
                                
                                color: white;
                                font-family:'{self.poppins}';
                                font-size: 15px;
                                font-weight: bold;
                            }}
                            
                            QPushButton:hover {{
                                background-color: #654F4A;
                                border: 2 solid #EB3E0D;
                            }}
                            
                            QPushButton:pressed {{
                                background-color: #82695F;
                                border: 2 solid #F34A1A;
                            }}
                        """)
    
class PlayButton(QPushButton):
    
    def __init__(self, parent=None):
        super().__init__("Play", parent)
        
        self.poppins = fm.FontManager.get_poppins(16)
        self.is_playing = False
        
        self.setFixedSize(110, 40)
        self.setStyleSheet(f"""
                            QPushButton {{
                                background-color: #2a4a3d;
                                border: 2 solid #03CD97;
                                border-radius: 18px;
                                padding: 10px 24px;
                                
                                color: white;
                                font-family:'{self.poppins}';
                                font-size: 15px;
                                font-weight: 500;
                            }}
                            
                            QPushButton:hover {{
                                background-color: #4B675C;
                                border: 2 solid #0AFABA;
                            }}
                            
                            QPushButton:pressed {{
                                background-color: #749A80;
                                border: 2 solid #11F0B4;
                            }}
                        """)
        
    def toggle_state(self):
        self.is_playing = not self.is_playing
        self.setText("Pause" if self.is_playing else "Play")

    def reset_state(self):
        self.setText("Start")

class InputBox(QWidget):
    
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.setMinimumWidth(100)
        self.setMaximumHeight(51)
        self.setStyleSheet("#QWidget {background-color: #f1a335}")
        
        self.poppins = fm.FontManager.get_poppins(16)
        
        # cant find fix to optimize big int values, limit to 5 digits.
        self.text_field = QLineEdit()
        self.text_field.setFixedWidth(140)
        self.text_field.setFixedHeight(30)
        self.text_field.setValidator(QIntValidator())
        self.text_field.setMaxLength(5)
        
        self.label = QLabel(text)
        self.label.setFixedWidth(150)
        self.label.setFixedHeight(18)
        
        self.label.setStyleSheet(f'font-size: 14px; font-family:"{self.poppins}", sans-serif; color: #FFFFFF; line-height: 1')
        self.text_field.setStyleSheet(f"""
                            QLineEdit {{
                                background-color: #1E232D;
                                border: 0;
                                border-radius: 2px;
                                padding: 2px 4px;
                                
                                color: white;
                                font-family:'{self.poppins}';
                                font-size: 14px;
                            }}
                            """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        
        layout.addWidget(self.label)
        layout.addWidget(self.text_field)
        
        self.setLayout(layout)
        
    def get_input(self):
        user_input = self.text_field.text()
        return user_input
    
    def clear(self):
        self.text_field.clear()
    
class ComboBox(QWidget):
    
    def __init__(self, text, items, parent=None):
        super().__init__(parent)
        self.setMaximumWidth(320)
        self.setMaximumHeight(51)
        self.setStyleSheet("#QWidget {background-color: #f1a335}")
        
        self.poppins = fm.FontManager.get_poppins(16)
        
        self.combo_box = QComboBox()
        self.combo_box.setFixedWidth(130)
        self.combo_box.setFixedHeight(30)

        # Add items dynamically
        self.combo_box.addItems(items)
        
        self.label = QLabel(text)
        self.label.setMaximumWidth(150)
        self.label.setFixedHeight(18)
        
        self.label.setStyleSheet(f'font-size: 14px; font-family:"{self.poppins}", sans-serif; color: #FFFFFF;')
        self.combo_box.setStyleSheet(f"""
                            QComboBox {{
                                background-color: #1E232D;
                                border: 0;
                                border-radius: 4px;
                                padding: 1px 4px;
                                
                                color: white;
                                font-family:'{self.poppins}';
                                font-size: 14px;
                            }}
                            QComboBox QAbstractItemView {{
                                background-color: #2A2F3A;
                                border: 1px solid #444;
                                color: white;
                                selection-background-color: #3A3F4B;
                                selection-color: white;
                                font-family: '{self.poppins}';
                            }}
                            """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 1, 0)
        layout.setSpacing(0)
        
        layout.addWidget(self.label)
        layout.addWidget(self.combo_box)
        
        self.setLayout(layout)
        
    def get_input(self):
        return self.combo_box.currentText()


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
        
        svg.setFixedSize(352, 294)

        # Labels
        label_1 = QLabel("No Data")
        label_2 = QLabel("There is no data to show right now")

        try:
            from font_manager import FontManager
            self.poppins = FontManager.get_poppins(16)
            font_family = self.poppins
        except:
            font_family = "Arial"

        label_1.setStyleSheet(f"color: #5D636C; font-family: '{font_family}'; font-size: 22px;")
        label_2.setStyleSheet(f"color: #5D636C; font-family: '{font_family}'; font-size: 18px;")
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
        
class CustomModal(QDialog):
    def __init__(self, message):
        super().__init__()
        self.setModal(True)  # Makes it modal
        self.setWindowTitle("Error Title")
        self.setFixedSize(352, 294)
        
        # Apply a stylesheet to the dialog
        self.setStyleSheet("""
            QDialog {
                background-color: #f0f0f0;
                border: 2px solid #ccc;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 14px;
                border: none;
                border-radius: 5px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

        layout = QVBoxLayout()
        label = QLabel(message)
        button = QPushButton("OK")
        button.clicked.connect(self.accept)

        layout.addWidget(label)
        layout.addWidget(button)
        self.setLayout(layout)
    
def main():
    app = QApplication([])
    window = CustomModal("rawr")
    window.exec_()
    app.exec_()
    
if __name__ == "__main__":
    main()
        
        
        