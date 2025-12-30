"""Simple calculator with if and else statements."""
# Aqui pedimos ao usuário que digite as notas e transformamos em float.
nota1 = float(input("Digite a primeira nota do aluno:"))
nota2 = float(input("Digite a segunda nota do aluno:"))

# Calculamos a média das notas.
media = (nota1 + nota2) / 2

# Fazemos as verificações necessárias para entender se o aluno está aprovado, em recuperação ou reprovado.
if media >= 7:
    print("Aluno aprovado!")
elif media >= 5:
    print("Aluno em recuperação.")
else:
    print("Aluno reprovado.")

