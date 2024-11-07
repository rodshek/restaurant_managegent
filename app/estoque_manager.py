# app/estoque_manager.py

from PySide6.QtWidgets import QLabel, QListWidget, QVBoxLayout, QWidget


class EstoqueManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestão de Estoque")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Gestão de Estoque"))

        self.lista_estoque = QListWidget()
        layout.addWidget(self.lista_estoque)

        self.setLayout(layout)

    def adicionar_item_estoque(self, item, quantidade):
        # Adiciona um item ao estoque
        self.lista_estoque.addItem(f"{item} - Quantidade: {quantidade}")

    def atualizar_quantidade_item(self, item, nova_quantidade):
        # Atualiza a quantidade de um item no estoque
        for index in range(self.lista_estoque.count()):
            if item in self.lista_estoque.item(index).text():
                self.lista_estoque.item(index).setText(
                    f"{item} - Quantidade: {nova_quantidade}")
                break
