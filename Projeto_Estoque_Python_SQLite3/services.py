from Database import adicionar_produto, buscar_produto


def cadastrar_produto(nome, preco, quantidade, promocao):
    adicionar_produto(nome, preco, quantidade, promocao)


def calcular_desconto(preco, promocao):
    if promocao:
        return preco * 0.20
    elif preco >= 100:
        return preco * 0.10
    else:
        return 0


def consultar_produto(nome):
    produto = buscar_produto(nome)

    if produto:
        nome, preco, quantidade, promocao = produto
        desconto = calcular_desconto(preco, promocao)
        preco_final = preco - desconto

        return {
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade,
            "desconto": desconto,
            "preco_final": preco_final
        }

    return None