import json
from produto import Produto
from cliente import Cliente
from typing import List
from io import TextIOWrapper

# Funções para manipular o arquivo de produtos
def gravar_produto(ficheiro_produto: str, produtos: List[Produto]) -> None:
    with open(ficheiro_produto, "w", encoding="utf-8") as file:
        assert isinstance(file, TextIOWrapper)  # Garantir que o tipo seja o esperado
        json.dump([produto.__dict__ for produto in produtos], file, ensure_ascii=False)

def carregar_produtos(ficheiro_produto: str) -> List[Produto]:
    try:
        with open(ficheiro_produto, "r", encoding="utf-8") as file:
            assert isinstance(file, TextIOWrapper)  # Garantir que o tipo seja o esperado
            # Ler o conteúdo do ficheiro de forma robusta
            conteudo = file.read()
            if conteudo.strip():  # Se não estiver vazio
                produtos = json.loads(conteudo)
                return [Produto(**produto) for produto in produtos]
            return []  # Retorna lista vazia se o ficheiro estiver vazio
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Erro ao ler o ficheiro de produtos. O formato do arquivo pode estar corrompido.")
        return []

# Funções para manipular o arquivo de clientes
def gravar_cliente(ficheiro_cliente: str, clientes: List[Cliente]) -> None:
    with open(ficheiro_cliente, "w", encoding="utf-8") as file:
        assert isinstance(file, TextIOWrapper)  # Garantir que o tipo seja o esperado
        json.dump([cliente.__dict__ for cliente in clientes], file, ensure_ascii=False)

def carregar_clientes(ficheiro_cliente: str) -> List[Cliente]:
    try:
        with open(ficheiro_cliente, "r", encoding="utf-8") as file:
            assert isinstance(file, TextIOWrapper)  # Garantir que o tipo seja o esperado
            conteudo = file.read()
            if conteudo.strip():
                clientes = json.loads(conteudo)
                return [Cliente(**cliente) for cliente in clientes]
            return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Erro ao ler o ficheiro de clientes. O formato do arquivo pode estar corrompido.")
        return []

# Funções para manipular o arquivo de compras
def gravar_compra(ficheiro_compras: str, compras: List[dict]) -> None:
    with open(ficheiro_compras, "w", encoding="utf-8") as file:
        assert isinstance(file, TextIOWrapper)  # Garantir que o tipo seja o esperado
        json.dump(compras, file, ensure_ascii=False)

def carregar_compras(ficheiro_compras: str) -> List[dict]:
    try:
        with open(ficheiro_compras, "r", encoding="utf-8") as file:
            assert isinstance(file, TextIOWrapper)  # Garantir que o tipo seja o esperado
            conteudo = file.read()
            if conteudo.strip():
                compras = json.loads(conteudo)
                return compras
            return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Erro ao ler o ficheiro de compras. O formato do arquivo pode estar corrompido.")
        return []
