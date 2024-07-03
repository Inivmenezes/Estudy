def main():
    biblioteca = {}  
    nome = input("Qual seu nome? ")
    print("Bem-Vindo à sua Biblioteca virtual, {}!".format(nome))

    while True:
        print("\nOpções:")
        print("1. Adicionar um livro à biblioteca.")
        print("2. Buscar um livro na biblioteca.")
        print("3. Remover um livro da biblioteca.")
        print("4. Mostrar a quantidade de livros na biblioteca.")
        print("5. Mostrar todos os livros da biblioteca.")
        print("6. Sair.")

        opcao = input("{}, para prosseguir escolha uma das opções: ".format(nome))

        if opcao == "1":
            titulo = input("Digite um título que queira adicionar: ")
            biblioteca[titulo] = True  
            print(f"{titulo} foi adicionado à biblioteca.")
        elif opcao == "2":
            titulo_busca = input("Digite o título que você deseja buscar: ")
            if titulo_busca in biblioteca:
                print(f"{titulo_busca} está na biblioteca.")
            else:
                print(f"{titulo_busca} não está na biblioteca.")
        elif opcao == "3":
            titulo_remover = input("Digite o título que você quer remover: ")
            if titulo_remover in biblioteca:
                del biblioteca[titulo_remover]
                print(f"{titulo_remover} foi removido da biblioteca.")
            else:
                print(f"{titulo_remover} não está na biblioteca.")
        elif opcao == "4":
            print(f"A biblioteca contém {len(biblioteca)} livros.")
        elif opcao == "5":
            print("Títulos na biblioteca:")
            for titulo in biblioteca:
                print(titulo)
        elif opcao == "6":
            print("Fechando a Biblioteca.")
            break
        else:
            print("Opção inválida. Escolha uma opção válida.")

if __name__ == "__main__":
    main()
