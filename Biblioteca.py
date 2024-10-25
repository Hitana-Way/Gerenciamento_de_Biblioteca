biblioteca = ['O Pequeno Príncipe', 'Romeu E Julieta', 'Quarto de Despejo', 'Veronika Decide Morrer', 'O Corvo']

def registrar_livro(livro):
    if livro not in biblioteca:
        biblioteca.append(livro)
        print("O livro: " + livro + " foi registrado com sucesso!")
    else:
        print("O livro já está registrado na biblioteca.")

def emprestar_livro(livro):
    if livro in biblioteca:
        biblioteca.remove(livro)
        print("O livro: " + livro + " foi emprestado.")
    else:
        print("O livro: " + livro + " não está disponível na nossa biblioteca!")

def devolver_livro(livro):
    if livro not in biblioteca:
        biblioteca.append(livro)
        print("O livro: " + livro + " foi devolvido!")
    else:
        print("O livro já está na biblioteca.")

def consultar_livros():
    if len(biblioteca) > 0:
        print("Livros disponíveis na biblioteca: ")
        for livro in biblioteca:
            print(livro)
    else:
        print("A biblioteca está vazia.")

def trocar_livro(livro_para_troca, livro_trocado):
    if livro_para_troca in biblioteca:
        biblioteca.remove(livro_para_troca)
        biblioteca.append(livro_trocado)
        print("O livro " + livro_para_troca + " foi trocado por " + livro_trocado + ".")
    else:
        print("Livro " + livro_para_troca + " não encontrado na biblioteca para troca!")

def GerenciamentoBiblioteca():
    continuar = True

    while continuar:
        print("\nDigite a opção desejada: \n1. Registrar livros \n2. Emprestar livros \n3. Devolver livros \n4. Consultar livros disponíveis \n5. Trocar livros \n0. Sair do sistema")
        opcao = input()

        if opcao == "1":
            livro_registrado = input("Digite o nome do livro que deseja registrar: ")
            registrar_livro(livro_registrado)

        elif opcao == "2":
            livro_emprestado = input("Digite o nome do livro que deseja pegar emprestado: ")
            emprestar_livro(livro_emprestado)

        elif opcao == "3":
            livro_devolver = input("Digite o nome do livro que deseja devolver: ")
            devolver_livro(livro_devolver)

        elif opcao == "4":
            consultar_livros()
        
        elif opcao == "5":
            livro_para_troca = input("Digite o nome do livro que você desejar receber: ")
            livro_trocado = input("Digite o nome do livro que você deseja ofertar em troca: ")
            trocar_livro(livro_para_troca, livro_trocado)

        elif opcao == "0":
            print("Programa Finalizado")
            continuar = False
        else:
            print("Opção inválida.")

GerenciamentoBiblioteca()
