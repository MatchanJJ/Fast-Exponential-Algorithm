import time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.animation import FuncAnimation
from PyQt5.QtCore import Qt
import warnings
warnings.filterwarnings("ignore", category=UserWarning, message="Animation was deleted.*")



class FastExponentiation:
    def get_operations(base, exp):
        operations = 0  # Initialize operation counter
        result = 1                         # init
        base = base
        if exp < 0:
            base = 1 / base                         # flip the base
            exp = -exp 
        while exp > 0:
            if exp % 2 == 1:
                result *= base
                operations += 1  # Count multiplication
            base *= base
            operations += 1  # Count squaring
            exp //= 2
        return operations
    
    def get_time(base, exp):
        start = time.perf_counter()
        result = 1                        # init
        base = base 
        if exp < 0:
            base = 1 / base                         # flip the base
            exp = -exp
        while exp > 0:
            if exp % 2 == 1:
                result *= base
            base *= base
            exp //= 2
        end = time.perf_counter()
        return end - start

class NaiveExponentiation:
    
    def get_operations(base, exp):
        operations = 0  
        result = 1                       
        base = base   
        
        if exp < 0:
            base = 1 / base                        
            exp = -exp
        for _ in range(exp):
            result *= base
            operations += 1  
        return operations
    
    
    def get_time(base, exp):
        start = time.perf_counter()
        result = 1                         
        base = base
        
        if exp < 0:
            base = 1 / base                         
            exp = -exp
            
        for _ in range(exp):
            result *= base
        end = time.perf_counter()
        return end - start
    

class GraphSimulation(QWidget):
    def __init__(self, start, end, step, mode, parent=None):
        super().__init__(parent)
        print("running GraphSimulation")

        # create canvas and layout
        self.fig = Figure(facecolor="#272b34")
        self.canvas = FigureCanvas(self.fig)
        self.ax = self.fig.add_subplot(111)
        self.canvas.setFixedSize(1149, 540)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.setAlignment(Qt.AlignCenter)
        self.setLayout(layout)
        
        # config
        self.base = 2
        self.start_exponent = start
        self.end_exponent = end
        self.step = step
        self.mode = mode

        # initialize plot elements
        self.x_values = []
        self.fast_times = []
        self.naive_times = []
        self.current_exp = self.start_exponent

        self.fast_line, = self.ax.plot([], [], label="Fast-Expo", color="#63dc93")
        self.naive_line, = self.ax.plot([], [], label="Naive", color="#ff4b4c")

        self.setup_plot()
        self.animate_graph()
        

    def setup_plot(self):
        self.ax.set_xlabel("Exponent", color='#959cae')
        
        if (self.mode == "Operation"): 
            self.ax.set_ylabel("# of Operations", color='#959cae')
        else:
            self.ax.set_ylabel("Runtime (seconds)", color='#959cae')
            
        
        
        self.ax.set_title("Fast vs Naive Exponentiation Simulation", color='white', fontweight='bold')
        self.ax.set_facecolor('#272b34')

        legend = self.ax.legend()
        legend.get_frame().set_facecolor('#3a3e47')
        legend.get_frame().set_edgecolor('#3a3e47')

        for text in legend.get_texts():
            text.set_color('white')

        self.ax.grid(False)
        self.ax.tick_params(axis='x', colors='#959cae')
        self.ax.tick_params(axis='y', colors='#959cae')

        for spine in ['bottom', 'top', 'left', 'right']:
            self.ax.spines[spine].set_visible(False)
        
        self.fig.tight_layout()
        self.fig.subplots_adjust(left=0.1)
        
    def update_plot(self, frame):
        if self.current_exp > self.end_exponent:
            return
        
        # change mode
        if (self.mode == "Operation"): 
            fast_time = FastExponentiation.get_operations(self.base, self.current_exp)
            naive_time = NaiveExponentiation.get_operations(self.base, self.current_exp)
        else:
            fast_time = FastExponentiation.get_time(self.base, self.current_exp)
            naive_time = NaiveExponentiation.get_time(self.base, self.current_exp)
        
        self.x_values.append(self.current_exp)
        self.fast_times.append(fast_time)
        self.naive_times.append(naive_time)

        self.fast_line.set_data(self.x_values, self.fast_times)
        self.naive_line.set_data(self.x_values, self.naive_times)

        self.ax.relim()
        self.ax.autoscale_view()

        self.current_exp += self.step
        self.fig.tight_layout()
        self.canvas.draw()
        
    def animate_graph(self):
        if(self.end_exponent > 1000):    
            self.animation = FuncAnimation(self.fig, self.update_plot, interval=1)
        else:
            self.animation = FuncAnimation(self.fig, self.update_plot, interval=5)
        
    def replot_graph(self, start, end, step):
        self.clear_animation()
        self.ax.clear()
        self.current_exp = start
        self.start_exponent = start 
        self.end_exponent = end
        self.step = step
        
        self.x_values = []
        self.fast_times = []
        self.naive_times = []
        
        self.fast_line, = self.ax.plot([], [], label="Fast-Expo", color="#63dc93")
        self.naive_line, = self.ax.plot([], [], label="Naive", color="#ff4b4c")
        
        if (self.mode == "Operation"): 
            self.ax.set_ylabel("# of Operations", color='#959cae')
        else:
            self.ax.set_ylabel("Runtime (seconds)", color='#959cae')
            
        self.setup_plot()
        self.animate_graph()
        
    def clear_animation(self):
        if hasattr(self, 'animation'):
            if self.animation.event_source:
                self.animation.event_source.stop()
            del self.animation
            self.animation = None
            print("Animation cleared.")
    

def main():
    app = QApplication([])
    sim = GraphSimulation(-1, -1000, 1, 'Operation')

    # Create a QMainWindow and set the GraphSimulation as its central widget
    window = QMainWindow()
    window.setCentralWidget(sim)
    window.show()

    app.exec_()

if __name__ == "__main__":
    main()
