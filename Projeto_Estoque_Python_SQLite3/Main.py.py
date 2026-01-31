from services import cadastrar_produto, consultar_produto, listar_produtos


def menu():
    print("\n=== SISTEMA DE ESTOQUE ===")
    print("1 - Cadastrar produto")
    print("2 - Consultar produto")
    print("3 - Listar todos os produtos")
    print("4 - Sair")


while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "4":
         print("Sistema finalizado...")
         break

    if opcao == "1":
        nome = input("Nome do produto: ").lower()
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))
        promo = input("Está em promoção? (s/n): ").lower()

        promocao = 1 if promo == "s" else 0

        cadastrar_produto(nome, preco, quantidade, promocao)
        print("✅ Produto cadastrado com sucesso!")

    elif opcao == "2":
        nome = input("Nome do produto: ")
        produto = consultar_produto(nome)

        if produto:
            print(f"\nProduto: {produto['nome']}")
            print(f"Preço bruto: R$ {produto['preco']:.2f}")
            print(f"Desconto: R$ {produto['desconto']:.2f}")
            print(f"Preço final: R$ {produto['preco_final']:.2f}")
            print(f"Quantidade em estoque: {produto['quantidade']}")
        else:
            print("❌ Produto não encontrado.")

    elif opcao == "3":
        produtos = listar_produtos()

    if not produtos:
            print("Nenhum produto cadastrado.")
    else:
            print("\n=== PRODUTOS CADASTRADOS ===")
            for p in produtos:
                status = "Promoção" if p["promocao"] else "Normal"
                print(
                    f"- {p['nome']} | "
                    f"Preço: R$ {p['preco']:.2f} | "
                    f"Qtd: {p['quantidade']} | "
                    f"{status}"
                    )
