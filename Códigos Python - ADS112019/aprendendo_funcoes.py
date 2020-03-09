"""
FUNÇÕES:
São são blocos de codigos identificados por um nome que realizam determinadas
tarefas. Elas podem receber argumentos e pode (ou não) retornar valores.

A sintaxe de uma função é dividida em três partes:
1- nome, 2- parâmetro, 3- corpo

"""
def soma (a, b):
    print(a + b)
#------------------------------------------------------------
soma = (2,9)
soma = (45, 45)
#Esse codigo retorna dentro dela O PRINT

"""
RETURN:
Retorno um valor que foi criado dentro da FUNÇÃO.
- O valor DEFAULT de return é: None (null, nil, void)
- é logicamente igual a FALSE

import random
#Declaração de função que cria uma lista aleatória/ BIBLIOTECA

def Cria_lista_aleatoria (tamanho):
    lista = []

    for i in range(tamanho):
        valor = random.randint(1, 10) #Número RANDOMICO de INTEIROS (randINT)
        lista.append(valor)
    return lista, max(lista), min(lista)

#Codigo Principal
tam = 5
li, maxli, minli = Cria_lista_aleatoria(tam)
print(li)
print(maxli)
print(minli)"""
#------------------------------------------------------
def soma (a, b):
    return (a + b)
#------------------------------------------------------------
print (soma (2,9))
print (soma (45, 45))


"""
FUNÇÕES BUILTIN NO PYTHON:
A biblioteca do Python contém vários componentes imbutidos, que podem ser utilizados em 
qualquer parte do código sem a necessidade de um import.

- max() = retorna o maior valor da listaque lhe é passada de parâmetro
- input() = que recebe o valor digitado pelo usuário
- float() = converte um valor para float
- int() = converte um valor para int

"""
#SEM ARGUMENTOS
def diga_algo (msg, nome):
    print("{}, {}!".format(msg, nome))

#CHAMADA NO CODIGO PRIMCIPAL:
diga_algo("Ola", "Fabiano")

#------------------------------------------------------------

def ola_pessoa (nome):
    print("Ola " + nome + " como você está?")

meu_nome = "Eduardo"
ola_pessoa(meu_nome)

#------------------------------------------------------------

def ola_pessoa_email (nome,email):
    print("Ola " + nome + " como você está, usa muito o email " + email + " ?")

meu_nome = "Eduardo"
meu_email = "eduardo.bancodados@gmail.com"
ola_pessoa_email(meu_nome, meu_email)

#------------------------------------------------------------


