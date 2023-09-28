import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ứng dụng PyQt6 đầu tiên")
        self.setGeometry(500, 300, 400, 200)

        self.label = QLabel("Chào mừng đến với PyQt6!")
        self.label.move(150, 80)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())