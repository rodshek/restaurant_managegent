# main.py

import sys

from PySide6.QtWidgets import QApplication

from app.pedido_manager import PedidoManager


def main():
    app = QApplication(sys.argv)
    window = PedidoManager()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
