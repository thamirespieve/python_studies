##Numericos
"""
- inteiro
- real com ponto flutuante (float)
"""
num_int = 3
print("Número inteiro: ", num_int)
num_real = 3.5
print("Número real: ",num_real)

#Função type,verifica a tipagem da var
print("Tipo da variavel: ",type(num_real))

#Operações aritimeticas 
"""
- Soma (+)
- Subtração (-)
- Multiplicação (*)
- Divisão (/)
- Divisão com retorno inteiro (//)
- Modulo % = retorna o resto da divisão
"""
soma = 1+5
sub = 1-5
mult = 2*5
div = 5/2
div_int = 5//2
modulo = 5%2
print("Divisao com retorno inteiro:", div_int)
print("Resto:", modulo)
#Conversão de var
"""
int()
float()
"""
print("valor em inteiro:", int(div))
print("Valor em float:", float(soma))

## Texto
"""
Com três aspas é possível quebrar o texto
Com \ também é possível quebrar o texto, porém não é considerado na visualização apenas 
no código
"""
nome_completo = "Thamires Pieve"
nome_aspas = """Pode pular 
linha"""
nome_quebra = "Pode pular" \
"linha"
nome = 'Gabriel'
sobrenome = "Silva"
#Formatação
"""
- Concatenação entre as variaveis (+)
- %s % substitui o '%s' pelas variavel passada, 
    se for mais de uma precisa de parentes 
- f {} começa com o f e as variaveis que devem ser incluidas é indicada dentro de {} 
- {} .format substitui as chaves pelas variaveis passada dentro do format   
"""
print("Nome completo primeira forma:", nome_completo)
print("Nome completo segunda forma:" + nome_completo)
print("Nome completo terceira forma:"+nome+sobrenome)
print('Nome completo quarta forma:'+ nome , sobrenome)
print("Nome completo quinta forma: %s" % nome_completo)
print("Nome completo sexta forma: %s %s"%(nome,sobrenome))
print(f"Nome completo setima forma: {nome} {sobrenome}")
print("Nome completo oitava forma: {} {}".format(nome,sobrenome))

#Principais metodos do tipo texto
"""
var.metodo
upper() - Maiusculo 
lower() - Minusculo
count() - Conta a quantidade de ocorrencia dentre de uma string
find() - Posição da primeira ocorrencia dentro de uma string
encode() - transforma a string em byte
decode() - transforma o byte em string
replace() - troca uma ocorrencia por outra
join()- adiciona um separador entre caracteres 
splite() - dividir as string em uma lista com base em um caracter definido
strip() - remove um caracter definido que está no começo e/ou no final da string
rstrip() - remove um caracter definido que está na direita da string
"""
print(nome.upper())
print("Quantos 'E' existem?", nome_completo.count('e'))
print("Onde está o e",nome_completo.find('e'))
print("String para byte", nome.encode())
print("byte para string", nome.encode().decode())
print("Trocando a por h",nome.replace("a","h"))
print("Adicionando separador -","-".join("Gabriel"))
print("dividindo string ",nome_completo.split(" "))
var_strip = "xtestex"
print("removendo x do começo e do final",var_strip.strip("x"))
print("removendo x da direita",var_strip.rstrip("x"))
#Comparadores
"""
in - existe um termo dentro do que quero comparar
not in - se uma ocorrencia não existe dentro da string
"""
print("Tha" in nome_completo)
print("abc" not in nome_completo)

#Boolean
"""
and - compara duas entradas 
or - uma das duas condições é verdadeira 
"""
if True and True:
    print("Será executado")

if True or False:
    print("Também será executado")

#Lista
"""
É uma coleçaõ de elementos ordenaveis e mutaveis 
"""
lista = [1,2,3,4,5,"array",True,False]
lista_ord =[1,5,7,4,3,6]
print("Lista",lista)
print("elemento index 2",lista[2])
print("pegar um intervalo da lista",lista[1:4])
print("Do começo até o elemento array",lista[:6])
print("Do elemento array até o final",lista[5:])

#Principais metados da lista
"""
append() - adiciona elemento ao final da lista
index() - retorna o index do primeiro elemento desejado
insert()- insere um elemento em um index especifico 
pop()- remove e retorna um elemento de um index especifico
remove() - remove o primeiro valor com falar especificado
sort() - ordenar a lista em ordem crescente
"""
print("adicionando elemento just no final ",lista.append("just"))
print("index do elemento just",lista.index("just"))
print("Adicionando um elemento em um index especifico",lista.insert(2,"add"))
print("Removendo o elemento de index 3",lista.pop(2))
print("Removendo o primeiro elemento com o valor especificado",lista.remove(3))
print("Ordenação da lista:",lista_ord.sort())
print(lista)
print(lista_ord)

#Tupla
"""
Coleção ordenada e imutavel
"""
tupla = (1,2,2,3,4)
print("Tupla",tupla)

print("Primeiro elemento",tupla[0])
print("Ultimo elemento",tupla[-1])

#Principais metodos
"""
count() - retorna a quantidade de vezes que um elemento aparece
index() - index da primeira ocorrencia que umelemento aparece
"""
print("Quantidade de vezes que o 2 aparece",tupla.count(2))
print("Index de um elemento",tupla.index(2))

#Dicionario
"""
É uma coleção não odernada de pares chave->valor
"""
pessoa = {"nome":"João","idade":30,"cidade":"São Paulo"}

print("Dicionario:",pessoa)
print("Nome:",pessoa['nome'])
pessoa["sobrenome"]="Silva"
print("Adicionando sobrnome",pessoa["sobrenome"])
print("Dicionario:",pessoa)

#Principais metodos
"""
del - remove um par chave-valor

keys() - retorna todas as chaves
values() - retorna todas os valores
items() - retorna um par chave-valor

O retorno é um discionario para acessar via lista é necessário transforma em lista
utilizando o list()
"""
pessoa["idade"]=31
print("Idade atualizada",pessoa["idade"])
del pessoa["sobrenome"]
print("Dicionario:",pessoa)
print("Chaves existentes:",pessoa.keys())
print("Acessando o primeiro valor",list(pessoa.keys())[0])
print("Valores existentes:",pessoa.values())
print("Acessando o segundo valor:",list(pessoa.values())[1])
print("Pares chave valor:",pessoa.items())
print("Pegando terceiro valor:",list(pessoa.items())[2][1])
