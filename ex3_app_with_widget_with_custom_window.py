from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QPushButton,
                               QLabel,
                               QCheckBox,
                               QWidget,
                               QVBoxLayout,
                               QHBoxLayout)
def box_is_changed(event):
    if event ==2:
        btn.setDisabled(False)
    elif event == 0:
        btn.setDisabled(True)
    
app = QApplication([])
window = QMainWindow()
window.setWindowTitle("First app with Widget")
window.setGeometry(1600, 100, 300, 100)

btn = QPushButton("Click me!")
btn.setCheckable(True)
btn.setDisabled(True)

chb = QCheckBox()
chb.stateChanged.connect(box_is_changed)

lbl = QLabel("Do you want to use the push button?")

hlayout = QHBoxLayout()
hlayout.addWidget(chb)
hlayout.addWidget(lbl)

vlayout = QVBoxLayout()
vlayout.addLayout(hlayout)
vlayout.addWidget(btn)

central_widget = QWidget()
central_widget.setLayout(vlayout)
window.setCentralWidget(central_widget)

window.show()
app.exec()