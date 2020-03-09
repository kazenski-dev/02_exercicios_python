"""Entrada de dados pelo teclado - MÉTODO IMPUT

#Declaração de Variáveis
nota_1 = int
nota_2 = int

Código principal"""
print("Lembre-se que a nota inserida deve ser arredondada para um valor inteiro\n")
nota_1 = int (input("Digite a primeira nota inteira: -"))
nota_2 = int (input("Digite a segunda nota: -"))
soma = nota_1 + nota_2
print("A soma das notas é:", soma)
print(30*"-", "\n%s - é a primeira nota inserida."%(nota_1))
print("%s - é a segunda nota inserida.\n"%(nota_2), 30*"-")
