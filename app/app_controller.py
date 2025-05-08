from PyQt5.QtWidgets import QApplication
from app.windows.start_window import StartWindow
from app.windows.simulation_window import SimulationWindow

class AppController:
    def __init__(self):
        self.start_window = StartWindow()
        self.simulation_window = SimulationWindow()

        self.start_window.start_button.clicked.connect(self.show_simulation_window)
        self.simulation_window.back_btn.clicked.connect(self.show_start_window)

    def show_simulation_window(self):
        self.start_window.close()
        self.simulation_window.show()

    def show_start_window(self):
        self.simulation_window.close()
        self.start_window.show()

    def run(self):
        self.start_window.show()