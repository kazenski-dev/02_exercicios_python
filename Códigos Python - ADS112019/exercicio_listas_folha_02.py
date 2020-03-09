"""
Faça um programa que leia um vetor de 10 números reais e mostre-os na ordem inversa:
"""
#Variaveis
vetor_inteiro = [0,0,0,0,0,0,0,0,0,0]
contador = 0

#Codigo Principal
while (contador < (len(vetor_inteiro))):
    vetor_inteiro[contador] = int(input("Digite o valor do vetor: "))
    contador += 1
contador = (len(vetor_inteiro) - 1)
while (contador >= 0):
    print(vetor_inteiro[contador], end= ", ")
    contador -= 1


"""
lista = []
nome = input("Digite seu nome: ")
idade = float(input("Digite sua idade: "))
sexo = input("Digite seu sexo: M- maculino ou F- feminino: ")
lista.append(nome)
lista.append(idade)
lista.append(sexo)
lista.reverse()
print(lista)
"""
