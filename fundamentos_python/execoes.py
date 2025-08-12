print("Exemplo de captura de excções")
try:
    numero = int(input("Digite um num inteiro:"))
    resultado = 10/numero
except ValueError as e:
    print(f"Erro de value error:{e}")
    #Adicionando uma mensagem exceção
    raise ValueError("Tipo de variaveis incompativeis")
except Exception as e:
    print(f"Erro:{e}")
#Else só executa se o try der certo
else:
    print('Resultado:',resultado)
#Executa dando certo ou errado
finally:
    print("Operação finalizada")
