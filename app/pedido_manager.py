# app/pedido_manager.py

from PySide6.QtWidgets import (QHBoxLayout, QLabel, QLineEdit, QListWidget,
                               QMessageBox, QPushButton, QSpinBox, QVBoxLayout,
                               QWidget)

# Importando a CaixaWindow para uso na tela de pedidos
from .caixa_window import CaixaWindow


class PedidoManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Pedidos - Restaurante")
        self.layout = QVBoxLayout(self)

        # Inicializando pedidos_caixa como um dicionário vazio
        self.pedidos_caixa = {}

        # Lista para armazenar o relatório diário
        self.relatorio_diario = []

        # Dicionário para armazenar clientes e pedidos
        self.clientes = {}

        # Preços dos itens
        self.precos = {
            "Refri": 5,
            "Cerveja": 5,
            "Lanche": 10,
            "Dog": 10,
            "Espetinho 7": 7,
            "Espetinho 5": 5
        }

        # Seção 1: Entrada do Cliente
        self.section_cliente = QVBoxLayout()
        self.layout.addLayout(self.section_cliente)

        self.input_mesa = QLineEdit(self)
        self.input_mesa.setPlaceholderText("Número da Mesa")
        self.input_cliente = QLineEdit(self)
        self.input_cliente.setPlaceholderText("Nome do Cliente")
        self.add_cliente_button = QPushButton("Adicionar Cliente")
        self.add_cliente_button.clicked.connect(self.adicionar_cliente)

        self.section_cliente.addWidget(QLabel("Entrada do Cliente"))
        self.section_cliente.addWidget(self.input_mesa)
        self.section_cliente.addWidget(self.input_cliente)
        self.section_cliente.addWidget(self.add_cliente_button)

        # Lista de Clientes
        self.lista_clientes = QListWidget()
        self.lista_clientes.clicked.connect(self.mostrar_pedidos_cliente)
        self.layout.addWidget(QLabel("Clientes:"))
        self.layout.addWidget(self.lista_clientes)

        # Seção 2: Inserção de Pedido
        self.section_pedido = QVBoxLayout()
        self.layout.addLayout(self.section_pedido)
        self.section_pedido.addWidget(QLabel("Inserir Pedido"))

        # Adicionando botões e campos de quantidade para os produtos
        for produto in self.precos.keys():
            self.adicionar_secao_pedido(produto)

        # Seção 3: Resumo do Pedido do Cliente
        self.section_resumo = QVBoxLayout()
        self.layout.addLayout(self.section_resumo)
        self.section_resumo.addWidget(QLabel("Resumo do Pedido"))

        self.resumo_pedidos = QListWidget()
        self.section_resumo.addWidget(self.resumo_pedidos)

        # Botão para excluir o pedido selecionado
        self.delete_pedido_button = QPushButton("Excluir Pedido Selecionado")
        self.delete_pedido_button.clicked.connect(
            self.excluir_pedido_selecionado)
        self.section_resumo.addWidget(self.delete_pedido_button)

        # Seção 4: Enviar Pedido para o Caixa
        self.section_envio = QVBoxLayout()
        self.layout.addLayout(self.section_envio)

        self.section_envio.addWidget(QLabel("Enviar Pedido para o Caixa"))

        self.envio_cliente_button = QPushButton(
            "Enviar Pedido Selecionado para o Caixa")
        self.envio_cliente_button.clicked.connect(self.enviar_para_caixa)
        self.section_envio.addWidget(self.envio_cliente_button)

        # Botão para abrir o caixa
        self.abrir_caixa_button = QPushButton("Abrir Caixa")
        self.abrir_caixa_button.clicked.connect(self.abrir_caixa)
        self.layout.addWidget(self.abrir_caixa_button)

    def adicionar_secao_pedido(self, produto):
        """Cria uma linha de inserção de produto com quantidade e preço."""
        produto_layout = QHBoxLayout()

        label_produto = QLabel(f"{produto} - R${self.precos[produto]}")
        spinbox_quantidade = QSpinBox()
        spinbox_quantidade.setRange(1, 20)
        adicionar_produto_button = QPushButton(f"Adicionar {produto}")
        adicionar_produto_button.clicked.connect(
            lambda _, p=produto, s=spinbox_quantidade: self.adicionar_pedido(
                p, s.value())
        )

        produto_layout.addWidget(label_produto)
        produto_layout.addWidget(spinbox_quantidade)
        produto_layout.addWidget(adicionar_produto_button)
        self.section_pedido.addLayout(produto_layout)

    def adicionar_cliente(self):
        mesa = self.input_mesa.text()
        cliente = self.input_cliente.text()
        if mesa and cliente:
            if cliente not in self.clientes:
                self.clientes[cliente] = {
                    "mesa": mesa, "pedidos": [], "total": 0, "status": "aberto"}
                self.lista_clientes.addItem(f"{cliente} - Mesa {mesa}")
                self.input_mesa.clear()
                self.input_cliente.clear()
            else:
                QMessageBox.warning(self, "Erro", "Cliente já cadastrado.")
        else:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos.")

    def adicionar_pedido(self, produto, quantidade):
        cliente_selecionado = self.lista_clientes.currentItem()
        if cliente_selecionado:
            cliente_nome = cliente_selecionado.text().split(" - ")[0]
            if cliente_nome in self.clientes:
                pedido = f"{produto} (x{quantidade})"
                valor_total = self.precos[produto] * quantidade
                self.clientes[cliente_nome]["pedidos"].append(
                    (pedido, valor_total))
                self.clientes[cliente_nome]["total"] += valor_total
                QMessageBox.information(
                    self, "Pedido", f"{pedido} adicionado para {cliente_nome}. Total: R${valor_total}")
                self.mostrar_pedidos_cliente()
        else:
            QMessageBox.warning(
                self, "Erro", "Selecione um cliente para adicionar o pedido.")

    def mostrar_pedidos_cliente(self):
        """Mostra os pedidos do cliente selecionado na lista de resumo, incluindo o valor total."""
        self.resumo_pedidos.clear()
        cliente_selecionado = self.lista_clientes.currentItem()
        if cliente_selecionado:
            cliente_nome = cliente_selecionado.text().split(" - ")[0]
            pedidos = self.clientes[cliente_nome]["pedidos"]
            total = self.clientes[cliente_nome]["total"]
            for pedido, valor in pedidos:
                self.resumo_pedidos.addItem(f"{pedido} - R${valor}")
            self.resumo_pedidos.addItem(f"Total: R${total}")

    def excluir_pedido_selecionado(self):
        """Exclui o pedido selecionado no resumo do cliente."""
        cliente_selecionado = self.lista_clientes.currentItem()
        pedido_selecionado = self.resumo_pedidos.currentItem()
        if cliente_selecionado and pedido_selecionado:
            cliente_nome = cliente_selecionado.text().split(" - ")[0]
            pedido_texto = pedido_selecionado.text().split(" - ")[0]
            if cliente_nome in self.clientes:
                for pedido, valor in self.clientes[cliente_nome]["pedidos"]:
                    if pedido == pedido_texto:
                        self.clientes[cliente_nome]["pedidos"].remove(
                            (pedido, valor))
                        self.clientes[cliente_nome]["total"] -= valor
                        break
                self.mostrar_pedidos_cliente()
                QMessageBox.information(
                    self, "Pedido", f"{pedido_texto} removido para {cliente_nome}.")
        else:
            QMessageBox.warning(
                self, "Erro", "Selecione um pedido para remover.")

    def enviar_para_caixa(self):
        """Envia o pedido do cliente selecionado para o caixa."""
        cliente_selecionado = self.lista_clientes.currentItem()
        if cliente_selecionado:
            cliente_nome = cliente_selecionado.text().split(" - ")[0]
            if cliente_nome in self.clientes:
                # Adiciona o cliente no dicionário de pedidos do caixa e marca como 'enviado'
                self.pedidos_caixa[cliente_nome] = self.clientes[cliente_nome]
                self.pedidos_caixa[cliente_nome]["status"] = "enviado para o caixa"

                # Remove o cliente da lista ativa de pedidos na tela de pedidos
                self.lista_clientes.takeItem(self.lista_clientes.currentRow())
                del self.clientes[cliente_nome]

                QMessageBox.information(
                    self, "Caixa", f"Pedido de {cliente_nome} enviado para o caixa.")
        else:
            QMessageBox.warning(
                self, "Erro", "Selecione um cliente para enviar o pedido para o caixa.")

    def abrir_caixa(self):
        """Abre a interface do caixa para gerenciar os pedidos enviados."""
        self.caixa_window = CaixaWindow(
            self.pedidos_caixa, self.relatorio_diario)
        self.caixa_window.show()
