from PyQt5.QtWidgets import QWidget, QHBoxLayout, QGridLayout, QApplication, QPushButton, QLineEdit
import sys
import os
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.numbers_show = QLineEdit()
        self.reverse = QPushButton('⌫', self)
        self.Empty = QPushButton('AC', self)
        self.percent = QPushButton('%', self)
        self.divide = QPushButton('÷', self)
        self.seven = QPushButton('7', self)
        self.eight = QPushButton('8', self)
        self.nine = QPushButton('9', self)
        self.multiply = QPushButton('x', self)
        self.four = QPushButton('4', self)
        self.five = QPushButton('5', self)
        self.six = QPushButton('6', self)
        self.subtract = QPushButton('-', self)
        self.one = QPushButton('1', self)
        self.two = QPushButton('2', self)
        self.three = QPushButton('3', self)
        self.add = QPushButton('+', self)
        self.change_sign = QPushButton('+/-', self)
        self.zero = QPushButton('0', self)
        self.dot = QPushButton('.', self)
        self.equal_to = QPushButton('=', self)
        self.previous_value = None
        self.current_value = "0"
        self.operator = None
        self.waiting_for_new_no = False

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon(self.resource("calculator.ico")))
        self.layout()
        self.style()
        self.get_input()

    def resource(self, relative_path):
        try:
            base_path = sys._MEIPASS    

        except AttributeError:
            base_path = os.path.abspath('.')

        return os.path.join(base_path, relative_path)

    def layout(self):
        layout = QGridLayout()
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.numbers_show)
        layout.addLayout(hlayout, 0, 0, 1, 4)
        layout.addWidget(self.reverse, 1, 0)
        layout.addWidget(self.Empty, 1, 1)
        layout.addWidget(self.percent, 1, 2)
        layout.addWidget(self.divide, 1, 3)
        layout.addWidget(self.seven, 2, 0)
        layout.addWidget(self.eight, 2, 1)
        layout.addWidget(self.nine, 2, 2)
        layout.addWidget(self.multiply, 2, 3)
        layout.addWidget(self.four, 3, 0)
        layout.addWidget(self.five, 3, 1)
        layout.addWidget(self.six, 3, 2)
        layout.addWidget(self.subtract, 3, 3)
        layout.addWidget(self.one, 4, 0)
        layout.addWidget(self.two, 4, 1)
        layout.addWidget(self.three, 4, 2)
        layout.addWidget(self.add, 4, 3)
        layout.addWidget(self.change_sign, 5, 0)
        layout.addWidget(self.zero, 5, 1)
        layout.addWidget(self.dot, 5, 2)
        layout.addWidget(self.equal_to, 5, 3)

        self.setLayout(layout)

    def style(self):
        self.numbers_show.setMinimumHeight(140)
        self.numbers_show.setFixedWidth(273)

        self.add.setObjectName('add')
        self.multiply.setObjectName('multiply')
        self.divide.setObjectName('divide')
        self.percent.setObjectName('percent')
        self.subtract.setObjectName('subtract')
        self.Empty.setObjectName('empty')
        self.reverse.setObjectName('reverse')
        self.equal_to.setObjectName('equal_to')

        self.setStyleSheet("""
    QWidget{
            background-color: black;        
                           }
    QPushButton{
        background-color: hsl(287, 3%, 28%);
        color: white;
        border: 2px solid black;
        border-radius: 30px; 
        width: 55px;
        height: 55px;
        font-weight: bold;
        font-size: 25px;
        padding: 1px;
        font-family: "San Francisco";
                           }
    QPushButton#divide{
        font-size: 30px;}
                           
    QPushButton#subtract{
        font-size: 40px;}

    QPushButton:hover {
        background-color: hsl(287, 3%, 40%);     
                           }

    QPushButton#empty,
    QPushButton#multiply,
    QPushButton#subtract,
    QPushButton#add,
    QPushButton#percent,
    QPushButton#divide,
    QPushButton#reverse,
    QPushButton#equal_to{
    background-color: hsl(34, 95%, 55%)}
                           
    QPushButton#empty:hover,
    QPushButton#multiply:hover,
    QPushButton#subtract:hover,
    QPushButton#add:hover,
    QPushButton#percent:hover,
    QPushButton#divide:hover,
    QPushButton#reverse:hover,
    QPushButton#equal_to:hover{
    background-color: hsl(36, 90%, 65%)}

""")

        self.numbers_show.setStyleSheet(
            "color: white;"
            "border: transparent")
        self.numbers_show.setFont(QFont('San Francisco', 40))
        self.numbers_show.setPlaceholderText('0')
        self.numbers_show.setAlignment(Qt.AlignRight | Qt.AlignBottom)
        self.numbers_show.setReadOnly(True)

    def get_input(self):
        number_buttons = [self.zero, self.one, self.two, self.three, self.four, self.five, self.six,
                   self.seven, self.eight, self.nine, self.dot]
        
        operator_buttons = [self.add, self.multiply, self.subtract, self.divide]

        for button in number_buttons:
            button.clicked.connect(self.number_clicked)

        for button in operator_buttons:
            button.clicked.connect(self.operator_clicked)

        self.set_font_size()
        self.equal_to.clicked.connect(self.calculate_result)
        self.Empty.clicked.connect(self.remove)
        self.numbers_show.returnPressed.connect(self.calculate_result)
        self.reverse.clicked.connect(self.backspace)
        self.change_sign.clicked.connect(self.toggle_sign)
        self.percent.clicked.connect(self.percent_pressed)

    def set_font_size(self):
        length = len(self.current_value)

        if length <= 5:
            size = 45
        elif length <= 9:
            size = 35
        elif length <= 13:
            size = 28
        else:
            size = 20
        
        self.numbers_show.setFont(QFont('San Francisco', size))

    def remove(self):
        self.current_value = "0"
        self.previous_value = None
        self.operator = None
        self.waiting_for_new_no = False
        self.numbers_show.setText("0")

    def backspace(self):
        if not self.waiting_for_new_no:
            self.current_value = self.current_value[:-1] or "0"
            self.numbers_show.setText(self.current_value)
            self.set_font_size()

    def number_clicked(self):
        sender_text = self.sender().text()
        if sender_text == "." and "." in self.current_value:
            return
        if self.waiting_for_new_no:
            self.current_value = sender_text
            self.waiting_for_new_no = False
        else:
            if self.current_value == '0' or self.current_value == 'Error':
                self.current_value = sender_text
            else:
                self.current_value += sender_text

        self.numbers_show.setText(self.current_value)
        self.set_font_size()

    def operator_clicked(self):
        operator = self.sender().text()

        if self.previous_value is not None:
            self.calculate_result()

        self.operator = operator
        self.previous_value = float(self.current_value)
        self.waiting_for_new_no = True

    def calculate_result(self):
        if self.operator == None:
            return
        
        current = float(self.current_value)

        if self.operator == "+":
            result = self.previous_value + current

        elif self.operator == "-":
            result = self.previous_value - current

        elif self.operator == "x":
            result = self.previous_value * current

        elif self.operator == "÷":
            if current == 0:
                self.numbers_show.setText("Error")
                return
            result = self.previous_value / current
        
        self.current_value = str(result)
        self.numbers_show.setText(self.current_value)
        self.set_font_size()

        self.previous_value = None
        self.waiting_for_new_no = True
        self.operator = None

    def toggle_sign(self):
        if self.current_value.startswith("-"):
            self.current_value = self.current_value[1:]
        else:
            if self.current_value != "0" and self.current_value != "0.0":
                self.current_value = "-" + self.current_value

        self.numbers_show.setText(self.current_value)
        self.set_font_size()

    def percent_pressed(self):
        current = float(self.current_value)

        if self.previous_value is None:
            result = current / 100

        else:
            # For + and -
            if self.operator == "+":
                result = self.previous_value + (self.previous_value * current / 100 )
            elif self.operator == "-":
                result = self.previous_value - (self.previous_value * current / 100 )

            # For × and ÷
            elif self.operator == "x":
                result = self.previous_value * current / 100

            elif self.operator == "÷":
                result = self.previous_value / current * 100

        self.current_value = str(result)
        self.numbers_show.setText(self.current_value)
        self.set_font_size()

def main():
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
