import utils
import produto

class Compra:
    def __init__(self, cliente, prod, quantidade, tamanho, preco, metodo_pagamento, troco=0):
        self.cliente = cliente
        self.produto = prod
        self.quantidade = quantidade
        self.tamanho = tamanho
        self.preco = preco
        self.metodo_pagamento = metodo_pagamento
        self.troco = troco

    def __str__(self):
        return f"Cliente: {self.cliente}, Produto: {self.produto}, Quantidade: {self.quantidade}, Tamanho: {self.tamanho}, Preço: {self.preco}, Método de Pagamento: {self.metodo_pagamento}, Troco: {self.troco}"

    @classmethod
    def from_string(cls, data_str):
        campos = data_str.strip().split(", ")
        cliente = campos[0].split(": ")[1]
        produto_str = campos[1].split(": ")[1]  # Renomeado para produto_str para evitar conflito
        quantidade = int(campos[2].split(": ")[1])
        tamanho = campos[3].split(": ")[1]
        preco = float(campos[4].split(": ")[1])
        metodo_pagamento = campos[5].split(": ")[1]
        troco = float(campos[6].split(": ")[1]) if len(campos) > 6 else 0
        return cls(cliente, produto_str, quantidade, tamanho, preco, metodo_pagamento, troco)

def criar_compra(clientes):
    id_cliente = utils.obter_input_numerico("Digite o ID do cliente: ")
    cliente = next((cliente for cliente in clientes if cliente.id_cliente == id_cliente), None)

    if not cliente:
        print("Cliente não encontrado.")
        return

    id_produto = utils.obter_input_numerico("Digite o ID do produto: ")
    produtos = produto.carregar_produtos(utils.ficheiro_produto)

    meu_prod = None
    for prod in produtos:
        if prod.produto_id == id_produto:
            meu_prod = prod

    if not meu_prod:
        print("Produto não encontrado.")
        return

    quantidade = utils.obter_input_numerico("Digite a quantidade: ")
    if quantidade > meu_prod.quantd:
        print(f"Quantidade indisponível. Temos apenas {meu_prod.quantd} unidades.")
        return
