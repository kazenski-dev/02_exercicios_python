"""
Faça um programa que leia um vetor de cinco números inteiros e mostre-os:
"""
#Variaveis
vetor_inteiro = [0, 0, 0, 0, 0]
contador = 0

#Codigo Principal
while (contador < (len(vetor_inteiro))):
    vetor_inteiro[contador] = eval(input("Digite o primeiro valor do vetor: "))
    contador += 1
print(vetor_inteiro)