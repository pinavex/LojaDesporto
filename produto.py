class Produto:
    def __init__(self, produto_id, nome, quantd, preco, categoria, descricao):
        self.produto_id = produto_id
        self.nome = nome
        self.quantd = quantd
        self.preco = preco
        self.categoria = categoria
        self.descricao = descricao

    def __str__(self):
        return f"{self.produto_id}, {self.nome}, {self.quantd}, {self.preco}, {self.categoria}, {self.descricao}"

    @staticmethod
    def from_string(data_str):
        produto_id, nome, quantd, preco, categoria, descricao = data_str.strip().split(", ")
        return Produto(int(produto_id), nome, int(quantd), float(preco), categoria, descricao)
