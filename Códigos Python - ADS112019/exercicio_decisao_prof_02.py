"""Faça um script que leia três numeros e mostre quem é o meior e o menor deles."""

#Variaveis
maior_valor = 0
menor_valor = 0

#Codigo Principal
num_1 =int(input("Digite o primeiro número:"))
num_2 =int(input("Digite o segundo número:"))
if num_1>num_2:
    maior_valor = num_1
    menor_valor = num_2
else:
    maior_valor = num_2
    menor_valor = num_1
num_3 =int(input("Digite o terceiro número:"))
if num_3>maior_valor:
    maior_valor = num_3
if menor_valor>num_3:
    menor_valor = num_3
print("O maior valor é:", maior_valor)
print("O menor valor é:", menor_valor)

#   1   9   3
#   6   0   2
#   9   6   3
"""
ALGORITMO DE ORDENAÇÃO
if (num3>num2)
aux = num3
num3 = num2
num2 = aux

if (num2>num1)
aux = num2
num2 = num1
num1 = aux

if (num3>num2)
aux = num3
num3 = num2
num2 = aux

num1 = max.(num1, num2, num3)
"""
