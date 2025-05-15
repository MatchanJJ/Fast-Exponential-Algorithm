import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit
from PyQt5.QtGui import QTextCursor, QTextFormat, QColor
from PyQt5.QtCore import QTimer

class Debugger(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Algorithm Visualizer')
        self.layout = QVBoxLayout()

        self.code_display = QTextEdit()
        self.code_display.setReadOnly(True)
        self.layout.addWidget(self.code_display)

        self.next_btn = QPushButton('Next Step')
        self.next_btn.clicked.connect(self.next_step)
        self.layout.addWidget(self.next_btn)

        self.setLayout(self.layout)

        self.code = [
            "def fast_exponentiation(base, exp):",
            "    result = 1",
            "    if exp < 0:",
            "        base = 1 / base",
            "        exp = -exp",
            "    while exp > 0:",
            "        if exp % 2 == 1:",
            "            result *= base",
            "        base *= base",
            "        exp //= 2",
            "    return result"
        ]

        self.step = 0
        self.update_code_display()

    def update_code_display(self):
        self.code_display.clear()
        for line in self.code:
            self.code_display.append(line)

    def highlight_line(self, line_number):
        cursor = self.code_display.textCursor()
        cursor.movePosition(QTextCursor.Start)

        for _ in range(line_number):
            cursor.movePosition(QTextCursor.Down)

        cursor.select(QTextCursor.LineUnderCursor)
        fmt = QTextFormat()
        fmt.setBackground(QColor("yellow"))
        cursor.setBlockFormat(fmt)

    def next_step(self):
        if self.step < len(self.code):
            self.update_code_display()
            self.highlight_line(self.step)
            print(f"Step {self.step + 1}: {self.code[self.step]}")
            self.step += 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    debugger = Debugger()
    debugger.show()
    sys.exit(app.exec_())