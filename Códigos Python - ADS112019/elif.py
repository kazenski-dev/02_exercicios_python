# ELIF

#Código Principal
categoria = int (input("Digite as categorias do produto: "))
if categoria == 1:
    preco = 10
elif categoria == 2:
    preco = 18
elif categoria == 3:
    preco = 23
elif categoria == 4:
    preco = 26
elif categoria == 5:
    preco = 31
else:
    print("Categoria Inválida, digite um número entre 1 e 5")
    preco = 0
print("O preço do produto é R$" ,preco)
