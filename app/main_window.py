from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Gerenciamento de Restaurante")
        self.setGeometry(300, 100, 800, 600)
