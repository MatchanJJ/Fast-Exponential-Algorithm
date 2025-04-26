from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class startApp(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Algorithm Simulation")
        self.resize(920, 720)
        
        #create objects
        self.label_1 = QLabel("Naive vs Fast-Expo")
        self.label_2 = QLabel("COMPARING ALGORITHM")
        
        self.button_1 = QPushButton("start")
        
        #Layout
        master_layout = QVBoxLayout()
        master_layout.setAlignment(Qt.AlignCenter)
        
        master_layout.addWidget(self.label_1)
        master_layout.addWidget(self.label_2)
        master_layout.addWidget(self.button_1)
        
        self.setLayout(master_layout) 
        
def main():
    app = QApplication([])
    
    window = startApp()
    
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()