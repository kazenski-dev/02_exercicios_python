"""Desafio:
Pedir ao usuario o primeiro numero a ser impresso e o ultimo:
Estou pedindo  o intervalo que eu quero!"""

#Variaveis
inicio = int(input("Digite um número inicial para contagem: "))
numero_max = int(input("Digite um número máximo para contagem: "))

#Codigo Principal:
while(inicio <= numero_max):
    print(inicio)
    inicio = inicio + 1