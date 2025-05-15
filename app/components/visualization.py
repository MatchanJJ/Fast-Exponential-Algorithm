import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QLabel, QHBoxLayout, QWidget, QVBoxLayout, QComboBox, QDialog
from PyQt5.QtGui import QIcon, QIntValidator
import components.font_manager as fm
from PyQt5.QtCore import Qt
from PyQt5.QtSvg import QSvgWidget
import components.component as ct

class NaiveExpo():
    def naive_exponentiation(base, exp):
        result = 1                                  #init
        if exp < 0:
            base = 1 / base                         # flip the base
            exp = -exp                              
        for _ in range(exp):                        #perform repeated multiplication
            result *= base              
        return result                               #return result

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


class VisualizeAlgo(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Create main container
        self.setFixedSize(1150, 570)
        self.setContentsMargins(0,0,0,0)

        # Create a horizontal layout
        layout = QHBoxLayout()
        
        # Create two child widgets
        self.code_widget = QWidget()
        self.code_widget.setStyleSheet('background-color: #1b1e28; border: 0px; border-radius: 4px;')  # Light blue
        self.code_widget.setFixedSize(900, 420)
        self.code_widget.setContentsMargins(0,0,0,0)
        
        #create code section
        code_widget_layout = QVBoxLayout()
        code_widget_layout.addStretch(1)
        code_1 = ct.CodeBlock("<span style='color: #add7ff;'> def fast_exponentiation</span><span style='color: #fffac2;'>(</span><span style='color: #ffffff;'>base, exp</span><span style='color: #fffac2;'>)</span>:")
        code_2 = ct.CodeBlock("<span style='color: #a6accd;'>    result</span> <span style='color: #fffac2;'>=</span> <span style='color: #5de4c7;'>1</span>  <span style='color: #717d9c;'># init</span>")
        code_3 = ct.CodeBlock("<span style='color: #5de4c7;'>    if</span> <span style='color: #ffffff;'>exp</span> <span style='color: #fffac2;'>&lt;</span> <span style='color: #5de4c7;'>0</span><span style='color: #fffac2;'>:</span>")
        code_4 = ct.CodeBlock("<span style='color: #ffffff;'>        base</span> <span style='color: #fffac2;'>=</span> <span style='color: #5de4c7;'>1</span> <span style='color: #fffac2;'>/</span> <span style='color: #ffffff;'>base</span>  <span style='color: #717d9c;'># flip the base</span>")
        code_5 = ct.CodeBlock("<span style='color: #ffffff;'>        exp</span> <span style='color: #fffac2;'>=</span> <span style='color: #fffac2;'>-</span><span style='color: #ffffff;'>exp</span>")
        code_6 = ct.CodeBlock("<span style='color: #5de4c7;'>    while</span> <span style='color: #ffffff;'>exp</span> <span style='color: #fffac2;'>&gt;</span> <span style='color: #5de4c7;'>0</span><span style='color: #fffac2;'>:</span>  <span style='color: #717d9c;'># loop until exponent is zero</span>")
        code_7 = ct.CodeBlock("<span style='color: #5de4c7;'>        if</span> <span style='color: #ffffff;'>exp</span> <span style='color: #fffac2;'>%</span> <span style='color: #5de4c7;'>2</span> <span style='color: #fffac2;'>==</span> <span style='color: #5de4c7;'>1</span><span style='color: #fffac2;'>:</span>  <span style='color: #717d9c;'># if exponent is odd, multiply result by base</span>")
        code_8 = ct.CodeBlock("<span style='color: #ffffff;'>            result</span> <span style='color: #fffac2;'>*=</span> <span style='color: #ffffff;'>base</span>")
        code_9 = ct.CodeBlock("<span style='color: #ffffff;'>        base</span> <span style='color: #fffac2;'>*=</span> <span style='color: #ffffff;'>base</span>  <span style='color: #717d9c;'># square the base</span>")
        code_10 = ct.CodeBlock("<span style='color: #ffffff;'>        exp</span> <span style='color: #fffac2;'>//=</span> <span style='color: #5de4c7;'>2</span>  <span style='color: #717d9c;'># halve the exponent</span>")
        code_11 = ct.CodeBlock("<span style='color: #5de4c7;'>    return</span> <span style='color: #ffffff;'>result</span>  <span style='color: #717d9c;'># return result</span>")
        
        # add to widget       
        codes = [code_1, code_2, code_3, code_4, code_5, code_6, code_7, code_8, code_9, code_10, code_11]
        for code in codes:
            code_widget_layout.addWidget(code)
            
        
        code_widget_layout.setContentsMargins(0,0,0,0)
        code_widget_layout.setSpacing(0)
        code_widget_layout.addStretch(1)
        self.code_widget.setLayout(code_widget_layout)

        self.result_widget = QWidget()
        self.result_widget.setStyleSheet('background-color: #F08080')  # Light coral
        self.result_widget.setFixedSize(124, 420)

        # Add widgets to the layout
        layout.addWidget(self.code_widget)
        layout.addWidget(self.result_widget)

        # Set layout to the main container
        self.setLayout(layout)
        
    def fast_expo_display(self):
        
        
        
        

    