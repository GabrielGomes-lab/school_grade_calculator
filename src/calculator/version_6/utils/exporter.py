import pandas as pd

def export_to_excel(data, filename="notas_estudantes.xlsx"):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
