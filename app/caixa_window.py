# app/caixa_window.py

from PySide6.QtWidgets import (QComboBox, QLabel, QLineEdit, QListWidget,
                               QMessageBox, QPushButton, QVBoxLayout, QWidget)

from .relatorio_window import RelatorioWindow


class CaixaWindow(QWidget):
    def __init__(self, pedidos_caixa, relatorio_diario):
        super().__init__()
        self.setWindowTitle("Caixa - Restaurante")
        self.layout = QVBoxLayout(self)

        # Inicializando variáveis
        self.pedidos_caixa = pedidos_caixa
        self.relatorio_diario = relatorio_diario
        self.valor_total = 0

        # Seção para selecionar cliente
        self.cliente_label = QLabel("Selecione o cliente para ver o pedido:")
        self.layout.addWidget(self.cliente_label)

        self.cliente_lista = QListWidget()
        self.cliente_lista.addItems(
            [cliente for cliente in self.pedidos_caixa.keys()])
        self.cliente_lista.clicked.connect(self.atualizar_total)
        self.layout.addWidget(self.cliente_lista)

        # Exibindo o total do pedido
        self.total_label = QLabel("Total do Pedido: R$ 0.00")
        self.layout.addWidget(self.total_label)

        # Campo para inserir o valor a cobrar
        self.input_valor = QLineEdit()
        self.input_valor.setPlaceholderText("Valor a Cobrar")
        self.layout.addWidget(self.input_valor)

        # Opção de método de pagamento
        self.payment_method_label = QLabel("Escolha o método de pagamento:")
        self.layout.addWidget(self.payment_method_label)

        self.payment_method = QComboBox(self)
        self.payment_method.addItems(["Dinheiro", "Pix", "Cartão"])
        self.layout.addWidget(self.payment_method)

        # Botão para finalizar o pagamento
        self.finalizar_button = QPushButton("Finalizar Pagamento")
        self.finalizar_button.clicked.connect(self.finalizar_pedido)
        self.layout.addWidget(self.finalizar_button)

    def atualizar_total(self):
        """Atualiza o total do pedido do cliente selecionado."""
        cliente_nome = self.cliente_lista.currentItem().text()
        if cliente_nome in self.pedidos_caixa:
            total = self.pedidos_caixa[cliente_nome]["total"]
            self.total_label.setText(f"Total do Pedido: R$ {total:.2f}")
            self.valor_total = total

    def finalizar_pedido(self):
        """Finaliza o pedido e registra o pagamento no relatório."""
        cliente_selecionado = self.cliente_lista.currentItem()
        if not cliente_selecionado:
            QMessageBox.warning(self, "Erro", "Selecione um cliente.")
            return

        cliente_nome = cliente_selecionado.text()
        if cliente_nome not in self.pedidos_caixa:
            QMessageBox.warning(
                self, "Erro", "Cliente não encontrado no caixa.")
            return

        try:
            valor_cobrado = float(self.input_valor.text())
        except ValueError:
            QMessageBox.warning(self, "Erro", "Insira um valor válido.")
            return

        if valor_cobrado < self.valor_total:
            QMessageBox.warning(
                self, "Erro", "Valor insuficiente para cobrir o total.")
            return

        metodo_pagamento = self.payment_method.currentText()
        troco = valor_cobrado - self.valor_total

        # Registrar no relatório
        self.relatorio_diario.append({
            "cliente": cliente_nome,
            "total": self.valor_total,
            "metodo_pagamento": metodo_pagamento,
            "troco": troco
        })

        # Exibir confirmação e abrir relatório
        QMessageBox.information(
            self, "Pagamento", f"Pagamento finalizado! Troco: R$ {troco:.2f}")
        self.abrir_relatorio()
        self.close()

    def abrir_relatorio(self):
        """Abre a interface de relatório diário."""
        self.relatorio_window = RelatorioWindow(self.relatorio_diario)
        self.relatorio_window.show()
