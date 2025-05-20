# cliente.py
import utils
from typing import List
from io import TextIOWrapper
import json

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

# Manipulação de ficheiros
def gravar_cliente(ficheiro_cliente: str, clientes: List[Cliente]) -> None:
    with open(ficheiro_cliente, "w", encoding="utf-8") as file:
        assert isinstance(file, TextIOWrapper)
        json.dump([cliente.__dict__ for cliente in clientes], file, ensure_ascii=False, indent=4)

def carregar_clientes(ficheiro_cliente: str) -> List[Cliente]:
    try:
        with open(ficheiro_cliente, "r", encoding="utf-8") as file:
            assert isinstance(file, TextIOWrapper)
            conteudo = file.read()
            if conteudo.strip():
                clientes = json.loads(conteudo)
                return [Cliente(**cliente) for cliente in clientes]
            return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Erro ao ler o ficheiro de clientes.")
        return []
