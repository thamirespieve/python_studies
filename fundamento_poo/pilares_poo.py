"""
abstração, encapsulamento, herança e polimorfismo

Herança -> herda os atributos e metados da classe mãe
Polimorfismo -> Permite utilizar o metado da classe mãe reemplementado de outra forma
encapsulamento -> Uso dos atributos prividas para proteger os dados de serem manipulados
abstraçao -> Cria um molde para criação de classes, não é possível criar uma instancia
de uma classe abstrata. Ela obriga a implementação de um metodo quando ele é definido como
abstrato
"""
class Animal:
    def __init__(self,nome):
        self.nome = nome
    
    def andar(self):
        print("O animal {self.nome} andou")
        return
    
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au au"

class Gato(Animal):
    def emitir_som(self):
        return "miau"
    
dog = Cachorro("Regex")
cat = Gato("Peixe")

animais = [dog,cat]

for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")

print("Exemplo encapsulamento")
"""
Quando um atributo é privado apenas os metodos da classe pode utilizar, 
não é possível alterar via 'herança' por exemplo
"""
class ContaBancaria:
    def __init__(self,saldo):
        self.__saldo = saldo #Atributo privado, é indicado pelos dois underlines 

    def depoisitar(self,valor):
        if valor >0:
            self.__saldo += valor

    def sacar(self,valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self):
     return self.__saldo

conta = ContaBancaria(saldo=1000)
print(f"Saldo em conta:{conta.consultar_saldo()}")
print(f"Deposito de 100")
print(f"Saldo em conta:{conta.consultar_saldo()}")
print(f"Saque de 200")
print(f"Saldo em conta:{conta.consultar_saldo()}")


print("Exemplo de abstração:")
from abc import ABC, abstractmethod

class Veiculo(ABC):
    
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo):
    def __init__(self):
        pass

    def ligar(self):
        return "Carro ligado usando chave"

    def desligar(self):
        return "Carro desligado usando chave"

carro_amarelo = Carro()
print(carro_amarelo.ligar())