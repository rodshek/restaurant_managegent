import unittest

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QTableWidgetItem

from app.caixa_window import CaixaWindow


class TestCaixaWindow(unittest.TestCase):
    def setUp(self):
        """Configuração inicial dos testes."""
        self.app = QApplication([])
        self.caixa_window = CaixaWindow()

    def test_visualizar_pedidos_no_caixa(self):
        """Teste para verificar se pedidos enviados ao caixa são listados corretamente."""
        # Simula o envio de um pedido
        self.caixa_window.adicionar_pedido_no_caixa("Mesa 5", "Bebida", 2)
        self.assertEqual(len(self.caixa_window.pedidos), 1)
        self.assertEqual(self.caixa_window.pedidos[0]['produto'], "Bebida")

    def test_marcar_pedido_como_pago(self):
        """Teste para marcar um pedido como pago no caixa."""
        self.caixa_window.adicionar_pedido_no_caixa("Mesa 6", "Lanche", 1)
        self.caixa_window.marcar_como_pago(0)
        self.assertTrue(self.caixa_window.pedidos[0]['pago'])


if __name__ == "__main__":
    unittest.main()
