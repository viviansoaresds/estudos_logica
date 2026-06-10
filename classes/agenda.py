#Exercício 4: Reescrita da agenda de contatos da semana utilizando classe

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome, telefone, email):
        for item in self.contatos:
            if item["nome"] == nome:
                print("Contato existente. Tente outro.")
                return
            
        contato = {"nome": nome, "telefone": telefone, "email": email}
        self.contatos.append(contato)

    
    def buscar_contato(self, nome):
        for contato in self.contatos:
            if contato["nome"] == nome:
                return contato
            
        return None
        
    def listar_contatos(self):
        if len(self.contatos) == 0:
            print("Nenhum contato cadastrado.")
            return
        
        for contato in self.contatos:
            print(f"Nome: {contato['nome']}")
            print(f"Telefone: {contato['telefone']}")
            print(f"Email: {contato['email']}")
            print("-------------------------")

    def remover_contato(self, nome):
        resultado = self.buscar_contato(nome)
        if resultado == None:
            print("Esse contato não existe.")
        else:
            self.contatos.remove(resultado)
            print(f"Contato {nome} removido com sucesso!")

def main():
    agenda = Agenda()  
   
    agenda.adicionar_contato("Vivian", "27999586542", "vivian@gmail.com")
    agenda.adicionar_contato("Ana", "25999486152", "ana@gmail.com")

    agenda.listar_contatos()
    
    resultado = agenda.buscar_contato("Vivian")
    print(resultado)
    
    agenda.remover_contato("Vivian")
    agenda.listar_contatos()

if __name__ == "__main__":
    main()


    
