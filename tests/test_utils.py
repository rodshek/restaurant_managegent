import os
import unittest

from app.utils import carregar_dados, salvar_dados


class TestUtils(unittest.TestCase):
    def setUp(self):
        """Configuração inicial dos testes."""
        self.dados = {"clientes": [
            {"nome": "Carlos", "mesa": "Mesa 1", "pedidos": []}]}
        self.caminho_arquivo = "test_dados.json"

    def test_salvar_dados(self):
        """Teste para salvar dados no arquivo."""
        salvar_dados(self.dados, self.caminho_arquivo)
        self.assertTrue(os.path.exists(self.caminho_arquivo))

    def test_carregar_dados(self):
        """Teste para carregar dados de um arquivo."""
        salvar_dados(self.dados, self.caminho_arquivo)
        dados_carregados = carregar_dados(self.caminho_arquivo)
        self.assertEqual(dados_carregados, self.dados)

    def tearDown(self):
        """Limpeza após os testes."""
        if os.path.exists(self.caminho_arquivo):
            os.remove(self.caminho_arquivo)


if __name__ == "__main__":
    unittest.main()
