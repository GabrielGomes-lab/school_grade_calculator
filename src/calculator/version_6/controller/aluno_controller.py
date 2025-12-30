from model.aluno import Aluno
from utils.exporter import export_to_excel

class AlunoController:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, registro, nota1, nota2):
        aluno = Aluno(registro, nota1, nota2)
        self.alunos.append(aluno)
        return aluno

    def listar_alunos(self):
        return [aluno.to_dict() for aluno in self.alunos]

    def exportar_excel(self):
        dados = self.listar_alunos()
        export_to_excel(dados)
