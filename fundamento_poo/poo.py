"""
Permiter que se criei código modular reutilizavel e fácil de manter.
Poo - se baseia na organização em torno de objetos (instancias de classes)
"""

class Pessoa:
    #Construtor da classe
    """ 
        self é uma referencia própria classe
        depois do self é os argumentos da classe
        -> None é para dizer que não tem retorno.
    """
    def __init__(self,nome,idade) -> None:
        self.nome = nome
        self.idade = idade
    
    #Metodos
    def saudacao(self):
        return f"Ola, meu nome é {self.nome} e eu tenho {self.idade} anos."

#Obejto
pessoa1 = Pessoa("Thamires",27)
print(pessoa1.saudacao())

pessoa2=Pessoa("Rodigro",32)
print(pessoa2.saudacao())