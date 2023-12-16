import mysql.connector


def conectar_banco():
    host = 'localhost'
    usuario = 'COLOQUE SEU USUARIO DO BANCO'
    senha = 'COLOQUE SUA SENHA DE USUARIO'
    banco_dados = 'loja'

    conexao = mysql.connector.connect(
        host=host,
        user=usuario,
        password=senha,
        database=banco_dados
    )

    return conexao


def exibir_menu():
    print("\n*** MENU ***")
    print("1. CRUD Cliente")
    print("2. CRUD Estoque")
    print("3. Relatório: Consumo Médio dos Clientes")
    print("4. Relatório: Produtos Mais Vendidos")
    print("5. Relatório: Produtos de Baixo Estoque")
    print("6. Sair")


def crud_cliente(conexao):
    while True:
        print("\n*** CRUD Cliente ***")
        print("1. Criar Cliente")
        print("2. Ler Clientes")
        print("3. Atualizar Cliente")
        print("4. Deletar Cliente")
        print("5. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção (1-5): ")

        if opcao == '1':
            criar_cliente(conexao)
        elif opcao == '2':
            ler_clientes(conexao)
        elif opcao == '3':
            atualizar_cliente(conexao)
        elif opcao == '4':
            deletar_cliente(conexao)
        elif opcao == '5':
            print("Voltando ao Menu Principal.")
            break
        else:
            print("Opção inválida. Tente novamente.")


def criar_cliente(conexao):
    cursor = conexao.cursor()
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o e-mail do cliente: ")

    # Inserir novo cliente no banco de dados
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (%s, %s)", (nome, email))
    conexao.commit()

    print("Cliente criado com sucesso!")


def ler_clientes(conexao):
    cursor = conexao.cursor()

    # Selecionar todos os clientes
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    # Exibir os clientes
    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        print("\n--- Clientes Cadastrados ---")
        for cliente in clientes:
            print(f"ID: {cliente[0]}, Nome: {cliente[1]}, E-mail: {cliente[2]}")


def atualizar_cliente(conexao):
    cursor = conexao.cursor()
    ler_clientes(conexao)

    # Solicitar o ID do cliente a ser atualizado
    id_cliente = input("Digite o ID do cliente que deseja atualizar: ")

    # Verificar se o cliente existe
    cursor.execute("SELECT * FROM clientes WHERE id = %s", (id_cliente,))
    cliente = cursor.fetchone()

    if cliente:
        novo_nome = input("Digite o novo nome do cliente: ")
        novo_email = input("Digite o novo e-mail do cliente: ")

        # Atualizar as informações do cliente no banco de dados
        cursor.execute("UPDATE clientes SET nome = %s, email = %s WHERE id = %s", (novo_nome, novo_email, id_cliente))
        conexao.commit()

        print("Cliente atualizado com sucesso!")
    else:
        print("Cliente não encontrado.")


def deletar_cliente(conexao):
    cursor = conexao.cursor()
    ler_clientes(conexao)

    # Solicitar o ID do cliente a ser deletado
    id_cliente = input("Digite o ID do cliente que deseja deletar: ")

    # Verificar se o cliente existe
    cursor.execute("SELECT * FROM clientes WHERE id = %s", (id_cliente,))
    cliente = cursor.fetchone()

    if cliente:
        # Deletar o cliente do banco de dados
        cursor.execute("DELETE FROM clientes WHERE id = %s", (id_cliente,))
        conexao.commit()

        print("Cliente deletado com sucesso!")
    else:
        print("Cliente não encontrado.")


def crud_estoque(conexao):
    while True:
        print("\n*** CRUD Estoque ***")
        print("1. Adicionar Produto ao Estoque")
        print("2. Ler Produtos no Estoque")
        print("3. Atualizar Informações do Produto")
        print("4. Remover Produto do Estoque")
        print("5. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção (1-5): ")

        if opcao == '1':
            adicionar_produto_estoque(conexao)
        elif opcao == '2':
            ler_produtos_estoque(conexao)
        elif opcao == '3':
            atualizar_produto_estoque(conexao)
        elif opcao == '4':
            remover_produto_estoque(conexao)
        elif opcao == '5':
            print("Voltando ao Menu Principal.")
            break
        else:
            print("Opção inválida. Tente novamente.")


def adicionar_produto_estoque(conexao):
    cursor = conexao.cursor()
    nome_produto = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade a ser adicionada ao estoque: "))

    # Adicionar produto ao estoque
    cursor.execute("UPDATE produtos SET estoque = estoque + %s WHERE nome = %s", (quantidade, nome_produto))
    conexao.commit()

    print(f"{quantidade} unidades do produto {nome_produto} adicionadas ao estoque.")


