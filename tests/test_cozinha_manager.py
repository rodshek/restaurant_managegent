# tests/test_report_manager.py

import unittest

from PySide6.QtWidgets import QApplication

from app.report_manager import ReportManager

app = QApplication([])


class TestReportManager(unittest.TestCase):
    def setUp(self):
        self.report_manager = ReportManager()

    def test_exibir_grafico_exemplo(self):
        # Verifica se o canvas é configurado e o título do gráfico é adicionado
        self.report_manager.exibir_grafico_exemplo()
        ax = self.report_manager.canvas.figure.axes[0]
        self.assertEqual(ax.get_title(), "Gráfico de Exemplo")


if __name__ == '__main__':
    unittest.main()
