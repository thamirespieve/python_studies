"""
São arquivos que contem instruções que podem ser utilizados em outros arquivos.
"""

print("Exemplo de importação de módulo padrão:")
##importa o modulo inteiro  
#import math

##Importa só a função que vai ser utilizada
from math import sqrt

raiz_quadrada = sqrt(144)
print(f"A raiz quadrada de 144 é {raiz_quadrada}")


print("\n Exemplo de criação e utilização de um modulo personalizado")
import meu_modulo

mensagem = meu_modulo.saudacao("Alice")
resultado= meu_modulo.dobro(5)

print(mensagem)
print(f"O dobro de 5 é {resultado}")