def ler_produtos_estoque(conexao):
    cursor = conexao.cursor()

    # Selecionar todos os produtos no estoque
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    # Exibir os produtos no estoque
    if not produtos:
        print("Nenhum produto no estoque.")
    else:
        print("\n--- Produtos no Estoque ---")
        for produto in produtos:
            print(f"ID: {produto[0]}, Nome: {produto[1]}, Estoque: {produto[2]}, Quantidade Vendida: {produto[3]}")


def atualizar_produto_estoque(conexao):
    cursor = conexao.cursor()
    ler_produtos_estoque(conexao)

    # Solicitar o ID do produto a ser atualizado
    id_produto = input("Digite o ID do produto que deseja atualizar: ")

    # Verificar se o produto existe
    cursor.execute("SELECT * FROM produtos WHERE id = %s", (id_produto,))
    produto = cursor.fetchone()

    if produto:
        novo_nome = input("Digite o novo nome do produto: ")
        novo_estoque = int(input("Digite o novo estoque do produto: "))
        nova_quantidade_vendida = int(input("Digite a nova quantidade vendida do produto: "))

        # Atualizar as informações do produto no banco de dados
        cursor.execute("UPDATE produtos SET nome = %s, estoque = %s, quantidadeVendida = %s WHERE id = %s",
                       (novo_nome, novo_estoque, nova_quantidade_vendida, id_produto))
        conexao.commit()

        print("Produto atualizado com sucesso!")
    else:
        print("Produto não encontrado.")


def remover_produto_estoque(conexao):
    cursor = conexao.cursor()
    ler_produtos_estoque(conexao)

    # Solicitar o ID do produto a ser removido
    id_produto = input("Digite o ID do produto que deseja remover: ")

    # Verificar se o produto existe
    cursor.execute("SELECT * FROM produtos WHERE id = %s", (id_produto,))
    produto = cursor.fetchone()

    if produto:
        # Remover o produto do estoque
        cursor.execute("DELETE FROM produtos WHERE id = %s", (id_produto,))
        conexao.commit()

        print("Produto removido do estoque com sucesso!")
    else:
        print("Produto não encontrado.")


def relatorio_consumo_medio_clientes(conexao):
    cursor = conexao.cursor()

    # Selecionar a média de consumo dos clientes
    cursor.execute("""
        SELECT clientes.id, clientes.nome, AVG(produtos.quantidadeVendida) AS consumo_medio
        FROM clientes
        LEFT JOIN produtos ON clientes.id = produtos.id
        GROUP BY clientes.id, clientes.nome
    """)
    relatorio = cursor.fetchall()

    # Exibir o relatório de consumo médio dos clientes
    if not relatorio:
        print("Nenhum dado disponível para gerar o relatório de consumo médio dos clientes.")
    else:
        print("\n--- Relatório de Consumo Médio dos Clientes ---")
        for linha in relatorio:
            print(f"ID: {linha[0]}, Nome: {linha[1]}, Consumo Médio: {linha[2]:.2f}")

    cursor.close()


def relatorio_produtos_mais_vendidos(conexao):
    cursor = conexao.cursor()

    # Selecionar os produtos mais vendidos
    cursor.execute("""
        SELECT id, nome, quantidadeVendida
        FROM produtos
        ORDER BY quantidadeVendida DESC
    """)
    relatorio = cursor.fetchall()

    # Exibir o relatório de produtos mais vendidos
    if not relatorio:
        print("Nenhum dado disponível para gerar o relatório de produtos mais vendidos.")
    else:
        print("\n--- Relatório de Produtos Mais Vendidos ---")
        for linha in relatorio:
            print(f"ID: {linha[0]}, Nome: {linha[1]}, Quantidade Vendida: {linha[2]}")

    cursor.close()


def relatorio_produtos_baixo_estoque(conexao):
    cursor = conexao.cursor()

    # Selecionar os produtos com estoque igual ou menor que 10
    cursor.execute("""
        SELECT id, nome, estoque
        FROM produtos
        WHERE estoque <= 10
    """)
    relatorio = cursor.fetchall()

    # Exibir o relatório de produtos de baixo estoque
    if not relatorio:
        print("Nenhum dado disponível para gerar o relatório de produtos de baixo estoque.")
    else:
        print("\n--- Relatório de Produtos de Baixo Estoque ---")
        for linha in relatorio:
            print(f"ID: {linha[0]}, Nome: {linha[1]}, Estoque: {linha[2]}")

    cursor.close()


# Programa principal
while True:
    exibir_menu()
    opcao = input("Escolha uma opção (1-6): ")

    if opcao == '1':
        crud_cliente(conectar_banco())
    elif opcao == '2':
        crud_estoque(conectar_banco())
    elif opcao == '3':
        relatorio_consumo_medio_clientes(conectar_banco())
    elif opcao == '4':
        relatorio_produtos_mais_vendidos(conectar_banco())
    elif opcao == '5':
        relatorio_produtos_baixo_estoque(conectar_banco())
    elif opcao == '6':
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
