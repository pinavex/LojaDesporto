from produto import Produto
from cliente import Cliente

def gravar_produto(ficheiro, lista_produtos):
    with open(ficheiro, "w") as f:
        for produto in lista_produtos:
            f.write(str(produto) + "\n")
    print(f"Produtos gravados em {ficheiro} com sucesso!")

def carregar_produtos(ficheiro):
    produtos = []
    try:
        with open(ficheiro, "r") as f:
            for linha in f:
                produto = Produto.from_string(linha)
                produtos.append(produto)
        print(f"Produtos carregados de {ficheiro} com sucesso!")
    except FileNotFoundError:
        print(f"O ficheiro {ficheiro} não foi encontrado.")
    return produtos

def gravar_cliente(ficheiro, lista_clientes):
    with open(ficheiro, "w") as f:
        for cliente in lista_clientes:
            f.write(str(cliente) + "\n")
    print(f"Clientes gravados em {ficheiro} com sucesso!")

def carregar_clientes(ficheiro):
    clientes = []
    try:
        with open(ficheiro, "r") as f:
            for linha in f:
                cliente = Cliente.from_string(linha)
                clientes.append(cliente)
        print(f"Clientes carregados de {ficheiro} com sucesso!")
    except FileNotFoundError:
        print(f"O ficheiro {ficheiro} não foi encontrado.")
    return clientes



