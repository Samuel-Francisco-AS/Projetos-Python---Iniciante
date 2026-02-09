# Importa funções do módulo Database e renomeia listar_produtos para evitar conflito de nome.
from Database import adicionar_produto, buscar_produto, listar_produtos as listar_produtos_db


# Define a função de service que encapsula o cadastro do produto.
def cadastrar_produto(nome, preco, quantidade, promocao):
    # Chama a função de inserção no banco com os parametros recebidos.
    adicionar_produto(nome, preco, quantidade, promocao)


# Define a função que calcula o desconto baseado em regras de promoção e preço.
def calcular_desconto(preco, promocao):
    # Inicializa o desconto com zero, assumindo sem desconto.
    desconto = 0

    # Se estiver em promoção, aplica 20% de desconto.
    if promocao:
        desconto = preco * 0.20
    # Se não estiver em promoção, mas preco >= 100, aplica 20%.
    elif preco >= 100:
        desconto = max(desconto, preco * 0.20)

    # Retorna o valor calculado do desconto.
    return desconto


# Define a função que consulta um produto e devolve dados processados.
def consultar_produto(nome):
    # Busca o produto no banco pelo nome.
    produto = buscar_produto(nome)

    # Se houver produto encontrado, processa os dados.
    if produto:
        # Desempacota a tupla retornada pelo banco.
        nome, preco, quantidade, promocao = produto
        # Calcula o desconto conforme as regras.
        desconto = calcular_desconto(preco, promocao)
        # Calcula o preço final subtraindo o desconto.
        preco_final = preco - desconto

        # Retorna um dicionário com dados prontos para a interface.
        return {
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade,
            "desconto": desconto,
            "preco_final": preco_final
        }

    # Retorna None quando o produto não é encontrado.
    return None

# Define a função que lista todos os produtos formatados.
def listar_produtos():
    # Gera a variável com a lista crua (tuplas) diretamente do banco.
    produtos = listar_produtos_db()

    # Inicializa a lista que irá conter os dicionários formatados.
    lista_formatada = []

    # Itera sobre cada produto retornado do banco.
    for produto in produtos:
        # Desempacota a tupla em variaveis.
        nome, preco, quantidade, promocao = produto
        # Adiciona um dicionário com chaves nomeadas na lista final.
        lista_formatada.append({
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade,
            "promocao": promocao
        })

    # Retorna a lista de dicionários.
    return lista_formatada
