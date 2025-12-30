import tkinter as tk
from tkinter import messagebox
from calculator import Aluno
from calculator.utils import exportar_excel

lista_alunos = []

def adicionar_aluno():
    registro = entry_registro.get()
    nota1 = entry_nota1.get()
    nota2 = entry_nota2.get()

    if not registro or not nota1 or not nota2:
        messagebox.showwarning("Erro", "Preencha todos os campos.")
        return

    try:
        aluno = Aluno(registro, nota1, nota2)
        lista_alunos.append(aluno.to_dict())

        label_resultado.config(
            text=f"Média: {aluno.media:.2f} | Status: {aluno.status}"
        )

        entry_registro.delete(0, tk.END)
        entry_nota1.delete(0, tk.END)
        entry_nota2.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Erro", "As notas devem ser numéricas.")

def exportar():
    if not lista_alunos:
        messagebox.showwarning("Aviso", "Nenhum aluno cadastrado.")
        return

    exportar_excel(lista_alunos)
    messagebox.showinfo("Sucesso", "Arquivo Excel exportado com sucesso!")

# ===== GUI =====
root = tk.Tk()
root.title("Calculadora de Média Escolar")
root.geometry("350x300")

tk.Label(root, text="Registro do Aluno").pack()
entry_registro = tk.Entry(root)
entry_registro.pack()

tk.Label(root, text="Nota 1").pack()
entry_nota1 = tk.Entry(root)
entry_nota1.pack()

tk.Label(root, text="Nota 2").pack()
entry_nota2 = tk.Entry(root)
entry_nota2.pack()

tk.Button(root, text="Adicionar Aluno", command=adicionar_aluno).pack(pady=10)
tk.Button(root, text="Exportar para Excel", command=exportar).pack()

label_resultado = tk.Label(root, text="")
label_resultado.pack(pady=10)

root.mainloop()
