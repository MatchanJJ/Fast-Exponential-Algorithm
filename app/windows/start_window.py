import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon
import components.font_manager as fm

class StartWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Algorithm Simulation")
        self.setMinimumSize(1080, 350)
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        icon = os.path.normpath(os.path.join(current_dir, '..', '..', 'icons', 'window_icon.png'))
        self.setWindowIcon(QIcon(icon))
        
        #create objects
        self.label_1 = QLabel("Fast-Expo vs Naive", self)
        self.label_2 = QLabel("Implementing the Fast-Expo Algorithm", self)
        
        self.start_button = QPushButton("start", self)
        
        #stylesheets
        ibm = fm.FontManager.get_ibm_plex(16)
        poppins = fm.FontManager.get_poppins(16)
        
        self.setObjectName("MainWidget")        
        self.setStyleSheet('#MainWidget {background-color: #141920; border: 2px solid #333; border-radius: 15px;}')
        
        self.label_1.setStyleSheet(f'font-size: 64px; font-family:"{poppins}", sans-serif; color: #FFFFFF; font-weight: bold ')
        self.label_2.setStyleSheet(f'font-size: 30px; font-family:"{ibm}", monospace; color: #C7CBD7;')
        
        self.start_button.setStyleSheet("""
                                    QPushButton {
                                        background-color: #07C08E;
                                        color: white;
                                        font-size: 20px;
                                        border: none;
                                        border-radius: 18px;
                                        padding: 10px 20px;
                                        font-weight: bold;
                                    }
                                    
                                    QPushButton:hover {
                                        background-color: #08e6aa;
                                    }
                                    
                                    QPushButton:pressed {
                                        background-color: #08ffcc;
                                    }
                                    """)
        
        self.label_1.setFixedHeight(64)
        self.label_2.setFixedHeight(64)
        self.label_2.setAlignment(Qt.AlignCenter)
        
        #Layout
        master_layout = QVBoxLayout()
        master_layout.setAlignment(Qt.AlignCenter)
        
        master_layout.addWidget(self.label_1)
        master_layout.addWidget(self.label_2)
        master_layout.addWidget(self.start_button)
        
        self.setLayout(master_layout) 
                
def main():
    app = QApplication([])
    
    window = StartWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()