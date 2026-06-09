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
            

alan = Aluno("Alan", [3, 5.3, 6])
gabriela = Aluno("Gabriela", [6.3, 7, 8.5])
caio = Aluno("Caio", [9.5, 8, 8.3])

alunos = [alan, gabriela, caio]
for aluno in alunos:
    print(f"{aluno.nome}: {aluno.situacao()}")