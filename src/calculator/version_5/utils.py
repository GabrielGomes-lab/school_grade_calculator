import pandas as pd

def exportar_excel(lista_alunos, nome_arquivo="registros_alunos.xlsx"):
    df = pd.DataFrame(lista_alunos)
    df.to_excel(nome_arquivo, index=False)
