"""
Faça um programa que peça uma nota, entre zero e dez. Mostre a mensagem caso o valor
seja inválido pedindo até que o usuário informe um valor válido.
"""
#Variaveis:
limite_inicio = 0
limite_fim = 10

#Codigo Principal
while True:
    num_usuario = int(input("Insira um valor inteiro entre zero e dez: "))
    if (num_usuario >= limite_inicio) and (num_usuario <= limite_fim):
        print("O valor inserido foi:", num_usuario)
        break
    else:
        print("Número Inválido.")