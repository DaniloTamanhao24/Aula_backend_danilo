import psycopg2 #Biblioteca que permite conexão com o PostgreSQL

def conectar():
    try:
        conexao = psycopg2.connect(
            dbname="minha_biblioteca",
            user="postgres",
            password="521344ldr",
            host="localhost",
            port="5432"
        )
        print("Conexão feita!")
        return conexao
    except Exception as erro:
        print(f"Erro ao conectar : {erro}")
        return None
    
def inserir_livro(conexao,livro):  #funcão para inserir livros
    try:
        cursor = conexao.cursor() #a query a seguir serve para inserir livros. Podemos fazer varias querys, seguindo a mesma estrutura

        insert_query = """ 
        INSERT INTO livros (titulo, autor ,ano_publicacao, num_paginas, qtd_capitulos, emprestado)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        valores = (livro.titulo, livro.autor, livro.ano_publicado, livro.num_paginas, livro.qtd_capitulos, livro.emprestado)
        cursor.execute(insert_query, valores) #executa a query
        conexao.commit() #persiste os dados no banco

        print(f"O livro '{livro.titulo}' foi inserido com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir o livro '{livro.titulo} : {str(e)}")
        conexao.rollback() #Reverte a transação em caso de erro


#Função para selecionar um livro com a query SELECT
def buscar_livros(conexao):
    try:
        cursor = conexao.cursor()
        select_query = "SELECT titulo, autor, ano_publicacao, num_paginas, qtd_capitulos, emprestado FROM livros"
        cursor.execute(select_query)
        livros = cursor.fetchall()
        if not livros :
            print("Não há livros cadastrados")
            return
        for livro in livros:
            titulo,autor,ano_publicacao, num_paginas, qtd_capitulos, emprestado = livro
            status_emprestimo = "Sim" if emprestado else "Não"
            print(f"Título: {titulo}, Autor: {autor}, Ano: {ano_publicacao}, Páginas: {num_paginas}, Capítulos: {qtd_capitulos}, Emprestado: {status_emprestimo}")
    except Exception as e:
        print(f"Erro ap buscar: {str (e)}")
