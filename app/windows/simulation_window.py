import os
import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFontDatabase, QIcon

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import components.component as ct

class SimulationWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simulation")
        self.resize(1280, 720)
        #objects
        self.back_btn = ct.BackButton()
        self.stop_btn = ct.StopButton()
        self.play_btn = ct.PlayButton()
        
        #stylesheets
        self.setObjectName("MainWidget")
        self.setStyleSheet('#MainWidget {background-color: #141920; border: 2px solid #333; border-radius: 15px;}')
        
        #layout
        master_layout = QVBoxLayout()
        master_layout.setAlignment(Qt.AlignCenter)
        
        # first row layout
        self.row_1 = QHBoxLayout()
        
        self.btn_row = QHBoxLayout()
        self.btn_row.addWidget(self.stop_btn)
        self.btn_row.addWidget(self.play_btn)
        
        spacer = QSpacerItem(900, 0, QSizePolicy.Fixed, QSizePolicy.Expanding)
        
        self.row_1.addWidget(self.back_btn)
        self.row_1.addItem(spacer)
        self.row_1.addLayout(self.btn_row)
        
        
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