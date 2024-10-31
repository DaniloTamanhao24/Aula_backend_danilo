class biblioteca :
    nome = ""

    def __init__(self,nome):
        self.catalogo = []
        self.nome = nome

    def adicionar_livro(self,livro):
        self.catalogo.append(livro)
        print(f"O livro {livro.titulo}, do autor {livro.autor} foi inserido")

    def mostrar_livros(self):
        if not self.catalogo:
            print("Não há livros cadastrados.")
        for livro in self.catalogo:
            print(f"Livro {livro.titulo} , Cadastrado com sucesso.")

class livro:
    ano_publicado = 0
    autor = ""
    titulo = ""
    num_paginas = 0
    emprestado = False
    qtd_capitulos = 0


    def __init__(self,ano_publicado,autor,titulo,num_paginas,emprestado,qtd_capitulos):
        self.ano_publicado = ano_publicado
        self.autor = autor
        self.titulo = titulo
        self.num_paginas = num_paginas
        self.emprestado =  emprestado
        self.qtd_capitulos = qtd_capitulos

    def emprestar(self):
        self.emprestado = True
    def devolver(self):
        self.emprestado = False

    def descrever(self):
        print("-"*20)
        print(f"Titulo do Livro : {self.titulo}")
        print(f"Ano de publicação : {self.ano_publicado}")
        print(f"Numero de capitulos : {self.qtd_capitulos}")
        print(f"Numero de páginas : {self.num_paginas}")
        print(f" Autor :{self.autor}")
        print("-"*20)
        if self.emprestado == True:
            print("O livro está emprestado")
        else:
            print("O livro está dísponivel")



