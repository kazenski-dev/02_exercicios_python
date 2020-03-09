"""
Faça um programa que leia a idade e altura de 5 pessoas, armazene cada informação
em seu respectivo valor. Imprima a idade e altura na ordem inversa a ordem feita.

#Variaveis
vetor_idade = [0, 0, 0, 0, 0]
vetor_altura = [0, 0, 0, 0, 0]
contador = 0

#Codigo Principal
for elementos in vetor_idade:
    vetor_idade[contador] = int(input("Insira a idade: "))
    vetor_altura[contador] = float(input("Insira a altura: "))
    contador += 1
print(vetor_idade)
print(vetor_altura)

decrementador = contador - 1
for elementos in vetor_idade:
    print(vetor_idade[decrementador])
    print(vetor_altura[decrementador])
    decrementador -= 1
"""

#Variaveis
vetor_idade = [0, 0, 0, 0, 0]
vetor_altura = [0, 0, 0, 0, 0]
contador = 0

#Codigo Principal
for elementos in vetor_idade:
    vetor_idade[contador] = int(input("Insira a idade: "))
    vetor_altura[contador] = float(input("Insira a altura: "))
    contador += 1
print(vetor_idade)
print(vetor_altura)

decrementador = contador - 1
for elementos in vetor_idade:
    print("[", end = " ")
    print(vetor_idade[decrementador], end =  ", ")
    print("]")
    decrementador -= 1
for elementos in vetor_idade:
    print("[", end=" ")
    print(vetor_altura[decrementador], end = " ")
    print("]")
    decrementador -= 1
