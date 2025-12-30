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
            return "Approved"
        elif self.media >= 5:
            return "Recovery"
        else:
            return "Failed"

    def to_dict(self):
        return {
            "Student ID": self.registro,
            "Grade 1": self.nota1,
            "Grade 2": self.nota2,
            "Average": round(self.media, 2),
            "Status": self.status
        }
