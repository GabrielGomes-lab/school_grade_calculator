""" Já aqui vamos utilizar conceitos de orientação a objetos para estruturar melhor nosso código, a ideia segue a mesma das anteriores, mas agora com classes e objetos."""


class Aluno:
    def __init__(self, registro, nota1, nota2):
        self.registro = registro
        self.nota1 = float(nota1)
        self.nota2 = float(nota2)
        self.media = self.calcular_media()
        self.status = self.determinar_status()

    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2

    def determinar_status(self):
        if self.media >= 7:
            return "Aprovado"
        elif self.media >= 5:
            return "Recuperação"
        else:
            return "Reprovado"

    def to_dict(self):
        return {
            "Registro": self.registro,
            "Nota 1": self.nota1,
            "Nota 2": self.nota2,
            "Média": round(self.media, 2),
            "Status": self.status
        }