import tkinter as tk
from tkinter import messagebox, scrolledtext

from services import cadastrar_produto, consultar_produto, listar_produtos


# ---------- FUNÇÕES ----------
def acao_cadastrar():
    try:
        nome = entry_nome.get().lower()
        preco = float(entry_preco.get())
        quantidade = int(entry_qtd.get())
        promocao = 1 if var_promo.get() else 0

        cadastrar_produto(nome, preco, quantidade, promocao)
        messagebox.showinfo("OK", "Produto cadastrado!")

        limpar_campos()

    except Exception as e:
        messagebox.showerror("Erro", str(e))


def acao_consultar():
    nome = entry_consulta.get()
    produto = consultar_produto(nome)

    output.delete("1.0", tk.END)

    if produto:
        texto = (
            f"Produto: {produto['nome']}\n"
            f"Preço bruto: R$ {produto['preco']:.2f}\n"
            f"Desconto: R$ {produto['desconto']:.2f}\n"
            f"Preço final: R$ {produto['preco_final']:.2f}\n"
            f"Quantidade: {produto['quantidade']}\n"
        )
        output.insert(tk.END, texto)
    else:
        output.insert(tk.END, "Produto não encontrado\n")


def acao_listar():
    produtos = listar_produtos()

    output.delete("1.0", tk.END)

    if not produtos:
        output.insert(tk.END, "Nenhum produto cadastrado\n")
        return

    for p in produtos:
        status = "Promoção" if p["promocao"] else "Normal"
        linha = (
            f"{p['nome']} | "
            f"Preço: {p['preco']:.2f} | "
            f"Qtd: {p['quantidade']} | "
            f"{status}\n"
        )
        output.insert(tk.END, linha)


def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    entry_qtd.delete(0, tk.END)
    var_promo.set(False)


# ---------- GUI ----------
root = tk.Tk()
root.title("Sistema de Estoque")
root.geometry("500x500")


frame = tk.Frame(root)
frame.pack(pady=10)


# Cadastro
tk.Label(frame, text="Nome").grid(row=0, column=0)
entry_nome = tk.Entry(frame)
entry_nome.grid(row=0, column=1)

tk.Label(frame, text="Preço").grid(row=1, column=0)
entry_preco = tk.Entry(frame)
entry_preco.grid(row=1, column=1)

tk.Label(frame, text="Quantidade").grid(row=2, column=0)
entry_qtd = tk.Entry(frame)
entry_qtd.grid(row=2, column=1)

var_promo = tk.BooleanVar()
tk.Checkbutton(frame, text="Promoção", variable=var_promo).grid(row=3, columnspan=2)

tk.Button(frame, text="Cadastrar", command=acao_cadastrar).grid(row=4, columnspan=2, pady=5)


# Consulta
tk.Label(frame, text="Consultar produto").grid(row=5, columnspan=2)
entry_consulta = tk.Entry(frame)
entry_consulta.grid(row=6, columnspan=2)

tk.Button(frame, text="Consultar", command=acao_consultar).grid(row=7, columnspan=2, pady=5)


# Listar
tk.Button(frame, text="Listar Todos", command=acao_listar).grid(row=8, columnspan=2)


# Output
output = scrolledtext.ScrolledText(root, width=60, height=15)
output.pack(pady=10)


root.mainloop()
