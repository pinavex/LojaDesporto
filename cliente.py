class Cliente:
    def __init__(self, id_cliente, nome, idade, email, telefone, data_nascimento):
        self.id_cliente = id_cliente
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
        self.data_nascimento = data_nascimento

    def __str__(self):
        return f"{self.id_cliente}, {self.nome}, {self.idade}, {self.email}, {self.telefone}, {self.data_nascimento}"

    @staticmethod
    def from_string(data_str):
        id_cliente, nome, idade, email, telefone, data_nascimento = data_str.strip().split(", ")
        return Cliente(int(id_cliente), nome, int(idade), email, telefone, data_nascimento)

