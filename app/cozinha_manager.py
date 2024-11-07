# app/cozinha_manager.py

from PySide6.QtWidgets import (QLabel, QListWidget, QPushButton, QVBoxLayout,
                               QWidget)


class CozinhaManager(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)

        # Lista de pedidos na cozinha
        self.lista_pedidos_cozinha = QListWidget()
        self.layout.addWidget(QLabel("Pedidos na Cozinha:"))
        self.layout.addWidget(self.lista_pedidos_cozinha)

        # Botão para marcar pedido como despachado
        self.despachar_pedido_button = QPushButton("Despachar Pedido")
        self.despachar_pedido_button.clicked.connect(self.despachar_pedido)
        self.layout.addWidget(self.despachar_pedido_button)

    def adicionar_pedido(self, pedido):
        # Adiciona pedido à lista de pedidos na cozinha
        self.lista_pedidos_cozinha.addItem(pedido)

    def despachar_pedido(self):
        for item in self.lista_pedidos_cozinha.selectedItems():
            item.setText(f"{item.text()} [Despachado]")
