from produto import Produto
from cliente import Cliente
from persistencia import gravar_produto, carregar_produtos, gravar_cliente, carregar_clientes
import re
from datetime import datetime

ficheiro_produto = "produtos.txt"
ficheiro_cliente = "clientes.txt"
produtos = []
clientes = []

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

    while True:
        quantd = obter_input_numerico("Digite a quantidade (somente números): ")
        if quantd < 0:
            print("A quantidade não pode ser negativa. Tente novamente.")
            continue
        break

    while True:
        try:
            preco = float(input("Digite o preço: "))
            if preco < 0:
                print("O preço não pode ser negativo. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Digite um valor numérico para o preço.")

    categoria = input("Digite a categoria do produto: ")
    descricao = input("Digite a descrição do produto: ")

    novo_produto = Produto(produto_id, nome, quantd, preco, categoria, descricao)
    produtos.append(novo_produto)
    print(f"Produto {nome} criado com sucesso!")

def listar_produtos():
    if produtos:
        for produto in produtos:
            print(produto)
    else:
        print("Não há produtos cadastrados.")

def criar_cliente():
    while True:
        id_cliente = obter_input_numerico("Digite o ID do cliente (somente números): ")
        if id_cliente < 0:
            print("O ID do cliente não pode ser negativo. Tente novamente.")
            continue
        if id_cliente_existe(id_cliente):
            print("ID do cliente já existe. Tente novamente.")
            continue
        break

    nome = input("Digite o nome do cliente: ")

    while True:
        email = input("Digite o email do cliente: ")
        if not email_valido(email):
            print("Email inválido. Tente novamente.")
            continue
        if email_existe(email):
            print("Email já cadastrado. Tente novamente.")
            continue
        break

    while True:
        telefone = input("Digite o telefone do cliente: ")
        if telefone_existe(telefone):
            print("Telefone já cadastrado. Tente novamente.")
            continue
        break

    while True:
        data_nascimento = input("Digite a data de nascimento do cliente (dd/mm/aaaa): ")
        try:
            idade = calcular_idade(data_nascimento)
            if idade < 16:
                print("O cliente deve ter pelo menos 16 anos. Tente novamente.")
                continue
            break
        except ValueError:
            print("Data de nascimento inválida. Tente novamente.")

    novo_cliente = Cliente(id_cliente, nome, idade, email, telefone, data_nascimento)
    clientes.append(novo_cliente)
    print(f"Cliente {nome} criado com sucesso!")

def listar_clientes():
    if clientes:
        for cliente in clientes:
            print(cliente)
    else:
        print("Não há clientes cadastrados.")

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

def menu():
    while True:
        print("\n1. Menu Produtos")
        print("2. Menu Clientes")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_produtos()
        elif opcao == "2":
            menu_clientes()
        elif opcao == "3":
            break
        else:
            print("Opção inválida, tente novamente.")

def menu_produtos():
    while True:
        print("\n1. Criar Produto")
        print("2. Listar Produtos")
        print("3. Gravar Produtos")
        print("4. Carregar Produtos")
        print("5. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            gravar_produtos()
        elif opcao == "4":
            carregar_produtos_banco()
        elif opcao == "5":
            break
        else:
            print("Opção inválida, tente novamente.")

def menu_clientes():
    while True:
        print("\n1. Criar Cliente")
        print("2. Listar Clientes")
        print("3. Gravar Clientes")
        print("4. Carregar Clientes")
        print("5. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            gravar_clientes()
        elif opcao == "4":
            carregar_clientes_banco()
        elif opcao == "5":
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()







