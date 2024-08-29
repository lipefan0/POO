class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome
    
    def emitir_som(self):
        pass

class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} está amamentando"

class Ave(Animal):
    def voar(self):
        return f"{self.nome} está voando"

print("\nExemplo de herança múltipla:")
class Morcego(Mamifero, Ave):
    def emitir_som(self):
        return "Morcego emitem sons ultrassônicos"
    
morcego = Morcego(nome='Vamp')

# Acessando os metodos da base animal
print("Nome do morcego:", morcego.nome)
print("Som do morcego:", morcego.emitir_som())

# Acessando os metodos da base mamifero e ave
print("Morcego amamentando:", morcego.amamentar())
print("Morcego voando:", morcego.voar())