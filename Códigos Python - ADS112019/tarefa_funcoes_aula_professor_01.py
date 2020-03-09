"""
Faça um script com uma função com três argumentos e que retorne 3 argumentos.
"""
def soma (valor1, valor2, valor3):
    soma = (valor1 + valor2 + valor3)
    return soma

#Codigo Principal
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
print("A soma é: ", soma(nota1, nota2, nota3))

#Codigo Principal
idade1 = 18
idade2 = 36
idade3 = 57
print("A soma das idades é: ", soma(idade1, idade2, idade3))

#Codigo principal
valor1 = 19
valor2 = 60
valor3 = 99
print("A soma dos valores é: ", soma(valor1, valor2, valor3))
