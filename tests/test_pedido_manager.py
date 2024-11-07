import unittest

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QTableWidgetItem

from app.pedido_manager import PedidoManager


class TestPedidoManager(unittest.TestCase):
    def setUp(self):
        """Configuração inicial dos testes."""
        self.app = QApplication([])
        self.pedido_manager = PedidoManager()

    def test_adicionar_cliente(self):
        """Teste para adicionar um cliente e seu pedido."""
        self.pedido_manager.adicionar_cliente("Mesa 1", "Carlos")
        self.assertEqual(len(self.pedido_manager.clientes), 1)
        self.assertEqual(self.pedido_manager.clientes[0]['nome'], "Carlos")

    def test_adicionar_produto(self):
        """Teste para adicionar um pedido a um cliente existente."""
        self.pedido_manager.adicionar_cliente("Mesa 2", "Fernanda")
        self.pedido_manager.adicionar_pedido(0, "Lanche", 2)
        self.assertEqual(len(self.pedido_manager.clientes[0]['pedidos']), 1)
        self.assertEqual(
            self.pedido_manager.clientes[0]['pedidos'][0]['produto'], "Lanche")

    def test_remover_pedido(self):
        """Teste para remover um pedido de um cliente."""
        self.pedido_manager.adicionar_cliente("Mesa 3", "João")
        self.pedido_manager.adicionar_pedido(0, "Dog", 1)
        self.pedido_manager.remover_pedido(0, 0)
        self.assertEqual(len(self.pedido_manager.clientes[0]['pedidos']), 0)

    def test_enviar_pedido_para_caixa(self):
        """Teste para enviar um pedido ao caixa."""
        self.pedido_manager.adicionar_cliente("Mesa 4", "Mariana")
        self.pedido_manager.adicionar_pedido(0, "Espetinho", 3)
        self.pedido_manager.enviar_pedido_para_caixa(0)
        self.assertEqual(len(self.pedido_manager.pedidos_enviados), 1)
        self.assertEqual(
            self.pedido_manager.pedidos_enviados[0]['produto'], "Espetinho")


if __name__ == "__main__":
    unittest.main()
