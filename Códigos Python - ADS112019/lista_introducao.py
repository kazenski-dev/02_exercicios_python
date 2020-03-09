"""
PHYTON: VETORES(ARRAYS) E LISTAS
Quando usamos? Quandotemos alguns nomes de funcionarios e salarios correspondentes a cada um desses nomes.
- usado entre colchetes []
- primeira posição de uma lista é ZERO, onde o ZERO é o primeiro elemento da lista
- posso ordenar, buscar elemento específico na lista
- EM PHYTON NÃO TEM ARRAY OU VETOR - AQUI SE CHAMA LISTA
- Lista é um objeto e existem especificações: TUpla ou Dicionário
- listas são o tipo de variaveis ou constantes
"""
#ACESSANDO ELEMENTOS DE UMA LISTA
lista = [-12, 50, 25, 0, 45, 9]
print(lista)
print(len(lista)) #imprimo a quantidade de elementos que tem na lista

lista_mista = [10, "chocolate" ,102.55, "05/01/200"] # tem tipos diferentes de variaveis
print(lista_mista)
#podemos colocar VARIOS tipos de elementos na mesma lista

print(lista[0]) #aqui vou imprimir o INDICE que eu quero
print(lista_mista[1])

#print(lista[7]) #da ERRO porque não tem auqi o indice 7

notas = [5.5, 10.0, 4.5]
soma_notas = notas[0] + notas[1] + notas[2]
print(soma_notas)

#PRIMEIRO COMANDO COM LISTA:
notas = [0, 0, 0]
notas[0] = eval(input("Digite a primeira nota: "))
notas[1] = eval(input("Digite a segunda nota: "))
notas[2] = eval(input("Digite a terceira nota: "))
print(notas)

