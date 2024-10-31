from livros import livro,biblioteca 
from db_connection import conectar, inserir_livro, buscar_livros



def adicionar_livros():
    print("Adicionar Livros: ")
    ano_publicado = int(input("Digite o ano de publicação: "))
    autor = input("Digite o autor do livro : ")
    titulo = input("Titulo do livro : ")
    num_paginas = int(input("Número de páginas: "))
    emprestado = input("O livro está emprestado ? (s/n): ").lower() == 's'
    qtd_capitulos = int(input("Digite a quantidade de cápitulos: "))

    novo_livro = livro(ano_publicado, autor, titulo, num_paginas, emprestado, qtd_capitulos)
    return novo_livro

conexao = conectar()

if conexao:
    Biblioteca = biblioteca("Minha biblioteca")
    while True:
        print("\n1. Adicionar livro \n2. Mostrar livros cadastrados \n3. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            novo_livro = adicionar_livros()
            Biblioteca.adicionar_livro(novo_livro)
            inserir_livro(conexao, novo_livro)
        
        elif opcao == '2':
            print("\nLivros cadastrados: ")
            
            buscar_livros(conexao)
        elif opcao == '3':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida, tente novamente")
    conexao.close()



#Biblioteca.adicionar_livro(livro1)
#Biblioteca.mostrar_livros()
#livro1 = livro(1853, "Álvares de Azevedo", "Lira dos vinte anos,",208,True,10)