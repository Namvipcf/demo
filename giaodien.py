import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("Ứng dụng PyQt6 đơn giản")
    window.setGeometry(100, 100, 400, 200)

    label = QLabel("Xin chào, PyQt6!", parent=window)
    label.move(150, 80)

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
