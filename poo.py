#Classes exemplo:
class Pessoas:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
    
    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos"

#Objetos Exemplo:

pessoa1 = Pessoas('Felipe', 27)

mensagem1 = pessoa1.saudacao()

print(mensagem1)

pessoa2 = Pessoas('Maria', 30)
memsagem2 = pessoa2.saudacao()

print(memsagem2)

