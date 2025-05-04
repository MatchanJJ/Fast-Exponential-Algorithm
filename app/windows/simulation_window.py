import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QScrollArea
from PyQt5.QtGui import QFontDatabase
import components.component as ct
import components.font_manager as fm
import components.graph as graph

class SimulationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simulation")
        self.resize(1280, 820)

        self.setObjectName("MainWidget")
        self.setStyleSheet('#MainWidget {background-color: #141920; border: 2px solid #333; border-radius: 15px;}')

        self.poppins = fm.FontManager.get_poppins(16)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 50, 0, 0)
        layout.setSpacing(15)

        layout.addLayout(self.create_top_bar())
        layout.addLayout(self.create_input_section())
        layout.addLayout(self.create_graph_area())
        layout.addStretch(1)

        self.setLayout(layout)

    def create_top_bar(self):
        row = QHBoxLayout()
        widget = self.wrap_widget(QHBoxLayout(), fixed_width=1200)

        back_btn = ct.BackButton()
        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        widget.layout().addWidget(back_btn)
        widget.layout().addItem(spacer)

        row.addWidget(widget)
        return row

    def create_input_section(self):
        row = QHBoxLayout()
        layout = QHBoxLayout()
        widget = self.wrap_widget(layout, fixed_width=1200, min_height=85, object_name="Widget",
                                  stylesheet="#Widget {background-color: #313744; border: 0; border-radius: 4px}")

        label_title = self.styled_label("Input", 20)
        label_base = self.styled_label("Base = 2", 14)
        
        input_layout = QHBoxLayout()
        input_layout.addWidget(ct.InputBox("Start Exponent"))
        input_layout.addWidget(ct.InputBox("End Exponent"))
        input_layout.addWidget(ct.InputBox("Step"))

        buttons = QHBoxLayout()
        buttons.addWidget(ct.StopButton())
        buttons.addWidget(ct.PlayButton())

        label_col = QVBoxLayout()
        label_col.addWidget(label_title)
        label_col.addWidget(label_base)
        label_col.setSpacing(4)

        layout.addLayout(label_col)
        layout.addLayout(input_layout)
        layout.addLayout(buttons)
        layout.addStretch(1)
        layout.setSpacing(35)
        layout.setContentsMargins(25, 0, 25, 0)

        row.addWidget(widget)
        return row

    def create_graph_area(self):
        # to fix
        row = QHBoxLayout()

        graph_widget = graph.GraphSimulation(1, 10000, 1)

        container_layout = QHBoxLayout()
        container_layout.setContentsMargins(0, 0, 0, 0)

        container = QWidget()
        container.setLayout(container_layout)
        container.setFixedWidth(1200)
        container.setFixedHeight(575)
        container.setObjectName("Widget") 
        container.setStyleSheet("""
            #Widget {
                background-color: #313744;  
                border: 0;
                border-radius: 4px;
            }
        """)

        container_layout.addWidget(graph_widget)

        row.setContentsMargins(0, 0, 0, 0)
        row.addWidget(container)
        return row

    def styled_label(self, text, size):
        label = QLabel(text)
        label.setStyleSheet(
            f'font-size: {size}px; font-family:"{self.poppins}", sans-serif; color: #FFFFFF; font-weight: bold;'
        )
        return label

    def wrap_widget(self, layout, fixed_width=None, min_height=None, object_name=None, stylesheet=None):
        widget = QWidget()
        widget.setLayout(layout)
        if fixed_width: widget.setFixedWidth(fixed_width)
        if min_height: widget.setMinimumHeight(min_height)
        if object_name: widget.setObjectName(object_name)
        if stylesheet: widget.setStyleSheet(stylesheet)
        layout.setContentsMargins(0, 0, 0, 0)
        return widget

        
        
def main():
    app = QApplication([])
    window = SimulationWindow()
    window.show()
    app.exec_()
    
if __name__ == "__main__":
    main()