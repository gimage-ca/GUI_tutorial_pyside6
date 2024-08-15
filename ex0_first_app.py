from PySide6.QtWidgets import QApplication, QMainWindow

app = QApplication([])
window = QMainWindow()
window.setWindowTitle("First app")
window.setGeometry(1600, 100, 300, 500)

window.setMaximumHeight(700)
window.setStyleSheet("background-color: yellow")
window.show()
app.exec()