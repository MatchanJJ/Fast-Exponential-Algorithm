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
        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)
        
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
        ax = self.fig.add_subplot(111)
        
        ax.plot(x_values, fast_times, label="Fast-Expo", color="blue")
        ax.plot(x_values, naive_times, label="Naive", color="orange")
        ax.set_xlabel("Exponent")
        ax.set_ylabel("Runtime (seconds)")
        ax.set_title("Fast vs Naive Exponentiation Simulation")
        ax.legend()
        ax.grid(True)

        self.fig.tight_layout()
        self.canvas.draw()
        print("Draw Canvas")

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
