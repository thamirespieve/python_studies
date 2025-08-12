"""
É um tipo especial de função que permite modificar ou extender o comportamento de outra
função
"""

def meu_decorador(func):
    def wrapper():
        print("Antes da função ser chamada")
        func()
        print("Depois da função ser chamada")
    return wrapper 

@meu_decorador
def minha_funcao():
    print("Minha função foi chamada")


minha_funcao()

class MeuDecoradorDeClasse:
    def __init__(self,func):
        self.func = func
    def __call__(self):
        print("Antes da função ser chamada (decorador de classe)")
        self.func()
        print("Depois da função ser chamada (decorador de classe)")

@MeuDecoradorDeClasse
def segunda_funcao():
    print("Segunda funcao foi chamada")

segunda_funcao()

##Decoradores comuns
"""
@classmethod -> Precisa passar o cls para função e que ela tenha acesso aos atributos e 
metodos da classe, não consegue acessar atributos e metodos que precisam ser instanciados.
@staticmethod -> Não recebe argumentos, não tem acesso ao atributos da classe ou da instancia
"""
class MinhaClasse:
    valor = 10 #Atributo classe (estatico), não precisa de instancia
    def __init__(self,nome):
        self.nome = nome
    
    #Requer uma instancia para ser chamado
    def metho_instancia(self):
        return f"Metodo de instancia chamado para {self.nome}"
    
    @classmethod
    def metofo_classe(cls):
        return f"Metodo de classe chamado para valor {cls.valor}"
    
    @staticmethod
    def metodo_estatico():
        return "Metodo estático chamado"



obj = MinhaClasse("Classe exemplo")
print(obj.metho_instancia())
print(MinhaClasse.valor)
print(MinhaClasse.metofo_classe())
print(MinhaClasse.metodo_estatico())


class Carro:
    def __init__(self,marca,modelo,ano):
        self.marca=marca
        self.modelo = modelo
        self.ano = ano
    
    @classmethod
    def criar_carro(cls,configuracao):
        marca,modelo,ano=configuracao.split(",")
        return cls(marca,modelo,int(ano))


configuracao1="Toyota,Corolla,2022"
carro1 = Carro.criar_carro(configuracao1)
print(f"Marca:{carro1.marca}\nModelo:{carro1.modelo}\nano:{carro1.ano}")

class Matematica:
    @staticmethod
    def somar(a,b):
        return a+b

print(Matematica.somar(2,8))

