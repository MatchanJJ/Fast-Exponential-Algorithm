import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QScrollArea
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
        self.third_row()
        
        master_layout.addLayout(self.row_1)
        master_layout.addLayout(self.row_2)
        master_layout.addLayout(self.row_3)
        master_layout.setContentsMargins(0,50,0,0)
        master_layout.setSpacing(15)
        
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
        widget.setMinimumHeight(85)
        widget_layout = QHBoxLayout(widget)
        
        widget.setObjectName("Widget")
        widget.setStyleSheet("#Widget {background-color: #313744; border: 0; border-radius: 15px}")
        
        #init objects to do
        label_title = QLabel("Input")
        label_base = QLabel("Base = 2")
        
        label_title.setStyleSheet(f'font-size: 20px; font-family:"{self.poppins}", sans-serif; color: #FFFFFF; font-weight: bold;')
        label_base.setStyleSheet(f'font-size: 14px; font-family:"{self.poppins}", sans-serif; color: #FFFFFF; font-weight: bold;')
        
        v = QVBoxLayout()
        v.addWidget(label_title)
        v.addWidget(label_base)
        
        v.setSpacing(4)
        
        start_input = ct.InputBox("Start Exponent")
        end_input = ct.InputBox("End Exponent")
        step_input = ct.InputBox("Step")
        
        h = QHBoxLayout()
        h.addWidget(start_input)
        h.addWidget(end_input)
        h.addWidget(step_input)
        
        widget_layout.addLayout(v)
        widget_layout.addLayout(h)
        
        widget_layout.addStretch(1)
        widget_layout.setSpacing(35)
        widget_layout.setContentsMargins(25,0,25,0)
        
        self.row_2.addWidget(widget)
    
    def third_row(self):
        widget = QWidget()
        widget_layout = QHBoxLayout(widget)
        widget.setObjectName("Widget")
        
        #add to scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(widget)
        scroll.setFixedWidth(1200)
        scroll.setMinimumHeight(475)
        
        scroll.setObjectName("Scroll")
        scroll.setStyleSheet("#Scroll, #Widget {background-color: #313744; border: 0; border-radius: 15px}")
        scroll.setContentsMargins(0,0,0,0)
        
        widget_layout.setContentsMargins(0,0,0,0)
        self.row_3.addWidget(scroll)
        
def main():
    app = QApplication([])
    window = SimulationWindow()
    window.show()
    app.exec_()
    
if __name__ == "__main__":
    main()