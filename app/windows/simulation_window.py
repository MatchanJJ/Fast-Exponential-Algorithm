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
        
        #stylesheets
        self.setObjectName("MainWidget")
        self.setStyleSheet('#MainWidget {background-color: #141920; border: 2px solid #333; border-radius: 15px;}')
        
        #layout
        master_layout = QVBoxLayout()
        master_layout.setAlignment(Qt.AlignCenter)
        
        # initialize rows
        self.row_1 = QHBoxLayout()        
        self.row_2 = QHBoxLayout()
        self.row_3 = QHBoxLayout()
        
        #add ui components
        self.first_row()
        self.second_row()
        
        master_layout.addLayout(self.row_1)
        master_layout.addLayout(self.row_2)
        master_layout.addLayout(self.row_3)
        
        self.setLayout(master_layout)
        
    def first_row(self):
        widget = QWidget()
        widget.setFixedWidth(1200)
        # add layout for the widget
        widget_layout = QHBoxLayout(widget)
        
        #init objects
        back_btn = ct.BackButton()
        stop_btn = ct.StopButton()
        play_btn = ct.PlayButton()
        
        btn_row = QHBoxLayout()
        btn_row.addWidget(stop_btn)
        btn_row.addWidget(play_btn)
        
        spacer = QSpacerItem(950, 0, QSizePolicy.Fixed, QSizePolicy.Expanding)
        
        widget_layout.addWidget(back_btn)
        widget_layout.addItem(spacer)
        widget_layout.addLayout(btn_row)
        
        self.row_1.addWidget(widget)
    
    def second_row(self):
        widget = QWidget()
        widget.setFixedWidth(1200)
        widget_layout = QHBoxLayout(widget)
        
        #init objects to do
    
    
        
def main():
    app = QApplication([])
    window = SimulationWindow()
    window.show()
    app.exec_()
    
if __name__ == "__main__":
    main()