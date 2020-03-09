"""
PESQUISA DE ELEMENTOS
- podemos pesquisar se está ou nao na lista
"""
#PESQUISA SEQUENCIAL
lista = [15, 7, 17, 39]
procurado = int(input("Digite o valor a ser procurado: "))
achou = False
contador_x = 0

while contador_x < (len(lista)):
    if lista[contador_x] == procurado:
        achou = True
        break
    contador_x += 1
if achou == True:
    print("Valor %d achado na lista, na posição %d." %(procurado, contador_x))
else:
    print("Valor %d NÂO foi encontrado na lista" % (procurado))