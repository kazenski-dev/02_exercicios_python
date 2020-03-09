"""
ACUMULADORES: tem valor VARIAVEL
"""
#Variaveis
numero = 1
soma = 0

#Codigo Principal
while (numero <= 10):
    num_usuario = int(input("Insira o valor a ser somado: "))
    soma = soma + num_usuario
    numero = numero + 1
print("Soma = %d"%(soma))
