import produto
from cliente import criar_cliente, listar_clientes, gravar_cliente, carregar_clientes
from persistencia import (carregar_compras
)

ficheiro_cliente = "clientes.txt"
ficheiro_compras = "compras.txt"

clientes = carregar_clientes(ficheiro_cliente)  # Carregar os clientes
compras = carregar_compras(ficheiro_compras)  # Carregar as compras

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
                produto.criar_produto()
            elif opcao_produto == "2":
                produto.listar_produtos()
            elif opcao_produto == "3":
                produto.listar_produtos()
                produto.atualizar_produto()
            elif opcao_produto == "4":
                produto.listar_produtos()
                produto.remover_produto()
            elif opcao_produto == "5":
                continue

        elif opcao == "2":
            print("\n1. Criar Cliente")
            print("2. Listar Clientes")
            print("3. Voltar")
            opcao_cliente = input("Escolha uma opção: ")

            if opcao_cliente == "1":
                criar_cliente(clientes, ficheiro_cliente)
            elif opcao_cliente == "2":
                listar_clientes(clientes)
            elif opcao_cliente == "3":
                continue

        elif opcao == "3":
            print("\n1. Criar Compra")
            print("2. Voltar")
            opcao_compra = input("Escolha uma opção: ")

            if opcao_compra == "1":
                listar_clientes(clientes)
                from compra import criar_compra
                criar_compra(clientes)
            elif opcao_compra == "2":
                continue

        elif opcao == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

menu()









