import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QStackedWidget, QMessageBox, QDesktopWidget
import components.component as ct
import components.font_manager as fm
import components.graph as graph

class SimulationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simulation")
        self.setMinimumSize(1280, 820)
    
        self.setObjectName("MainWidget")
        self.setStyleSheet('#MainWidget {background-color: #141920; border: 2px solid #333; border-radius: 15px;}')
        self.poppins = fm.FontManager.get_poppins(16)
        
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
        
        #calls the graph
        layout.addLayout(self.create_graph_area())
        
        layout.addStretch(1)

        self.setLayout(layout)
        
    def create_top_bar(self):
        row = QHBoxLayout()
        widget = self.wrap_widget(QHBoxLayout(), fixed_width=1200)

        self.back_btn = ct.BackButton()
        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        label = QLabel("| Algorithm Comparison")
        label.setStyleSheet('color: #03CD97; font-size: 22px; font-weight:bold')
        
        widget.layout().addWidget(self.back_btn)
        widget.layout().addWidget(label)
        widget.layout().addItem(spacer)

        row.addWidget(widget)
        row.setContentsMargins(0,0,0,5)
        return row

    def create_input_section(self):
        row = QHBoxLayout()
        layout = QHBoxLayout()
        widget = self.wrap_widget(layout, fixed_width=1200, min_height=85, object_name="Widget",
                                  stylesheet=f"#Widget {{background-color: #313744; border: 0; border-radius: {self.border_radius}}}")

        label_title = self.styled_label("Base", 20)
        label_base = self.styled_label("2", 20)
        label_base.setStyleSheet('color: #03CD97; font-size: 20px; font-weight:bold')
        
        input_layout = QHBoxLayout()
        
        self.start_input = ct.InputBox("Start Exponent")
        self.end_input = ct.InputBox("End Exponent")
        self.step_input = ct.InputBox("Step")
        
        items = ["Operation","Runtime"]
        self.mode_input = ct.ComboBox("Mode", items)
        
        items_2 = ["both","fast", "naive"]
        self.graph_input = ct.ComboBox("Graph", items_2)
        
        input_layout.addWidget(self.start_input)
        input_layout.addWidget(self.end_input)
        input_layout.addWidget(self.step_input)
        input_layout.addWidget(self.mode_input)
        input_layout.addWidget(self.graph_input)
        input_layout.setSpacing(5)

        buttons = QHBoxLayout()
        
        self.stop_button = ct.StopButton()
        self.play_button = ct.PlayButton()
        self.play_button.reset_state()
        
        buttons.addWidget(self.stop_button)
        buttons.addWidget(self.play_button)
        buttons.setContentsMargins(0,10,0,0)
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

    def create_graph_area(self):
        row = QHBoxLayout()
        self.is_stop = False
        
        # main container
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
        # placeholder
        self.placeholder = ct.NoDataFound()
        
        # create stack widget to handle switching
        self.stacked = QStackedWidget()
            
        self.stacked.addWidget(self.placeholder)
        
        self.container_layout.addWidget(self.stacked, alignment=Qt.AlignCenter)
        
        # function call
        self.play_button.clicked.connect(self.on_play)
        self.stop_button.clicked.connect(self.on_stop)

        row.setContentsMargins(0, 0, 0, 0)
        row.addWidget(self.container)
        return row

    def on_play(self):
        try:
            start = int(self.start_input.get_input())
            end = int(self.end_input.get_input())
            step = int(self.step_input.get_input())
            mode = self.mode_input.get_input()
            display = self.graph_input.get_input()
            print(display)
            frames = ((end - start) // step) + 1
             
            MAX_FRAMES = 10000
            if frames > MAX_FRAMES:
                frames = MAX_FRAMES
            gap = end - start
            
            # error handling
            if step <= 0:
                self.clear_line()
                raise ValueError("Step must be a positive number.")
            if start >= end:
                self.clear_line()
                raise ValueError("Start must be less than End.")
            if step > gap:
                self.clear_line()
                raise ValueError("Step must be within the range (end - start).")
                    
            # run only if animation is permanently stopped                
            if self.is_stop or not hasattr(self, 'graph_widget'):
                if hasattr(self, 'graph_widget') and self.graph_widget:
                    self.graph_widget.clear_animation()
                    self.stacked.removeWidget(self.graph_widget)
                    self.graph_widget.deleteLater()
                        
                self.graph_widget = graph.GraphSimulation(start, end, step, mode, frames, display)
                self.stacked.addWidget(self.graph_widget)
                self.stacked.setCurrentWidget(self.graph_widget)
                self.is_stop = False
                
                self.play_button.toggle_state()
                self.graph_widget.toggle_animation()
                self.graph_widget.set_is_running(True)
                return
            
            self.play_button.toggle_state()
            self.graph_widget.toggle_animation()
            
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Input Error", str(e))
            
    def on_stop(self):
        self.is_stop = True
        self.play_button.reset_state()
        try:
            if hasattr(self.graph_widget, 'animation') and self.graph_widget.animation:
                self.graph_widget.animation.event_source.stop()
        except Exception as e:
            self.is_stop = False
            print(str(e))
        
    def clear_line(self):
        self.start_input.clear()
        self.end_input.clear()
        self.step_input.clear()
    
    # helper classes    
    def styled_label(self, text, size):
        label = QLabel(text)
        label.setStyleSheet(
            f'font-size: {size}px; font-family:"{self.poppins}", sans-serif; color: #FFFFFF; font-weight: bold;'
        )
        return label
    
    # tf does this do .
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