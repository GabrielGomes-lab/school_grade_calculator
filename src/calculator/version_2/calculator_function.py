""" Aqui para essa segunda versão, estamos evoluindo em nossos conhecimentos de Python, 
então utilizaremos uma maneira mais 'refinida' de fazer o mesmo cálculo, utilizando funções."""

""" Podemos continuar com a mesma ideia de input, mas agora vamos encapsular a lógica em funções para melhor organização do código."""
nota1 = float(input("Digite a primeira nota do aluno:"))
nota2 = float(input("Digite a segunda nota do aluno:"))

def calcular_media(nota1, nota2):
    """Calcula a média de duas notas."""
    nota1 = float(nota1)
    nota2 = float(nota2)
    media = (nota1 + nota2) / 2

    if media >= 7:
        print("Aluno aprovado!")
    elif media >= 5:
        print("Aluno em recuperação.")
    else:
        print("Aluno reprovado.")
    return media

# Chamamos a função para calcular a média e determinar o status do aluno.
calcular_media(nota1, nota2)

