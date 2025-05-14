import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QMessageBox, QStackedWidget
import components.component as ct
import components.font_manager as fm
from PyQt5.QtGui import QIcon

class VisualizationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Visualization")
        self.setMinimumSize(1280, 820)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.setObjectName("MainWidget")
        self.setStyleSheet('#MainWidget {background-color: #141920; border: 2px solid #333; border-radius: 15px;}')
        self.poppins = fm.FontManager.get_poppins(16)
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        icon = os.path.normpath(os.path.join(current_dir, '..', '..', 'icons', 'window_icon.png'))
        self.setWindowIcon(QIcon(icon))
        # config
        self.border_radius = 20

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 40, 0, 0)
        layout.setSpacing(10)

        layout.addLayout(self.create_top_bar())
        layout.addLayout(self.create_input_section())
        layout.addLayout(self.create_visualization_area())
        layout.addStretch(1)

        self.setLayout(layout)

    def create_top_bar(self):
        row = QHBoxLayout()
        widget = self.wrap_widget(QHBoxLayout(), fixed_width=1200)

        self.back_btn = ct.BackButton()
        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        label = QLabel("| Algorithm Visualization")
        label.setStyleSheet('color: #03CD97; font-size: 22px; font-weight:bold')

        widget.layout().addWidget(self.back_btn)
        widget.layout().addWidget(label)
        widget.layout().addItem(spacer)

        row.addWidget(widget)
        row.setContentsMargins(0, 0, 0, 5)
        return row

    def create_input_section(self):
        row = QHBoxLayout()
        layout = QHBoxLayout()
        widget = self.wrap_widget(layout, fixed_width=1200, min_height=85, object_name="Widget",
                                  stylesheet=f"#Widget {{background-color: #313744; border: 0; border-radius: {self.border_radius}}}")

        label_title = self.styled_label("Visualization", 20)
        label_base = self.styled_label("Tool", 20)
        label_base.setStyleSheet('color: #03CD97; font-size: 20px; font-weight:bold')

        input_layout = QHBoxLayout()

        self.base_input = ct.InputBox("Base")
        self.exp_input = ct.InputBox("Exponent")
        
        items = ["Naive", "Fast-Expo"]
        self.mode_input = ct.ComboBox("Algorithm", items)

        input_layout.addWidget(self.base_input)
        input_layout.addWidget(self.exp_input)
        input_layout.addWidget(self.mode_input)
        input_layout.setSpacing(5)

        buttons = QHBoxLayout()

        self.stop_button = ct.StopButton()
        self.play_button = ct.PlayButton()
        self.play_button.reset_state()

        buttons.addWidget(self.stop_button)
        buttons.addWidget(self.play_button)
        buttons.setContentsMargins(0, 10, 0, 0)
        buttons.setSpacing(18)

        label_col = QHBoxLayout()
        label_col.addWidget(label_title)
        label_col.addWidget(label_base)
        label_col.setSpacing(6)

        layout.addLayout(label_col)
        layout.addLayout(input_layout)
        layout.addStretch(1)
        layout.addLayout(buttons)
        layout.setSpacing(35)
        layout.setContentsMargins(25, 0, 25, 0)

        row.addWidget(widget)
        return row

    def create_visualization_area(self):
        row = QHBoxLayout()
        self.container_layout = QHBoxLayout()
        self.container_layout.setContentsMargins(0, 0, 0, 0)

        self.container = QWidget()
        self.container.setLayout(self.container_layout)
        self.container.setFixedWidth(1200)
        self.container.setFixedHeight(600)
        self.container.setObjectName("Widget") 
        self.container.setStyleSheet(f"""    
            #Widget {{
                background-color: #313744;  
                border: 0;
                border-radius: {self.border_radius};
            }}
        """)
        
        self.stacked = QStackedWidget()

        self.placeholder = ct.NoDataFound()
        self.stacked.addWidget(self.placeholder)
        
        self.container_layout.addWidget(self.stacked, alignment=Qt.AlignCenter)
        
        row.setContentsMargins(0, 0, 0, 0)
        row.addWidget(self.container)
        return row
        
        
    # Helper methods
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
    window = VisualizationWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
