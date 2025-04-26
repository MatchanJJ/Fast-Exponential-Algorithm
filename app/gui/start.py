from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFontDatabase

class startApp(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Algorithm Simulation")
        self.resize(1080, 350)
        
        #create objects
        self.label_1 = QLabel("Naive vs Fast-Expo")
        self.label_2 = QLabel("COMPARING ALGORITHM")
        
        self.button_1 = QPushButton("start")
        
        
        #stylesheets
        font_id = QFontDatabase.addApplicationFont("font/IBM_Plex_Mono/IBMPlexMono-Regular.ttf")
        font_id_2 = QFontDatabase.addApplicationFont("font/Poppins/Poppins-Bold.ttf")
            
        if font_id == -1:
            print("❌ Failed to load font") 
        else:
            font_1 = QFontDatabase.applicationFontFamilies(font_id)[0]
            print(f"Loaded: {font_1}")
            
        if font_id_2 == -1:
            print("❌ Failed to load font") 
        else:
            font_2 = QFontDatabase.applicationFontFamilies(font_id_2)[0]
            print(f"Loaded: {font_2}")
        
        self.setObjectName("MainWidget")        
        self.setStyleSheet('#MainWidget{background-color: #141920; border: 2px solid #333; border-radius: 15px;}')
        
        self.label_1.setStyleSheet(f'font-size: 64px; font-family:"{font_2}", sans-serif; color: white; font-weight: bold')
        self.label_2.setStyleSheet(f'font-size: 32px; font-family:"{font_1}", monospace; color: #C7CBD7;')
        self.label_2.setAlignment(Qt.AlignCenter)

        
        self.button_1.setStyleSheet("""
                                    QPushButton {
                                        background-color: #03CD97;
                                        color: white;
                                        font-size: 24px;
                                        border: none;
                                        border-radius: 10px;
                                        padding: 10px 20px;
                                    }
                                    
                                    QPushButton:hover {
                                        background-color: #04B284;
                                    }
                                    
                                    QPushButton:pressed {
                                        background-color: #028E69;
                                    }
                                    """)
        #Layout
        master_layout = QVBoxLayout()
        master_layout.setAlignment(Qt.AlignCenter)
        
        layout_1 = QVBoxLayout()        
        layout_1.addWidget(self.label_1)
        layout_1.addWidget(self.label_2)
        
        master_layout.addLayout(layout_1)
        master_layout.addWidget(self.button_1)
        
        self.setLayout(master_layout) 
        
def main():
    app = QApplication([])
    
    window = startApp()
    
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()