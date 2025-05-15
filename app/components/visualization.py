import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QLabel, QHBoxLayout, QWidget, QVBoxLayout, QComboBox, QDialog
from PyQt5.QtGui import QIcon, QIntValidator
import components.font_manager as fm
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtSvg import QSvgWidget
import components.component as ct


class FastExpo():
    def fast_exponentiation(base, exp):
        result = 1                             # init 
        if exp < 0:
            base = 1 / base                    # flip the base
            exp = -exp                              
        while exp > 0:                         # loop until exponent is zero
            if exp % 2 == 1:                   # if exponent is odd, multiply result by base
                result *= base
            base *= base                       # square the base
            exp //= 2                          # halve the exponent
        return result                          # return result


class Visualization(QWidget):
    
    def __init__(self, base, exp, parent=None):
        super().__init__(parent)
        self.setFixedSize(1158, 570)
        self.setContentsMargins(0,0,0,15)
        
        self._create_code_wdiget()
        self._create_result_wdiget()
        
        # config
        self.base = base
        self.exp = exp        
        self.current_line = None
        self.gen = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.next_step)
        self.is_paused = False
        
        layout = QVBoxLayout()
        layout.addWidget(self.code_widget)
        layout.addWidget(self.result_output_widget)
        
        self.setLayout(layout)
        
    def _create_code_wdiget(self):
        # Create two child widgets
        self.code_widget = QWidget()
        self.code_widget.setStyleSheet('background-color: #1b1e28; border: 0px; border-radius: 4px;')  # Light blue
        self.code_widget.setFixedSize(1145, 420)
        self.code_widget.setContentsMargins(0,0,0,0)
        
        #create code section
        code_widget_layout = QVBoxLayout()
        code_widget_layout.addStretch(1)
        code_1 = ct.CodeBlock("<span style='color: #add7ff;'> def fast_exponentiation</span><span style='color: #fffac2;'>(</span><span style='color: #ffffff;'>base, exp</span><span style='color: #fffac2;'>)</span>:")
        code_2 = ct.CodeBlock("<span style='color: #a6accd;'>    result</span> <span style='color: #fffac2;'>=</span> <span style='color: #5de4c7;'>1</span>  <span style='color: #717d9c;'># init</span>")
        code_3 = ct.CodeBlock("<span style='color: #5de4c7;'>    if</span> <span style='color: #ffffff;'>exp</span> <span style='color: #fffac2;'>&lt;</span> <span style='color: #5de4c7;'>0</span><span style='color: #fffac2;'>:</span>")
        code_4 = ct.CodeBlock("<span style='color: #ffffff;'>        base</span> <span style='color: #fffac2;'>=</span> <span style='color: #5de4c7;'>1</span> <span style='color: #fffac2;'>/</span> <span style='color: #ffffff;'>base</span>  <span style='color: #717d9c;'># flip the base if negative exp</span>")
        code_5 = ct.CodeBlock("<span style='color: #ffffff;'>        exp</span> <span style='color: #fffac2;'>=</span> <span style='color: #fffac2;'>-</span><span style='color: #ffffff;'>exp</span>")
        code_6 = ct.CodeBlock("<span style='color: #5de4c7;'>    while</span> <span style='color: #ffffff;'>exp</span> <span style='color: #fffac2;'>&gt;</span> <span style='color: #5de4c7;'>0</span><span style='color: #fffac2;'>:</span>  <span style='color: #717d9c;'># loop until exponent is zero</span>")
        code_7 = ct.CodeBlock("<span style='color: #5de4c7;'>        if</span> <span style='color: #ffffff;'>exp</span> <span style='color: #fffac2;'>%</span> <span style='color: #5de4c7;'>2</span> <span style='color: #fffac2;'>==</span> <span style='color: #5de4c7;'>1</span><span style='color: #fffac2;'>:</span>  <span style='color: #717d9c;'># if exponent is odd, multiply result by base</span>")
        code_8 = ct.CodeBlock("<span style='color: #ffffff;'>            result</span> <span style='color: #fffac2;'>*=</span> <span style='color: #ffffff;'>base</span>")
        code_9 = ct.CodeBlock("<span style='color: #ffffff;'>        base</span> <span style='color: #fffac2;'>*=</span> <span style='color: #ffffff;'>base</span>  <span style='color: #717d9c;'># square the base</span>")
        code_10 = ct.CodeBlock("<span style='color: #ffffff;'>        exp</span> <span style='color: #fffac2;'>//=</span> <span style='color: #5de4c7;'>2</span>  <span style='color: #717d9c;'># halve the exponent</span>")
        code_11 = ct.CodeBlock("<span style='color: #5de4c7;'>    return</span> <span style='color: #ffffff;'>result</span>  <span style='color: #717d9c;'># return result</span>")
        
        # add to widget       
        self.code_blocks = [code_1, code_2, code_3, code_4, code_5, code_6, code_7, code_8, code_9, code_10, code_11]
        for code in self.code_blocks:
            code_widget_layout.addWidget(code)
            
        code_widget_layout.setContentsMargins(0,0,0,0)
        code_widget_layout.setSpacing(0)
        code_widget_layout.addStretch(1)
        
        self.code_widget.setLayout(code_widget_layout)
    
    def _create_result_wdiget(self):
        self.result_output_widget = QWidget()
        self.result_output_widget.setObjectName('Result')
        self.result_output_widget.setStyleSheet('#Result{background-color: #1b1e28; border: 0px; border-radius: 4px;}')
        self.result_output_widget.setFixedSize(1145, 100)
        self.result_output_widget.setContentsMargins(0,0,0,50)
        
        self.result_output = ct.ResultBlock('result', '')
        self.base_output = ct.ResultBlock('base', '')
        self.exp_output = ct.ResultBlock('exp', '')
        
        layout = QHBoxLayout()
        layout.addWidget(self.result_output)
        layout.addWidget(self.base_output)
        layout.addWidget(self.exp_output)
        layout.addStretch(1)
        layout.setAlignment(Qt.AlignTop)
        
        self.result_output_widget.setLayout(layout)
    
    def start_visualization(self):
        base = self.base
        exp = self.exp
        
        if self.current_line is not None:
            self.code_blocks[self.current_line - 1].unhighlight()
        print("start_visualization reached")
        self.gen = self.fast_expo_gen(base,exp)
        self.timer.start(500)
    
    def next_step(self):
        try:
            # Get both line number and state
            line_num, state = next(self.gen)
            
            # Highlight code line
            if self.current_line is not None:
                self.code_blocks[self.current_line - 1].unhighlight()
            self.code_blocks[line_num - 1].highlight()
            self.current_line = line_num
            
            # Update display values
            self.result_output.update_value(state['result'] if state['result'] is not None else "1")
            self.base_output.update_value(state['base'])
            self.exp_output.update_value(state['exp'])
        except StopIteration as e:
            self.timer.stop()
            final_result = e.value
            self.result_output.update_value(f"{final_result}")
            print("Visualization complete")
            
    def toggle_pause(self):
        
        self.is_paused = not self.is_paused
        if self.is_paused:
            self.timer.stop()
        else:
            self.timer.start(1000)
        print(self.is_paused)
        return self.is_paused
    
    def stop(self):
        self.timer.stop()
        self.is_paused = False
        # Clear any highlighting
        if self.current_line is not None:
            self.code_blocks[self.current_line - 1].unhighlight()
    
    @staticmethod
    def fast_expo_gen(base, exp):
        print(f"\n--- Starting generator with base={base}, exp={exp} ---")
        state = {"result": None, "base": base, "exp": exp}
        
        yield (1, state)  # code_1
        result = 1
        state = {"result": result, "base": base, "exp": exp}
        yield (2, state)  # code_2

        if exp < 0:
            yield (3, state)  # code_3
            base = 1 / base
            state = {"result": result, "base": base, "exp": exp}
            yield (4, state)  # code_4
            
            exp = -exp
            state = {"result": result, "base": base, "exp": exp}
            yield (5, state)  # code_5

        state = {"result": result, "base": base, "exp": exp}
        yield (6, state)  # code_6

        while exp > 0:
            state = {"result": result, "base": base, "exp": exp}
            yield (6, state)  # code_6 (loop check)
            
            if exp % 2 == 1:
                state = {"result": result, "base": base, "exp": exp}
                yield (7, state)  # code_7
                result *= base
                state = {"result": result, "base": base, "exp": exp}
                yield (8, state)  # code_8

            base *= base
            state = {"result": result, "base": base, "exp": exp}
            yield (9, state)  # code_9
            
            exp //= 2
            state = {"result": result, "base": base, "exp": exp}
            yield (10, state)  # code_10

        state = {"result": result, "base": base, "exp": exp}
        yield (11, state)  # code_11
        return result
