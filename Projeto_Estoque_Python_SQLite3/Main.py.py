
produtos = [
    {"nome": "monitor", "preco": 400,"promocao": True},
    {"nome": "filtro de linha","preco": 120,"promocao": False},
     {"nome": "headset","preco": 200,"promocao": False},
      {"nome": "soundbar","preco": 300,"promocao": True},
]

while True:

    print('\n1 - Digite o nome do produto que deseja verificar:')
    print('2 - Sair')

    opcao = int(input('Selecione sua opção:'))

    if opcao == 1:
        print('\nProdutos disponíveis:')
        for produto in produtos:
            print(f'{produto["nome"]}')

        nome_escolhido = input('\nDigite o nome do produto:').lower()
        encontrado = False

        for produto in produtos:
                if produto["nome"] == nome_escolhido:
                    encontrado = True

                    preco = produto["preco"]

                    if preco >= 100 and not produto["promocao"]:
                        desconto = preco * 0.10
                    elif produto["promocao"]:
                        desconto = preco * 0.20
                    else:
                        desconto = 0
                    
                    preco_final = preco - desconto

                    print('\nDetalhes do produto:')
                    print(f'Produto: {produto["nome"]}')
                    print(f'Preço bruto: R$ {preco:.2f}')
                    print(f'O desconto aplicável é de: R$ {desconto:.2f}')
                    print(f'O valor de um(a) {produto["nome"]} com desconto é: R$ {preco_final:.2f}')
                    break

    elif opcao == 2:
        print('encerrando sistema...')

    else:
        print('Produto inválido!')

