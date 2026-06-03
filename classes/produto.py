# Exercício 1:

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def valor_total(self):
        return self.preco * self.quantidade
produto1 = Produto("Calça", 99.90, 3)
print(f"{produto1.valor_total():.2f}")