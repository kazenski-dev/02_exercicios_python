"""CONDIÇÃO - IF - exemplo 1
Faça um programa que receba 3 valores e identifique
o maior, e o menor."""

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
COMANDO DIRETO PARA ACHAR MAX E MIN
notamax = max(nota1, nota2, nota3)
notamin = min(nota1, nota2, nota3)
"""
