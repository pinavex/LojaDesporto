import json
import utils
from typing import List
from io import TextIOWrapper

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

def carregar_produtos(ficheiro_produto: str) -> List[Produto]:
    try:
        with open(ficheiro_produto, "r", encoding="utf-8") as file:
            assert isinstance(file, TextIOWrapper)  # Garantir que o tipo seja o esperado
            # Ler o conteúdo do ficheiro de forma robusta
            conteudo = file.read()
            if conteudo.strip():  # Se não estiver vazio
                produtos_json = json.loads(conteudo)
                return [Produto(**produto) for produto in produtos_json]
            return []  # Retorna lista vazia se o ficheiro estiver vazio
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Erro ao ler o ficheiro de produtos. O formato do arquivo pode estar corrompido.")
        return []

# Funções para manipular o arquivo de produtos
def gravar_produto(ficheiro_produto: str, lista_produtos: List[Produto]) -> None:
    with open(ficheiro_produto, "w", encoding="utf-8") as file:
        assert isinstance(file, TextIOWrapper)  # Garantir que o tipo seja o esperado
        json.dump([produto.__dict__ for produto in lista_produtos], file, ensure_ascii=False, indent=4)

produtos = carregar_produtos(utils.ficheiro_produto)  # Carregar os produtos

# Funções de manipulação de produtos
def criar_produto():
    while True:
        produto_id = utils.obter_input_numerico("Digite o ID do produto (somente números): ")
        if produto_id < 0:
            print("O ID do produto não pode ser negativo. Tente novamente.")
            continue
        if id_produto_existe(produto_id):
            print("ID do produto já existe. Tente novamente.")
            continue
        break

    nome = input("Digite o nome do produto: ")
    quantd = utils.obter_input_numerico("Digite a quantidade (somente números): ")
    preco = float(input("Digite o preço: "))
    categoria = input("Digite a categoria do produto: ")
    descricao = input("Digite a descrição do produto: ")

    novo_produto = Produto(produto_id=produto_id, nome=nome, quantd=quantd, preco=preco, categoria=categoria, descricao=descricao)
    produtos.append(novo_produto)
    gravar_produto(utils.ficheiro_produto, produtos)  # Gravar produtos no arquivo
    print(f"Produto {nome} criado com sucesso!")

def listar_produtos():
    if produtos:
        for produto in produtos:
            print(produto)
    else:
        print("Não há produtos cadastrados.")

def atualizar_produto():
    produto_id = utils.obter_input_numerico("Digite o ID do produto a ser atualizado: ")
    produto_atualizado = next((produto for produto in produtos if produto.produto_id == produto_id), None)

    if produto_atualizado:
        print(f"Produto encontrado: {produto_atualizado}")
        nome = input(f"Digite o nome do produto (atual: {produto_atualizado.nome}): ") or produto_atualizado.nome
        quantd = utils.obter_input_numerico(f"Digite a quantidade (atual: {produto_atualizado.quantd}): ") or produto_atualizado.quantd
        preco = float(input(f"Digite o preço (atual: {produto_atualizado.preco}): ") or produto_atualizado.preco)
        categoria = input(f"Digite a categoria (atual: {produto_atualizado.categoria}): ") or produto_atualizado.categoria
        descricao = input(f"Digite a descrição (atual: {produto_atualizado.descricao}): ") or produto_atualizado.descricao
        produto_atualizado.nome = nome
        produto_atualizado.quantd = quantd
        produto_atualizado.preco = preco
        produto_atualizado.categoria = categoria
        produto_atualizado.descricao = descricao
        gravar_produto(utils.ficheiro_produto, produtos)  # Gravar produtos no arquivo
        print(f"Produto {produto_atualizado.nome} atualizado com sucesso!")
    else:
        print("Produto não encontrado.")

def remover_produto():
    produto_id = utils.obter_input_numerico("Digite o ID do produto a ser removido: ")
    produto_removido = next((produto for produto in produtos if produto.produto_id == produto_id), None)

    if produto_removido:
        produtos.remove(produto_removido)
        gravar_produto(utils.ficheiro_produto, produtos)  # Gravar produtos no arquivo
        print(f"Produto {produto_removido.nome} removido com sucesso!")
    else:
        print("Produto não encontrado.")

# Funções para gravação e carregamento
def gravar_produtos():
    gravar_produto(utils.ficheiro_produto, produtos)


def id_produto_existe(produto_id):
    return any(produto.produto_id == produto_id for produto in produtos)
