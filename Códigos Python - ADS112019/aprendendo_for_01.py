"""
USANDO FOR
WHILE oU FOR
- WHILE:
- FOR:
"""
lista = [8, 9,15]
for elementos in lista:
    print(elementos)

"""lista_dois = [8, 9, 15]
contador = 0
while (contador < len(lista_dois)):
    elementos  = lista_dois[contador]
    print(elementos)
    contador += 1"""

lista_tres = [8, 9, 15, 20, 48]
procurando = int(input("Digite o valor que deseja procurar: "))
for elementos in lista_tres:
    if elementos == procurando:
        print("Elemento encontrado na posição:")
        break
else:
    print("Elemento não encontrado.")