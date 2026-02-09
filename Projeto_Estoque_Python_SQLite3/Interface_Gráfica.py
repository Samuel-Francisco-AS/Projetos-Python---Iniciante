# Importa o Tkinter com alias tk para criar a interface gráfica.
import tkinter as tk
# Importa caixas de diálogo e um widget de texto com rolagem.
from tkinter import messagebox, scrolledtext

# Importa funções de serviço que acessam e processam o estoque.
from services import cadastrar_produto, consultar_produto, listar_produtos


# ---------- FUNÇÕES ----------
# Define a ação do botão de cadastro.
def acao_cadastrar():
    # Inicia um bloco de tratamento de erros para validar entradas.
    try:
        # Obtém o nome do produto e converte para minúsculas.
        nome = entry_nome.get().lower()
        # Converte o preço digitado para float.
        preco = float(entry_preco.get())
        # Converte a quantidade digitada para inteiro.
        quantidade = int(entry_qtd.get())
        # Define promoção como 1 (sim) ou 0 (não) conforme o checkbox.
        promocao = 1 if var_promo.get() else 0

        # Chama a função de serviço para cadastrar o produto.
        cadastrar_produto(nome, preco, quantidade, promocao)
        # Exibe uma mensagem de sucesso ao usuário.
        messagebox.showinfo("OK", "Produto cadastrado!")

        # Limpa os campos do formulário após o cadastro.
        limpar_campos()

    # Captura qualquer exceção e exibe a mensagem de erro.
    except Exception as e:
        # Mostra a caixa de erro com o texto da exceção.
        messagebox.showerror("Erro", str(e))


# Define a ação do botão de consulta.
def acao_consultar():
    # Obtém o nome digitado para consulta.
    nome = entry_consulta.get().lower()
    # Chama a função de serviço para buscar o produto.
    produto = consultar_produto(nome)

    # Limpa o texto de saída antes de exibir novos resultados.
    output.delete("1.0", tk.END)

    # Se encontrou um produto, monta o texto detalhado.
    if produto:
        # Cria a string com dados formatados do produto.
        texto = (
            f"Produto: {produto['nome']}\n"
            f"Preço bruto: R$ {produto['preco']:.2f}\n"
            f"Desconto: R$ {produto['desconto']:.2f}\n"
            f"Preço final: R$ {produto['preco_final']:.2f}\n"
            f"Quantidade: {produto['quantidade']}\n"
        )
        # Insere o texto no widget de saída.
        output.insert(tk.END, texto)
    # Caso não encontre, informa ao usuário.
    else:
        # Escreve a mensagem de "não encontrado" na saída.
        output.insert(tk.END, "Produto não encontrado\n")


# Define a ação do botão de listar todos.
def acao_listar():
    # Obtém todos os produtos formatados do serviço.
    produtos = listar_produtos()

    # Limpa o texto de saída antes de exibir a lista.
    output.delete("1.0", tk.END)

    # Se a lista estiver vazia, informa e sai da função.
    if not produtos:
        # Mensagem para indicar que não há produtos.
        output.insert(tk.END, "Nenhum produto cadastrado\n")
        # Retorna para evitar continuar.
        return

    # Itera sobre cada produto para montar as linhas de exibição.
    for p in produtos:
        # Define o status baseado no campo promocao.
        status = "Promoçao" if p["promocao"] else "Normal"
        # Monta uma linha com os dados principais.
        linha = (
            f"{p['nome']} | "
            f"Preço: {p['preco']:.2f} | "
            f"Qtd: {p['quantidade']} | "
            f"{status}\n"
        )
        # Insere a linha no widget de saída.
        output.insert(tk.END, linha)


# Define a função que limpa os campos de entrada do formulário.
def limpar_campos():
    # Apaga o texto do campo de nome.
    entry_nome.delete(0, tk.END)
    # Apaga o texto do campo de preço.
    entry_preco.delete(0, tk.END)
    # Apaga o texto do campo de quantidade.
    entry_qtd.delete(0, tk.END)
    # Reseta o checkbox de promoção.
    var_promo.set(False)


# ---------- GUI ----------
# Cria a janela principal do Tkinter.
root = tk.Tk()
# Define o título da janela.
root.title("Sistema de Estoque")
# Define o tamanho inicial da janela.
root.geometry("500x500")


# Cria um frame para organizar os widgets.
frame = tk.Frame(root)
# Posiciona o frame com espaçamento vertical.
frame.pack(pady=10)


# Cadastro
# Cria rótulo para o campo Nome.
tk.Label(frame, text="Nome").grid(row=0, column=0)
# Cria a entrada de texto para Nome.
entry_nome = tk.Entry(frame)
# Posiciona o campo Nome na grade.
entry_nome.grid(row=0, column=1)

# Cria rótulo para o campo Preço.
tk.Label(frame, text="Preço").grid(row=1, column=0)
# Cria a entrada de texto para Preço.
entry_preco = tk.Entry(frame)
# Posiciona o campo Preço na grade.
entry_preco.grid(row=1, column=1)

# Cria rótulo para o campo Quantidade.
tk.Label(frame, text="Quantidade").grid(row=2, column=0)
# Cria a entrada de texto para Quantidade.
entry_qtd = tk.Entry(frame)
# Posiciona o campo Quantidade na grade.
entry_qtd.grid(row=2, column=1)

# Cria uma variável booleana para o checkbox de promoção.
var_promo = tk.BooleanVar()
# Cria o checkbox e associa à variável.
tk.Checkbutton(frame, text="Promoção", variable=var_promo).grid(row=3, columnspan=2)

# Cria o botão de cadastrar e associa à função de ação.
tk.Button(frame, text="Cadastrar", command=acao_cadastrar).grid(row=4, columnspan=2, pady=5)


# Consulta
# Cria rótulo para a seção de consulta.
tk.Label(frame, text="Consultar produto").grid(row=5, columnspan=2)
# Cria a entrada de texto para consulta.
entry_consulta = tk.Entry(frame)
# Posiciona o campo de consulta na grade.
entry_consulta.grid(row=6, columnspan=2)

# Cria o botão de consultar e associa à função de ação.
tk.Button(frame, text="Consultar", command=acao_consultar).grid(row=7, columnspan=2, pady=5)


# Listar
# Cria o botão para listar todos os produtos.
tk.Button(frame, text="Listar Todos", command=acao_listar).grid(row=8, columnspan=2)


# Output
# Cria o widget de texto com rolagem para exibir saídas.
output = scrolledtext.ScrolledText(root, width=60, height=15)
# Posiciona o widget de saída na janela.
output.pack(pady=10)


# Inicia o loop principal da interface gráfica.
root.mainloop()
