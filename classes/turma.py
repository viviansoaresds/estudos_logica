# Exercício 3: 

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas
    
    def media(self):
        return sum(self.notas) / len(self.notas)
 
    def situacao(self):
        media = self.media()
        if media >= 7:
            return "Aprovado"
        elif media >= 5:
            return "Recuperação"
        else:
            return "Reprovado"
 
class Turma:
    def __init__(self):
        self.alunos = []
    
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_aprovados(self):
        return [aluno for aluno in self.alunos if aluno.situacao() == "Aprovado"]
    
    def media_da_turma(self):
        return sum([aluno.media() for aluno in self.alunos]) / len(self.alunos)
    
alunos = [
    Aluno("Alan", [3, 5.3, 6]),
    Aluno("Gabriela", [6.3, 7, 8.5]),
    Aluno("Caio", [9.5, 8, 8.3])
]

turma = Turma()

for aluno in alunos:
    turma.adicionar_aluno(aluno)

aprovados = turma.listar_aprovados()
for aluno in aprovados:
    print(f"{aluno.nome} - Aprovado")

print(f"Média da turma: {turma.media_da_turma():.2f}")