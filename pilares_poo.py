# Exemplo de herança

print('Classes exemplo:')
class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def emitir_som(self):
        pass

    def andar(self):
        print(f'O animal {self.nome} andou')
        return

class Cachorro(Animal):
    def emitir_som(self):
        return "Au, au"
    
class Gato(Animal):
    def emitir_som(self):
        return "Miau, miau"
    
dog = Cachorro(nome='Rex')
cat = Gato(nome='Mingau')

print("\nExemplo de polimorfismo:")
animais = [dog, cat]
for animal in animais:
    print(f"O {animal.nome} faz: {animal.emitir_som()}")

print("\nExemplo de encapsulamento:")
class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo #atributo privado
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
    
    def sacar(self, valor):
        if valor > 0 and self.__saldo >= valor:
            self.__saldo -= valor

    def consultar_saldo(self):
        return self.__saldo
    
conta = ContaBancaria(saldo=1000)
print(f"Saldo da conta bancaria: {conta.consultar_saldo()}")
conta.depositar(valor=500)
print(f"Saldo da conta bancaria: {conta.consultar_saldo()}")
conta.depositar(valor=-500)
print(f"Saldo da conta bancaria: {conta.consultar_saldo()}")
conta.sacar(valor=1500)
print(f"Saldo da conta bancaria: {conta.consultar_saldo()}")

conta_do_zezinho = ContaBancaria(saldo=100)

print("\nExemplo de abstração:")

from abc import ABC, abstractmethod

class Veiculo(ABC):

    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo):
    def __init__(self) -> None:
        pass

    def ligar(self):
        print("Carro ligado usando a chave")
    
    def desligar(self):
        print("Carro desligado usando a chave")

carro_amarelo = Carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())