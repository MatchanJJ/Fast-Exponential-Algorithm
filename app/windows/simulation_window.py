import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFontDatabase
import components.component as ct
import components.font_manager as fm

class SimulationWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simulation")
        self.resize(1280, 720)
        
        # stylesheets
        self.setObjectName("MainWidget")
        self.setStyleSheet('#MainWidget {background-color: #141920; border: 2px solid #333; border-radius: 15px;}')
        
        # get font
        self.poppins = fm.FontManager.get_poppins(16)
        
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

        master_layout.addStretch(1)
        
        self.setLayout(master_layout)
        
    def first_row(self):
        widget = QWidget()
        widget.setFixedWidth(1200)
        
        #widget.setObjectName("Widget")
        #widget.setStyleSheet("#Widget {background-color: #313744; border: 0; border-radius: 30px}")
        
        # add layout for the widget
        widget_layout = QHBoxLayout(widget)
        widget_layout.setContentsMargins(0, 0, 0, 0)
        
        #init objects
        back_btn = ct.BackButton()
        stop_btn = ct.StopButton()
        play_btn = ct.PlayButton()  
        
        btn_row = QHBoxLayout()
        btn_row.addWidget(stop_btn)
        btn_row.addWidget(play_btn)
        
        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        
        widget_layout.addWidget(back_btn)
        widget_layout.addItem(spacer)
        widget_layout.addLayout(btn_row)
        
        self.row_1.addWidget(widget)
    
    def second_row(self):
        widget = QWidget()
        widget.setFixedWidth(1200)
        widget.setMinimumHeight(100)
        
        widget_layout = QHBoxLayout(widget)
        widget.setObjectName("Widget")
        widget.setStyleSheet("#Widget {background-color: #313744; border: 0; border-radius: 15px}")
        
        #init objects to do
        label_title = QLabel("Input")
        label_base = QLabel("Base = 2")
        
        label_title.setFont(self.poppins)
        
        v = QVBoxLayout()
        v.addWidget(label_title)
        v.addWidget(label_base)
        
        start_input = ct.InputBox()
        
        
        widget_layout.addLayout(v)
        widget_layout.addWidget(start_input)
        
        self.row_2.addWidget(widget)
    
    
        
def main():
    app = QApplication([])
    window = SimulationWindow()
    window.show()
    app.exec_()
    
if __name__ == "__main__":
    main()