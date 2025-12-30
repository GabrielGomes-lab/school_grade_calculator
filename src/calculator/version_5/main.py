""" Aqui é nosso código principal que utiliza a classe Aluno para calcular médias e determinar status dos alunos."""

# Aqui importamos a classe Aluno do módulo calculator
from calculator import Aluno
import pandas as pd
# Exemplo de uso simples classe Aluno
oAluno = Aluno("João", 8.5, 7.0)

# Aqui podemos além de tudo exibir tudo separadamente utilizando os métodos da classe.
print(oAluno.nome)
print(oAluno.nota1)
print(oAluno.nota2)
# Mas digamos que queremos um programa interativo para o usuário com vários alunos e que eles sejam salvos em uma lista de dicionário e que depois sejam exibidos e exportados para um excel.
lista_alunos = []
while True:
    nome = input("Digite o número de registro do aluno (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    nota1 = float(input(f"Digite a primeira nota do aluno {nome}: "))
    nota2 = float(input(f"Digite a segunda nota do aluno {nome}: "))

    aluno = Aluno(nome, nota1, nota2)
    lista_alunos.append({
        "Nome": aluno.nome,
        "Média": aluno.media,
        "Status": aluno.status
    })
    aluno.exibir_resultado()

# Criar um DataFrame com os registros dos alunos
df = pd.DataFrame(lista_alunos)
# Exportar os registros para um arquivo Excel
df.to_excel("registros_alunos.xlsx", index=False)
print("Registros dos alunos foram exportados para 'registros_alunos.xlsx'.")

