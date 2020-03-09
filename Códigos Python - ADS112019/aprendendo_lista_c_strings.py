"""
LISTA COM STRINGS:
Funcionam da mesma forma, permitindo o acesso a varios valores.

---------------------------------------------------------------
ListaStr = ["Maça,", "Pera", "Quiwi"]
print(ListaStr)
---------------------------------------------------------------
Compras = []
while True:
    produto = input("Produtos: ")
    if (produto == "fim"):
        break
    Compras.append(produto)
#APPEND adiciona um elemento no FINAL da lista
for produtos in Compras:
    print(produtos)
---------------------------------------------------------------

LISTA COM PRODUTOS DIFERENTES:

produto1 = ["maça", 10, 0, 0.38]
produto2 = ["pera", 50, 1, 0]
produto3 = ["kiwi", 5, 0, 0.99]
compras = [produto1, produto2, produto3]
print (compras)
"""