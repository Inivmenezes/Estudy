def adicionar_contato(contatos, nome, numero):
    contatos[nome] = numero
    print(f'Contato {nome} adicionado com sucesso.')

def remover_contato(contatos, nome):
    if nome in contatos:
        del contatos[nome]
        print(f'Contato {nome} removido com sucesso.')
    else:
        print(f'Contato {nome} não encontrado.')

def pesquisar_contato(contatos, nome):
    if nome in contatos:
        print(f'{nome}: {contatos[nome]}')
    else:
        print(f'Contato {nome} não encontrado.')

def listar_contatos(contatos):
    if contatos:
        print('Lista de contatos:')
        for nome, numero in contatos.items():
            print(f'{nome}: {numero}')
    else:
        print('A lista de contatos está vazia.')

def menu():
    contatos = {}
    while True:
        print("\nMenu:")
        print("1. Adicionar contato")
        print("2. Remover contato")
        print("3. Pesquisar contato")
        print("4. Listar contatos")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do contato: ")
            numero = input("Número de telefone: ")
            adicionar_contato(contatos, nome, numero)
        elif opcao == '2':
            nome = input("Nome do contato a ser removido: ")
            remover_contato(contatos, nome)
        elif opcao == '3':
            nome = input("Nome do contato a ser pesquisado: ")
            pesquisar_contato(contatos, nome)
        elif opcao == '4':
            listar_contatos(contatos)
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()