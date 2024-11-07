# app/relatorio_diario_window.py

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class RelatorioDiarioWindow(QWidget):
    def __init__(self, relatorio_diario):
        super().__init__()
        self.setWindowTitle("Relatório Diário")
        self.layout = QVBoxLayout(self)

        self.relatorio_label = QLabel(self)
        self.layout.addWidget(self.relatorio_label)
        self.relatorio_diario = relatorio_diario
        self.exibir_relatorio()

    def exibir_relatorio(self):
        """Exibe o relatório diário na interface."""
        relatorio_texto = ""
        for item in self.relatorio_diario:
            relatorio_texto += (
                f"Cliente: {item['cliente']} (Mesa {item['mesa']})\n"
                f"Total: R$ {item['total']:.2f}\n"
                f"Método de Pagamento: {item['metodo_pagamento']}\n\n"
            )
        self.relatorio_label.setText(relatorio_texto)
