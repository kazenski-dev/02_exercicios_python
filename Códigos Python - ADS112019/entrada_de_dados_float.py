#Entrada de Dados FLOAT
num_1 = float (input("Digite um número:"))
print(num_1)
num_2 = float(input("Digite outro número:"))
print(num_2)
soma = num_1+num_2
print("A soma é:",soma)
#Eu posso digitar um número INTEIRO, a máquina converterá em FLOAT: 10 virará 10.00

print("A soma entre %.2f e %.2f é %.2f"%(num_1, num_2,soma))

"""Diferente do índice do .format, aqui os elementos colocados entre parênteses
seguirão a ordem de aparecimento dos % na frase. Se tiver, por exemplo, 4 %, devo ter
4 indices entre parenteses; e eles apaecerão na ordem que estão nos parenteses."""


