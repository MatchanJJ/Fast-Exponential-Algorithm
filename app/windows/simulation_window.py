import os
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFontDatabase, QIcon

class SimulationWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simulation")
        self.resize(1280, 720)
        #objects
        self.back_btn = QPushButton("Back")
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.normpath(os.path.join(current_dir, '..', '..', 'icons', 'arrow_left.svg'))

        self.back_btn.setIcon(QIcon(icon_path))
        
        #stylesheets11
        
        #layout
        master_layout = QVBoxLayout()
        master_layout.setAlignment(Qt.AlignCenter)
        
        self.row_1 = QHBoxLayout()
        self.row_1.addWidget(self.back_btn)
        
        self.row_2 = QHBoxLayout()
        self.row_3 = QHBoxLayout()
        
        master_layout.addLayout(self.row_1)
        master_layout.addLayout(self.row_2)
        master_layout.addLayout(self.row_3)
        
        self.setLayout(master_layout)
        
def main():
    app = QApplication([])
    window = SimulationWindow()
    window.show()
    app.exec_()
    
if __name__ == "__main__":
    main()