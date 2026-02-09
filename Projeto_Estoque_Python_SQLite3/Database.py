# Importa o módulo sqlite3 para trabalhar com banco de dados SQLite.
import sqlite3
# Importa o módulo os para lidar com caminhos de arquivo e diretórios.
import os

# Define a função responsável por abrir conexão com o banco.
def conectar():
    # Define o diretório base do arquivo atual (pasta onde este script está).
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # Monta o caminho completo do arquivo do banco de dados SQLite.
    DB_PATH = os.path.join(BASE_DIR, "Estoque.db")
    # Abre e retorna a conexão com o banco de dados.
    return sqlite3.connect(DB_PATH)

# Define a função que cria a tabela de produtos se ela ainda não existir.
def criar_tabela():
    # Abre a conexão com o banco.
    conexao = conectar()
    # Cria um cursor para executar comandos SQL.
    cursor = conexao.cursor()

    # Executa o comando SQL para criar a tabela produtos com campos definidos.
    cursor.execute (""" 
                   CREATE TABLE IF NOT EXISTS produtos
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    preco REAL NOT NULL,
                    quantidade INTEGER NOT NULL,
                    promocao INTEGER NOT NULL
                    )
                    """)

    # Confirma (salva) as alterações no banco.
    conexao.commit() 
    # Fecha a conexão com o banco.
    conexao.close() 

# Bloco executado apenas quando o arquivo é rodado diretamente.
if __name__ == "__main__":
    # Chama a criação da tabela ao executar este arquivo como script.
    criar_tabela()

# Define a função que insere um produto no banco de dados.
def adicionar_produto(nome, preco, quantidade, promocao):
    """
    Insere um novo produto no banco de dados.
    promocao: 1 = sim | 0 = nÃ£o
    """
    # Abre a conexão com o banco.
    conexao = conectar()
    # Cria um cursor para executar SQL.
    cursor = conexao.cursor()

    # Executa um INSERT com parâmetros para evitar SQL injection.
    cursor.execute("""
        INSERT INTO produtos (nome, preco, quantidade, promocao)
        VALUES (?, ?, ?, ?)
    """, (nome, preco, quantidade, promocao))

    # Confirma a inserção no banco.
    conexao.commit()
    # Fecha a conexão com o banco.
    conexao.close()


# Define a função que busca um produto pelo nome.
def buscar_produto(nome):
    """
    Busca um produto pelo nome.
    Retorna uma tupla ou None.
    """
    # Abre a conexão com o banco.
    conexao = conectar()
    # Cria um cursor para executar SQL.
    cursor = conexao.cursor()

    # Executa um SELECT filtrando pelo nome informado.
    cursor.execute("""
        SELECT nome, preco, quantidade, promocao
        FROM produtos
        WHERE nome = ?
    """, (nome,))

    # Obtém a primeira linha encontrada (ou None).
    produto = cursor.fetchone()
    # Fecha a conexão com o banco.
    conexao.close()
    # Retorna a tupla com os dados do produto (ou None).
    return produto


# Define a função que lista todos os produtos do banco.
def listar_produtos():
    """
    Retorna todos os produtos cadastrados.
    """
    # Abre a conexão com o banco.
    conexao = conectar()
    # Cria um cursor para executar SQL.
    cursor = conexao.cursor()

    # Executa um SELECT para trazer todos os produtos.
    cursor.execute("""
        SELECT nome, preco, quantidade, promocao
        FROM produtos
    """)

    # Busca todas as linhas retornadas.
    produtos = cursor.fetchall()
    # Fecha a conexão com o banco.
    conexao.close()
    # Retorna a lista de tuplas com os dados.
    return produtos

# Esse bloco sÃ³ roda quando o arquivo Ã© executado diretamente
if __name__ == "__main__":
    # Garante a tabela criada antes de qualquer uso interativo.
    criar_tabela()
    # Mensagem de confirmaÃ§Ã£o no console.
    print("Banco de dados e tabela 'produtos' prontos para uso.")
