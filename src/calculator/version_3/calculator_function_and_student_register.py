""" Aqui vamos utilizar a mesma base da versão número 3, mas agora vamos adicionar a funcionalidade de registrar o nome do aluno junto com suas notas e média, além da possibilidade de exportar um excel"""

import pandas as pd

def calcular_media(aluno,nota1, nota2):
    """Calcula a média de duas notas."""
    nota1 = float(nota1)
    nota2 = float(nota2)
    media = (nota1 + nota2) / 2

    if media >= 7:
        status = "Aluno aprovado!"
    elif media >= 5:
        status = "Aluno em recuperação."
    else:
        status = "Aluno reprovado."
    
    return aluno,media, status

# Lista para armazenar os registros dos alunos
registros = []
while True:
    aluno = input("Digite o número de registro do aluno (ou 'sair' para encerrar): ")
    if aluno.lower() == 'sair':
        break
    nota1 = float(input(f"Digite a primeira nota do aluno {aluno}: "))
    nota2 = float(input(f"Digite a segunda nota do aluno {aluno}: "))

    nome, media, status = calcular_media(aluno,nota1, nota2)
    registros.append({"Nome": nome, "Média": media, "Status": status})
    print(f"{nome} - Média: {media:.2f} - {status}")

# Criar um DataFrame com os registros dos alunos
df = pd.DataFrame(registros)

# Exportar os registros para um arquivo Excel
df.to_excel("registros_alunos.xlsx", index=False)
print("Registros dos alunos foram exportados para 'registros_alunos.xlsx'.")