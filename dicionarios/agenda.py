# Exercício 3: Gerenciamento de contatos

def adicionar_contato(lista, nome, telefone, email):
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }
    for item in lista:
        if item["nome"] == nome:
            print("Contato existente. Tente outro.")
            return
      
    lista.append(contato)
    print(f"Contato {nome} adicionado com sucesso!")
    

def buscar_contato(lista, nome):
    for contato in lista:
        if contato["nome"] == nome:
            return contato
    return None

def listar_contatos(lista):
    if len(lista) == 0:
        print("Nenhum contato cadastrado.")
        return
    for contato in lista:
        print(f"Nome: {contato['nome']}")
        print(f"Telefone: {contato['telefone']}")
        print(f"Email: {contato['email']}")
        print("---")

def remover_contato(lista, nome):
    resultado = buscar_contato(lista, nome)
    if resultado is None:
        print("Esse contato não existe.")
    else:
        lista.remove(resultado)
        print(f"Contato {nome} removido com sucesso!")

def main():
    contatos = []
    adicionar_contato(contatos, "Vivian", "2796589541", "vivian@gmail.com")
    
    resultado = buscar_contato(contatos, "Vivian")
    print(resultado)
    
    listar_contatos(contatos)
    remover_contato(contatos, "Vivian")

if __name__ == "__main__":
    main()