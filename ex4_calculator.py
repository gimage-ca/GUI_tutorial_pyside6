from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QLineEdit,
                               QPushButton,
                               QGridLayout,
                               QWidget)
from PySide6.QtCore import Qt

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(1600, 100, 230, 290)
        self.setFixedSize(230, 290)
        self.setWindowOpacity(0.99)
        
        self.layout = QGridLayout()
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setLayout(self.layout)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        
        self.setup_display()
                
        self.layout.addWidget(self.display, 0, 0, 1, 4)
        
        self.buttons = [
            "C", "+/-", "%", "÷",
            "7", "8", "9", "x",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "0", ".", "="
        ]
        
        self.buttons_fcn = {
            "C": self.clear,
            "+/-": self.change_sign,
            "%": self.percent,
            "÷": self.divide,
            "x": self.multiply,
            "-": self.subtract,
            "+": self.add,
            "=": self.equal
        }
    
        self.result = None
        self.first_number = None
        self.second_number = None
        self.operator = None
        self.setup_push_buttons()
        
    def __get_btn_properties(self):
        return{
            "border": "1px solid rgba(0, 0, 0, 0.5)",
            "color": "rgba(242, 163, 60, 1)",
            "color_pressed": "rgb(212, 121, 31)",
            "number_color": "rgb(96, 96, 96)",
            "number_color_pressed": "rgb(157, 157, 157)",
            "first_row_btn_color": "rgb(59, 59, 59)"
        }
        
    def __get_btn_styles(self):
        prop = self.__get_btn_properties()
        
        style_last_col = f"""
                        QPushButton{{
                            background-color: {prop['color']};
                            border: {prop['border']};
                            margin: 0;
                            font-size: 30px;
                        }}
                        QPushButton::pressed {{
                            background-color: {prop['color_pressed']}
                        }}
        """
        
        style_first_row = f"""
                        QPushButton{{
                            background-color: {prop['first_row_btn_color']};
                            border: {prop['border']};
                            margin: 0;
                            font-size: 25px;
                        }}
                        QPushButton::pressed {{
                            background-color: {prop['number_color']}
                        }}
                        """
                        
        general_style = f"""
                        QPushButton{{
                            background-color: {prop['number_color']};
                            border: {prop['border']};
                            margin: 0;
                            font-size: 25px;
                        }}
                        QPushButton::pressed{{
                            background-color: {prop['number_color_pressed']};
                        }}
                        """
        return style_last_col, style_first_row, general_style
        
    def setup_push_buttons(self):
        width = 60
        height = 50
        
        row = 0
        col = 0
        style_last_col, style_first_row, general_style = self.__get_btn_styles()

        for btn_txt in self.buttons:
            btn = QPushButton(btn_txt)
            if row == 4:
                if btn_txt == "0":
                    self.layout.addWidget(btn, row+1, col, 1, 2)
                    btn.setFixedSize(2*width, height)
                else:
                    self.layout.addWidget(btn, row+1, col+1, 1, 1)
                    btn.setFixedSize(width, height)
            else:
                self.layout.addWidget(btn, row+1, col, 1, 1)
                btn.setFixedSize(width, height)
            col += 1                
            
            if row == 0:
                btn.setStyleSheet(style_first_row)
            else:
                btn.setStyleSheet(general_style)
                
            if col > 3:
                btn.setStyleSheet(style_last_col)
                col = 0
                row += 1
            if btn_txt == "=":
                btn.setStyleSheet(style_last_col)
    
    def clear(self):
        '''Clear line edit'''
        self.display.clear()
        
    def change_sign(self):
        pass
    
    def percent(self):
        pass
    
    def divide(self):
        pass
    
    def multiply(self):
        pass
    
    def subtract(self):
        pass
    
    def add(self):
        pass
    
    def equal(self):
        self.display.setText(str(round(self.result, 4)))
        
    def setup_display(self):
        self.display = QLineEdit()
        self.display.setPlaceholderText('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self.display.setFixedSize(230, 50)
        
        self.display.setStyleSheet("""
                                   QLineEdit {
                                       font-size: 40px;
                                       padding: 0 10 0 0;
                                       font-weight: 200;
                                        background: qlineargradient(
                                            x1: 0, y1: 0,
                                            x2: 0, y2: 1,
                                            stop: 0 rgb(58, 58, 62),
                                            stop: 0.6 rgb(58, 59, 62),
                                            stop: 1 rgb(52, 68, 80)
                                        );
                                   }
                                   """)
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    
    window = Calculator()
    window.show()
    app.exec()