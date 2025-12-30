import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox
from controller.aluno_controller import AlunoController
from ttkbootstrap.tableview import Tableview

class AppGUI:
    def __init__(self, root):
        self.controller = AlunoController()
        self.root = root
        self.root.title("School Average Calculator")
        self.root.geometry("800x450")

        self.build_form()
        self.build_table()
        self.build_buttons()

    def build_form(self):
        frame = tb.Frame(self.root, padding=10)
        frame.pack(fill=X)

        tb.Label(frame, text="Student ID").grid(row=0, column=0, padx=5)
        tb.Label(frame, text="Grade 1").grid(row=0, column=1, padx=5)
        tb.Label(frame, text="Grade 2").grid(row=0, column=2, padx=5)

        self.entry_id = tb.Entry(frame)
        self.entry_g1 = tb.Entry(frame)
        self.entry_g2 = tb.Entry(frame)

        self.entry_id.grid(row=1, column=0, padx=5)
        self.entry_g1.grid(row=1, column=1, padx=5)
        self.entry_g2.grid(row=1, column=2, padx=5)

    def build_table(self):
        columns = [
            {"text": "Student ID", "stretch": True},
            {"text": "Grade 1"},
            {"text": "Grade 2"},
            {"text": "Average"},
            {"text": "Status"},
        ]

        self.table = Tableview(
            master=self.root,
            coldata=columns,
            rowdata=[],
            paginated=False,
            searchable=False,
            bootstyle=PRIMARY
        )
        self.table.pack(fill=BOTH, expand=True, padx=10, pady=10)

    def build_buttons(self):
        frame = tb.Frame(self.root, padding=10)
        frame.pack()

        tb.Button(frame, text="Add Student", bootstyle=SUCCESS, command=self.add_student).pack(side=LEFT, padx=5)
        tb.Button(frame, text="Export to Excel", bootstyle=INFO, command=self.export).pack(side=LEFT, padx=5)

    def add_student(self):
        try:
            aluno = self.controller.adicionar_aluno(
                self.entry_id.get(),
                self.entry_g1.get(),
                self.entry_g2.get()
            )

            self.table.insert_row(
                values=(
                    aluno.registro,
                    aluno.nota1,
                    aluno.nota2,
                    f"{aluno.media:.2f}",
                    aluno.status
                )
            )

            self.entry_id.delete(0, END)
            self.entry_g1.delete(0, END)
            self.entry_g2.delete(0, END)

        except ValueError:
            messagebox.showerror("Error", "Grades must be numeric")

    def export(self):
        self.controller.exportar_excel()
        messagebox.showinfo("Success", "Excel file exported successfully!")
