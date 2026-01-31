import sqlite3
import os

def conectar():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.join(BASE_DIR, "Estoque.db")
    return sqlite3.connect(DB_PATH)

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute (""" 
                   CREATE TABLE IF NOT EXISTS produtos
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    preco REAL NOT NULL,
                    quantidade INTEGER NOT NULL,
                    promocao INTEGER NOT NULL
                    )
                    """)

    conexao.commit() 
    conexao.close() 

if __name__ == "__main__":
    criar_tabela()

def adicionar_produto(nome, preco, quantidade, promocao):
    """
    Insere um novo produto no banco de dados.
    promocao: 1 = sim | 0 = não
    """
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO produtos (nome, preco, quantidade, promocao)
        VALUES (?, ?, ?, ?)
    """, (nome, preco, quantidade, promocao))

    conexao.commit()
    conexao.close()


def buscar_produto(nome):
    """
    Busca um produto pelo nome.
    Retorna uma tupla ou None.
    """
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT nome, preco, quantidade, promocao
        FROM produtos
        WHERE nome = ?
    """, (nome,))

    produto = cursor.fetchone()
    conexao.close()
    return produto


def listar_produtos():
    """
    Retorna todos os produtos cadastrados.
    """
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT nome, preco, quantidade, promocao
        FROM produtos
    """)

    produtos = cursor.fetchall()
    conexao.close()
    return produtos

def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT nome, preco, quantidade, promocao
        FROM produtos
    """)

    produtos = cursor.fetchall()
    conexao.close()
    return produtos

# Esse bloco só roda quando o arquivo é executado diretamente
if __name__ == "__main__":
    criar_tabela()
    print("Banco de dados e tabela 'produtos' prontos para uso.")