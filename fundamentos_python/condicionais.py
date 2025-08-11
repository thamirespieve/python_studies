#condicionais
"""
if, elif e else
Comparadores
== -> igual
> -> maior
< -> menor
>= -> maior igual
<= -> menor igual
!= -> diferente
"""
idade = int(input("Quantos anos vocês tem?"))

if idade >= 18:
    print("Maior de idade")
elif idade >= 12:
    print("Adolescente")
else:
    print("Criança")

mensagem = "Pode tirar carteira" if idade >= 18 else "Você não pode tirar carteira"
print(mensagem)