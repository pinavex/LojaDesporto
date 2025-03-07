class Compra:
    def __init__(self, cliente, produto, quantidade, tamanho, preco, metodo_pagamento, troco=0):
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade
        self.tamanho = tamanho
        self.preco = preco
        self.metodo_pagamento = metodo_pagamento
        self.troco = troco

    def __str__(self):
        return f"Cliente: {self.cliente}, Produto: {self.produto}, Quantidade: {self.quantidade}, Tamanho: {self.tamanho}, Preço: {self.preco}, Método de Pagamento: {self.metodo_pagamento}, Troco: {self.troco}"

    @classmethod
    def from_string(cls, data_str):
        # Supondo que o formato de string seja consistente para recriar a classe
        campos = data_str.strip().split(", ")
        cliente = campos[0].split(": ")[1]
        produto = campos[1].split(": ")[1]
        quantidade = int(campos[2].split(": ")[1])
        tamanho = campos[3].split(": ")[1]
        preco = float(campos[4].split(": ")[1])
        metodo_pagamento = campos[5].split(": ")[1]
        troco = float(campos[6].split(": ")[1]) if len(campos) > 6 else 0
        return cls(cliente, produto, quantidade, tamanho, preco, metodo_pagamento, troco)
