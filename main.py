from produto import Produto
from cliente import Cliente
from persistencia import (
    gravar_produto, carregar_produtos, gravar_cliente, carregar_clientes,
    gravar_compra, carregar_compras
)
import re
from datetime import datetime

ficheiro_produto = "produtos.txt"
ficheiro_cliente = "clientes.txt"
ficheiro_compras = "compras.txt"
produtos = []
clientes = []
compras = carregar_compras(ficheiro_compras)  # Carregando as compras diretamente aqui

# Funções de validação e utilidade
def calcular_idade(data_nascimento):
    data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    hoje = datetime.today()
    return hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))

def email_valido(email):
    padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(padrao, email) is not None

def email_existe(email):
    return any(cliente.email == email for cliente in clientes)

def telefone_existe(telefone):
    return any(cliente.telefone == telefone for cliente in clientes)

def id_cliente_existe(id_cliente):
    return any(cliente.id_cliente == id_cliente for cliente in clientes)

def id_produto_existe(produto_id):
    return any(produto.produto_id == produto_id for produto in produtos)

def obter_input_numerico(mensagem):
    while True:
        valor = input(mensagem)
        if valor.isdigit():
            return int(valor)
        else:
            print("Entrada inválida. Digite um número inteiro.")

# Funções de manipulação de produtos
def criar_produto():
    while True:
        produto_id = obter_input_numerico("Digite o ID do produto (somente números): ")
        if produto_id < 0:
            print("O ID do produto não pode ser negativo. Tente novamente.")
            continue
        if id_produto_existe(produto_id):
            print("ID do produto já existe. Tente novamente.")
            continue
        break

    nome = input("Digite o nome do produto: ")
    quantd = obter_input_numerico("Digite a quantidade (somente números): ")
    preco = float(input("Digite o preço: "))
    categoria = input("Digite a categoria do produto: ")
    descricao = input("Digite a descrição do produto: ")

    novo_produto = Produto(produto_id=produto_id, nome=nome, quantd=quantd, preco=preco, categoria=categoria, descricao=descricao)
    produtos.append(novo_produto)
    print(f"Produto {nome} criado com sucesso!")

def listar_produtos():
    if produtos:
        for produto in produtos:
            print(produto)
    else:
        print("Não há produtos cadastrados.")

def atualizar_produto():
    produto_id = obter_input_numerico("Digite o ID do produto que deseja atualizar: ")
    produto_encontrado = next((produto for produto in produtos if produto.produto_id == produto_id), None)

    if produto_encontrado:
        print(f"Produto encontrado: {produto_encontrado}")
        produto_encontrado.nome = input(f"Digite o novo nome do produto (atual: {produto_encontrado.nome}): ")
        produto_encontrado.quantd = obter_input_numerico(f"Digite a nova quantidade (atual: {produto_encontrado.quantd}): ")
        produto_encontrado.preco = float(input(f"Digite o novo preço (atual: {produto_encontrado.preco}): "))
        produto_encontrado.categoria = input(f"Digite a nova categoria (atual: {produto_encontrado.categoria}): ")
        produto_encontrado.descricao = input(f"Digite a nova descrição (atual: {produto_encontrado.descricao}): ")
        print(f"Produto {produto_encontrado.nome} atualizado com sucesso!")
    else:
        print("Produto não encontrado.")

def remover_produto():
    produto_id = obter_input_numerico("Digite o ID do produto que deseja remover: ")
    produto_encontrado = next((produto for produto in produtos if produto.produto_id == produto_id), None)

    if produto_encontrado:
        produtos.remove(produto_encontrado)
        print(f"Produto {produto_encontrado.nome} removido com sucesso!")
    else:
        print("Produto não encontrado.")

# Funções de manipulação de clientes
def criar_cliente():
    while True:
        id_cliente = obter_input_numerico("Digite o ID do cliente (somente números): ")
        if id_cliente_existe(id_cliente):
            print("ID do cliente já existe. Tente novamente.")
            continue
        break

    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente (somente números): ")
    data_nascimento = input("Digite a data de nascimento do cliente (dd/mm/aaaa): ")
    idade = calcular_idade(data_nascimento)

    novo_cliente = Cliente(id_cliente=id_cliente, nome=nome, idade=idade, email=email, telefone=telefone, data_nascimento=data_nascimento)
    clientes.append(novo_cliente)
    print(f"Cliente {nome} criado com sucesso!")

def listar_clientes():
    if clientes:
        for cliente in clientes:
            print(cliente)
    else:
        print("Não há clientes cadastrados.")

# Funções de manipulação de compras
def criar_compra():
    id_cliente = obter_input_numerico("Digite o ID do cliente: ")
    cliente = next((cliente for cliente in clientes if cliente.id_cliente == id_cliente), None)

    if not cliente:
        print("Cliente não encontrado.")
        return

    id_produto = obter_input_numerico("Digite o ID do produto: ")
    produto = next((produto for produto in produtos if produto.produto_id == id_produto), None)

    if not produto:
        print("Produto não encontrado.")
        return

    quantidade = obter_input_numerico("Digite a quantidade: ")
    if quantidade > produto.quantd:
        print(f"Quantidade indisponível. Temos apenas {produto.quantd} unidades.")
        return

    metodo_pagamento = input("Digite o método de pagamento: ")

    preco_total = quantidade * produto.preco
    compra = {
        "cliente": cliente.nome,
        "produto": produto.nome,
        "quantidade": quantidade,
        "preco_total": preco_total,
        "metodo_pagamento": metodo_pagamento
    }

    compras.append(compra)
    produto.quantd -= quantidade
    gravar_produtos()
    gravar_compra(ficheiro_compras, compras)
    print(f"Compra realizada com sucesso! Total: {preco_total}.")

# Funções para gravação e carregamento
def gravar_produtos():
    gravar_produto(ficheiro_produto, produtos)

def carregar_produtos_banco():
    global produtos
    produtos = carregar_produtos(ficheiro_produto)

def gravar_clientes():
    gravar_cliente(ficheiro_cliente, clientes)

def carregar_clientes_banco():
    global clientes
    clientes = carregar_clientes(ficheiro_cliente)

# Menu principal
def menu():
    while True:
        print("\n1. Menu Produtos")
        print("2. Menu Clientes")
        print("3. Menu Compras")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n1. Criar Produto")
            print("2. Listar Produtos")
            print("3. Atualizar Produto")
            print("4. Remover Produto")
            print("5. Voltar")
            opcao_produto = input("Escolha uma opção: ")

            if opcao_produto == "1":
                criar_produto()
                gravar_produtos()
            elif opcao_produto == "2":
                listar_produtos()
            elif opcao_produto == "3":
                atualizar_produto()
                gravar_produtos()
            elif opcao_produto == "4":
                remover_produto()
                gravar_produtos()
            elif opcao_produto == "5":
                continue

        elif opcao == "2":
            print("\n1. Criar Cliente")
            print("2. Listar Clientes")
            print("3. Voltar")
            opcao_cliente = input("Escolha uma opção: ")

            if opcao_cliente == "1":
                criar_cliente()
                gravar_clientes()
            elif opcao_cliente == "2":
                listar_clientes()
            elif opcao_cliente == "3":
                continue

        elif opcao == "3":
            print("\n1. Criar Compra")
            print("2. Voltar")
            opcao_compra = input("Escolha uma opção: ")

            if opcao_compra == "1":
                criar_compra()
            elif opcao_compra == "2":
                continue

        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Carregando dados no início do programa
carregar_produtos_banco()
carregar_clientes_banco()

menu()










