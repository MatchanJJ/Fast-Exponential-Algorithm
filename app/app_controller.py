from PyQt5.QtWidgets import QApplication, QDesktopWidget
from app.windows.start_window import StartWindow
from app.windows.simulation_window import SimulationWindow
from app.windows.menu_window import MenuWindow
from app.windows.visualization_window import VisualizationWindow

class AppController:
    def __init__(self):
        self.start_window = StartWindow()
        self.menu_window = MenuWindow()
        self.simulation_window = SimulationWindow()
        self.visualization_window = VisualizationWindow()

        self.start_window.start_button.clicked.connect(self.show_menu_window)
        self.simulation_window.back_btn.clicked.connect(self.show_menu_window)
        self.menu_window.left_btn.clicked.connect(self.show_visualization_window)
        self.menu_window.right_btn.clicked.connect(self.show_simulation_window)

    # function for showing each window
    def show_start_window(self):
        self.hide_all_windows()
        self.center_window(self.start_window)
        self.start_window.show()

    def show_menu_window(self):
        self.hide_all_windows()
        self.center_window(self.menu_window)
        self.menu_window.show()

    def show_simulation_window(self):
        self.hide_all_windows()
        self.center_window(self.simulation_window)
        self.simulation_window.show()

    def show_visualization_window(self):
        self.hide_all_windows()
        self.center_window(self.visualization_window)
        self.visualization_window.show()

    def hide_all_windows(self):
        self.start_window.hide()
        self.menu_window.hide()
        self.simulation_window.hide()
        self.visualization_window.hide()
        
    def center_window(self, window):
        window.adjustSize()  # Adjust size based on content

        # Get screen geometry
        screen_geometry = QDesktopWidget().screenGeometry()
        window_geometry = window.frameGeometry()

        # Center the window
        window_geometry.moveCenter(screen_geometry.center())
        window.move(window_geometry.topLeft())

    def run(self):
        self.show_start_window()
