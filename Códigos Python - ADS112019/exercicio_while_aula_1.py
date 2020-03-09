"""
Vamos solicitar um número ao usuário e armazenar na variável 'num'.
Para saber se o número é positivofazer o seguinte: num >0
Identificar se é maior, menor ou igual:
"""
#Codigo Principal
num = int(input("Insira o valor: "))
if (num > 0):
    print("Numero positivo.")
else:
    if(num < 0):
        print("Número negativo")
    else:
        print("Número ZERO")
