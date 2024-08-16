from PySide6.QtWidgets import QApplication, QWidget

app = QApplication([])
window = QWidget()
window.setWindowTitle("First app")
window.setGeometry(1600, 100, 300, 500)

window.setMaximumHeight(700)
window.setStyleSheet("background-color: yellow")
window.show()
app.exec()