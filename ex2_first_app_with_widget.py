from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QPushButton,
                               QLabel,
                               QCheckBox,
                               QWidget,
                               QVBoxLayout,
                               QHBoxLayout)


class MyWindow(QMainWindow):
    def __init__(self, ) -> None:
        super().__init__()
        self.setWindowTitle("First app with Widget")
        self.setGeometry(1600, 100, 300, 100)
        
        hlayout = self.setup_hlayout()
        self.setup_btn()
        
        vlayout = QVBoxLayout()
        vlayout.addLayout(hlayout)
        vlayout.addWidget(self.btn)

        central_widget = QWidget()
        central_widget.setLayout(vlayout)
        self.setCentralWidget(central_widget)

    def setup_btn(self)->None:
        '''
        set up the push button
        '''
        self.btn = QPushButton("Click me!")
        self.btn.setCheckable(True)
        self.btn.setDisabled(True)
        
    def setup_hlayout(self)->QHBoxLayout:
        '''
        Set up the checkbox and label and put them 
        in a horizontal layout
        '''
        chb = QCheckBox()
        chb.stateChanged.connect(self.box_is_changed)
        lbl = QLabel("Do you want to use the push button?")
        hlayout = QHBoxLayout()
        hlayout.addWidget(chb)
        hlayout.addWidget(lbl)
        
        return hlayout
    
    def box_is_changed(self, event)->None:
        '''
        Slot for activating the push button
        '''
        if event ==2:
            self.btn.setDisabled(False)
        elif event == 0:
            self.btn.setDisabled(True)
            

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()

    window.show()
    app.exec()