"""
FATIANDO STRING
"""
nome = "TAKEHIKO MARUYAMA"
print(nome[:6]) #aqui to fatiando do inicio ate meu limite 6

#-------------------------------------------------------------------------------------#
#Achar um pedaco de string

nome = "TAKEHIKO MARUYAMA"
print("re" in nome)
print("ru" in nome)
#ambos deram false porque tem o sense case que nao acha esse pedaco de string no nome

#-------------------------------------------------------------------------------------#
#Imprimir o tamanho de uma string

nome = "TAKEHIKO MARUYAMA"
print(len(nome)) #Imprime os indices de ZERO ate o final

#-------------------------------------------------------------------------------------#
#Imprimir em minusculo e em maiusculo

nome = "TAKEHIKO MARUYAMA"
print(nome.lower())
print(nome.upper())

#-------------------------------------------------------------------------------------#
#Imprimir a string - retornando cada palavra que for separada por ESPAÇO, em elementos de uma lsita

nome = "TAKEHIKO MARUYAMA"
print(nome.split())

#-------------------------------------------------------------------------------------#

"""
FUNCOES EM LISTAS
- sempre que tiver colchetes [] é uma LISTA
- consigo trabalhar com os índices e tambem com os elementos
- listas podem ser concatenadas oun multiplicadas


lista = ["O carro", "O peixe", 123, 111]
nova_lista = ["pedra", lista]
print(nova_lista )
print(lista + nova_lista) #concatenar
print(lista * 3) #multiplicar

#RESULTADO NA TELA:

['O carro', 'O peixe', 123, 111, 'pedra', ['O carro', 'O peixe', 123, 111]]
['O carro', 'O peixe', 123, 111, 'O carro', 'O peixe', 123, 111, 'O carro', 'O peixe', 123, 111]
#-------------------------------------------------------------------------------------#

print("O peixe" in lista) #busco um elemento em especifico na lista

#-------------------------------------------------------------------------------------#

numeros = [14.55, 67, 89.88, 10, 21.5]
print(min(numeros))
print(max(numeros))

#-------------------------------------------------------------------------------------#

livros = ["java", "sql server", "delphy", "python"]
livros.append("android")
print(livros)

#-------------------------------------------------------------------------------------#

livros = ["java", "sql server", "delphy", "python"]
livros.append("android")
livros.insert(0, "eclipse")
print(livros)

#-------------------------------------------------------------------------------------#

livros = ["java", "sql server", "delphy", "python"]
livros.append("android")
print(livros)
livros.insert(0, "eclipse")
print(livros)
livros.pop(0)
print(livros)
livros.remove("java")
print(livros)

#-------------------------------------------------------------------------------------#
"""
livros = ["java", "sql server", "delphy", "python"]
livros.sort() #ordena num tipo de ordem - ORDEM ALFABETICA
print(livros)
livros.reverse() #ordena de outra forma - IBNVERTE A ORDEM DOS ELEMENTOS
print(livros)

#-------------------------------------------------------------------------------------#

#count = retorna o número de ocorrências que tem um elemento que quero dentro da lista

livros = ["java", "sql server", "delphy", "python"]
print(livros.count("java")) #retorna o numero de elementos que tem o parametro que pedi

#-------------------------------------------------------------------------------------#
#COMO E O CODIGO DO COUNT?

lista = [1,10,2,10,3,1,4,5,6]
contador = 0
for i in range(len(lista)):
    if (lista[i] == 10):
        contador += 1
print(contador)

contador = lista.count(10)
print(contador)

#-------------------------------------------------------------------------------------#
#Adicionar elementos em lista com append

lista1 = [1,2,3,4]
lista2 = [5,6,7]
for i in range(len(lista2)):
#vou verificar o tamanho de elementos da lista2 - cada elemento de lista2
    lista1.append(lista2[i])
#aqui digo que é pra adicionar na ultima posicao de lista1 o elemento de lista 2
print(lista1)

#-------------------------------------------------------------------------------------#
#USANDO COMANDO EXTEND

lista1 = [1,2,3,4]
lista2 = [5,6,7]
print(lista1.extend(lista2))

#-------------------------------------------------------------------------------------#
#INSERT NA POSICAO 2 O VALOR 10

lista = [1,2,3,4]
lista.insert(2,10)
print(lista)

#-------------------------------------------------------------------------------------#



