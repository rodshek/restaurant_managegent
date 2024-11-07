# tests/test_estoque_manager.py

import unittest

from PySide6.QtWidgets import QApplication

from app.estoque_manager import EstoqueManager

app = QApplication([])


class TestEstoqueManager(unittest.TestCase):
    def setUp(self):
        self.estoque_manager = EstoqueManager()

    def test_adicionar_item_estoque(self):
        self.estoque_manager.adicionar_item_estoque("Arroz", 50)
        self.assertEqual(self.estoque_manager.lista_estoque.count(), 1)
        self.assertIn("Arroz - Quantidade: 50",
                      self.estoque_manager.lista_estoque.item(0).text())

    def test_atualizar_quantidade_item(self):
        self.estoque_manager.adicionar_item_estoque("Feijão", 30)
        self.estoque_manager.atualizar_quantidade_item("Feijão", 40)
        self.assertIn("Feijão - Quantidade: 40",
                      self.estoque_manager.lista_estoque.item(0).text())


if __name__ == '__main__':
    unittest.main()
