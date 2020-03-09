"""
Faça um programa que faça uma tabuada por um número que o usuário informrá.
"""
#Variaveis
num_inicial = 1
ULTIMO_NUM = 10
num_tabuada = int(input("Insira o número que deseja visualizar a tabuada: "))

#Codigo Principal
print("Tabuada do número:", num_tabuada)
while(num_inicial <= ULTIMO_NUM):
    print("",num_inicial * num_tabuada)
    num_inicial = num_inicial + 1