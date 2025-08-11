lista = [1,2,3,4,5]

for elemento in lista:
    print(elemento)

print("For tupla")
tupla=(1,2,3,4,5)

for elemento in tupla:
    print(elemento)

print("For dicionario")
pessoa = {"nome":"João", "idade":30,"cidade":"são paulo"}

for chave in pessoa.keys():
    print(chave)

for chave in pessoa.values():
    print(chave)

for chave,valor in pessoa.items():
    print(f"{chave}: {valor}")
    
##Range
"""
range() -> retorna um intervalo numerico em forma de lista
len -> retorna a quantidade de elementos da lista
"""
print("\n Utilizando a função range()")
for numero in range(5):
    print("Numero: ", numero)

print("\n Utilizando a função range() com len()")
for indice in range(2,len(lista)):
    print("Indice: ",indice)
    print("Elemento: ",lista[indice])
    if indice == 3:
        lista[indice]=2
print(lista)

#enumerate()

lista_enum = ["a","b","c"]

for indice,valor in enumerate(lista_enum):
    print(f"{indice}: {valor}")
    if indice == 1:
        print("indice 1")

#While
print("Exemplo while")
cont = 0

while cont < 5 :
    print("Contagem: ", cont)
    cont += 1


print("Contador finalizado")


