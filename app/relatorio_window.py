# app/relatorio_window.py

import pandas as pd
from fpdf import FPDF
from PySide6.QtWidgets import (QFileDialog, QLabel, QListWidget, QMessageBox,
                               QPushButton, QVBoxLayout, QWidget)


class RelatorioWindow(QWidget):
    def __init__(self, relatorio_diario):
        super().__init__()
        self.setWindowTitle("Relatório Diário - Restaurante")
        self.layout = QVBoxLayout(self)

        # Título do Relatório
        self.layout.addWidget(QLabel("Relatório Diário de Movimentações"))

        # Lista de relatórios de movimentação
        self.lista_relatorio = QListWidget()
        self.relatorio_diario = relatorio_diario

        # Exibindo as transações na lista
        self.exibir_relatorio()
        self.layout.addWidget(self.lista_relatorio)

        # Botão para exportar o relatório para PDF
        self.export_pdf_button = QPushButton("Exportar para PDF")
        self.export_pdf_button.clicked.connect(self.exportar_pdf)
        self.layout.addWidget(self.export_pdf_button)

        # Botão para exportar o relatório para Excel
        self.export_excel_button = QPushButton("Exportar para Excel")
        self.export_excel_button.clicked.connect(self.exportar_excel)
        self.layout.addWidget(self.export_excel_button)

    def exibir_relatorio(self):
        """Mostra o relatório na interface a partir do relatorio_diario fornecido."""
        for movimento in self.relatorio_diario:
            self.lista_relatorio.addItem(
                f"Cliente: {movimento['cliente']} - Total: R$ {movimento['total']:.2f} - "
                f"Método: {movimento['metodo_pagamento']} - Troco: R$ {movimento['troco']:.2f}"
            )

    def exportar_pdf(self):
        """Exporta o relatório diário para um arquivo PDF."""
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Salvar Relatório como PDF", "", "PDF Files (*.pdf)", options=options)

        if file_path:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", "B", 12)
            pdf.cell(200, 10, txt="Relatório Diário - Movimentação",
                     ln=True, align="C")
            pdf.set_font("Arial", size=10)

            for movimento in self.relatorio_diario:
                cliente = movimento['cliente']
                total = movimento['total']
                metodo_pagamento = movimento['metodo_pagamento']
                troco = movimento['troco']
                pdf.cell(200, 10, txt=f"Cliente: {cliente} - Total: R$ {total:.2f} - "
                                      f"Método: {metodo_pagamento} - Troco: R$ {troco:.2f}", ln=True)

            pdf.output(file_path)
            QMessageBox.information(
                self, "Exportação Completa", "Relatório exportado como PDF com sucesso.")

    def exportar_excel(self):
        """Exporta o relatório diário para um arquivo Excel."""
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Salvar Relatório como Excel", "", "Excel Files (*.xlsx)", options=options)

        if file_path:
            # Convertendo o relatório para um DataFrame do Pandas
            df = pd.DataFrame(self.relatorio_diario)
            df.to_excel(file_path, index=False)
            QMessageBox.information(
                self, "Exportação Completa", "Relatório exportado como Excel com sucesso.")
