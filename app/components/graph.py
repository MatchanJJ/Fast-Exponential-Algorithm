import time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class FastExponentiation:
    @staticmethod
    def get_time(base, exp):
        start = time.perf_counter()
        result = 1
        while exp > 0:
            if exp % 2 == 1:
                result *= base
            base *= base
            exp //= 2
        end = time.perf_counter()
        return end - start

class NaiveExponentiation:
    @staticmethod
    def get_time(base, exp):
        start = time.perf_counter()
        result = 1
        for _ in range(exp):
            result *= base
        end = time.perf_counter()
        return end - start

class GraphSimulation(QWidget):
    def __init__(self, start, end, step, parent=None):
        super().__init__(parent)
        print("running GraphSimulation")
        
        # create canvas and layout
        self.fig = Figure(facecolor="#272b34")
        self.canvas = FigureCanvas(self.fig)
        self.ax = self.fig.add_subplot(111)
        
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        
        # config
        self.base = 2
        self.start_exponent = start
        self.end_exponent = end
        self.step = step
        
        # call
        self.graph()

    def graph(self):
        x_values = []
        fast_times = []
        naive_times = []

        exponent = self.start_exponent
        

        while exponent <= self.end_exponent:
            fast_time = FastExponentiation.get_time(self.base, exponent)
            naive_time = NaiveExponentiation.get_time(self.base, exponent)

            x_values.append(exponent)
            fast_times.append(fast_time)
            naive_times.append(naive_time)

            exponent += self.step

        
        # add subplot, 1 row, 1 column, 1st plot        
        self.ax.plot(x_values, fast_times, label="Fast-Expo", color="#63dc93")
        self.ax.plot(x_values, naive_times, label="Naive", color="#ff4b4c")
        self.ax.set_xlabel("Exponent", color='#959cae')
        self.ax.set_ylabel("Runtime (seconds)", color='#959cae')
        self.ax.set_title("Fast vs Naive Exponentiation Simulation", color='white', fontweight='bold')
        self.ax.set_facecolor('#272b34')
        legend = self.ax.legend()

        legend.get_frame().set_facecolor('#3a3e47')  
        legend.get_frame().set_edgecolor('#3a3e47')    

        # Set text color
        for text in legend.get_texts():
            text.set_color('white')
        
        self.ax.grid(False)
        
        # Set tick label colors (numbers on self.axes)
        self.ax.tick_params(axis='x', colors='#959cae')
        self.ax.tick_params(axis='y', colors='#959cae')

        # Set self.axes edge (border) color
        self.ax.spines['bottom'].set_color('white')
        self.ax.spines['top'].set_color('white')
        self.ax.spines['left'].set_color('white')
        self.ax.spines['right'].set_color('white')

        self.fig.tight_layout()
        print("Draw Canvas")
        self.canvas.draw()

def main():
    app = QApplication([])
    sim = GraphSimulation(1, 1000, 1)

    # Create a QMainWindow and set the GraphSimulation as its central widget
    window = QMainWindow()
    window.setCentralWidget(sim)
    window.show()

    app.exec_()

if __name__ == "__main__":
    main()
