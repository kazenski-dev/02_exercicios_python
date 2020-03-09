"""
Pedir o utilizador que introduza 5 numeros. Guardar numa lista. Mostrar a lista
FORMA 01
"""
n1 = float(input("Insira o numero: "))
n2 = float(input("Insira o numero: "))
n3 = float(input("Insira o numero: "))
n4 = float(input("Insira o numero: "))
n5 = float(input("Insira o numero: "))
l = [n1, n2, n3, n4, n5]
l.sort()
print(l)

"""
Pedir o utilizador que introduza 5 numeros. Guardar numa lista. Mostrar a lista
FORMA 02
"""
lista1 = []
for elementos in range(5):
    lista1.append(float(input("Insira o numero: ")))
    lista1.sort()
print(lista1)

"""
Pedir o utilizador que introduza 5 numeros. Guardar numa lista. Mostrar a lista
FORMA 02
"""
contador = 0
lista =[]
while (contador <=5):
    lista.append(float(input("Insira o numero: ")))
    lista.sort()
    contador += 1
print(lista)


