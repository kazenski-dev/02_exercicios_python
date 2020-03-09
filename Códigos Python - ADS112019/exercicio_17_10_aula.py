"""
Faça um script que peça ao usuario o numero de materias da escola,ou seja, um inteiro positivo.
Em seguida, ele vai digitando o valor de cada nota, isso sera armazenado numa lista.
ao final seu script devera fornecer a media geral do aluno.
"""

lista_notas = []
numero_notas = int(input("Insira a quantidade de materias: "))
soma = 0

for elementos in range(numero_notas):
    nota = float(input("Insira a nota: "))
    lista_notas.append(nota)
    soma = (soma + nota)
print(lista_notas)
media = (soma / len(lista_notas))
print("A média é: ", media)

#------------------------------------------------------------------

lista_notas = []
numero_notas = float(input("Insira a quantidade de materias: "))
contador = 0
soma = 0

while (contador < numero_notas):
    nota = int(input("Insira a nota: "))
    lista_notas.append(nota)
    soma= (soma + lista_notas[contador])
    contador += 1
print(lista_notas)
media = (soma / len(lista_notas))
print("A média é: ", media)










