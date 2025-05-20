import datetime
import re

ficheiro_produto = "produtos.txt"
ficheiro_compras = "compras.txt"


def obter_input_numerico(mensagem):
    while True:
        valor = input(mensagem)
        if valor.isdigit():
            return int(valor)
        else:
            print("Entrada inválida. Digite um número inteiro.")


# Funções de validação e utilidade
def calcular_idade(data_nascimento):
    data_nascimento = datetime.datetime.strptime(data_nascimento, "%d/%m/%Y")
    hoje = datetime.datetime.today()
    return hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))


def email_valido(email):
    padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(padrao, email) is not None


def email_existe(email, lista_clientes):
    return any(cliente.email == email for cliente in lista_clientes)


def telefone_existe(telefone, lista_clientes):
    return any(cliente.telefone == telefone for cliente in lista_clientes)


def id_cliente_existe(id_cliente, lista_clientes):
    return any(cliente.id_cliente == id_cliente for cliente in lista_clientes)


# Função para validar o método de pagamento
def validar_metodo_pagamento(cliente, produto_selecionado, quantidade, lista_compras, produto, gravar_produto,
                             gravar_compra):
    metodos_validos = ["dinheiro", "cartão de crédito", "cartão de débito", "transferência bancária", "mbway"]

    while True:
        metodo_pagamento = input(
            "Digite o método de pagamento (dinheiro, cartão de crédito, cartão de débito, transferência bancária, mbway): ").lower()

        # Verificando se o método de pagamento é válido e sem números ou símbolos
        if metodo_pagamento in metodos_validos and metodo_pagamento.isalpha():
            break
        else:
            print(
                "Método de pagamento inválido. Tente novamente com um dos seguintes métodos: dinheiro, cartão de crédito, cartão de débito, transferência bancária, mbway.")

    preco_total = quantidade * produto_selecionado.preco
    compra = {
        "cliente": cliente.nome,
        "produto": produto_selecionado.nome,
        "quantidade": quantidade,
        "preco_total": preco_total,
        "metodo_pagamento": metodo_pagamento
    }

    lista_compras.append(compra)
    produto_selecionado.quantd -= quantidade
    gravar_produto(ficheiro_produto, produto)  # Atualizando o estoque
    gravar_compra(ficheiro_compras, lista_compras)  # Gravar compras no arquivo
    print(f"Compra realizada com sucesso! Total: {preco_total}.")


