"""
Faça um programa que peça 3 valores doo lados do trilangulo. O programa deve informar
se os valores podem ser um triangulo. Indique, caso os lados formem um triangulo equilátero,
isosceles ou escaleno.
Dicas:
-tres lados iguais formam triangulo equilatero
-dois lados iguais formam triangulo isosceles
-tres lados iferentesformam triangulo escaleno
"""
#Variaveis
lado_1 = int(input("Insira o primeiro valor do lado: "))
lado_2 = int(input("Insira o segundo valor do lado: "))
lado_3 = int(input("Insira o terceiro valor do lado: "))

#Codigo Principal
if (lado_1 == lado_2) and (lado_1 == lado_3) and (lado_2 == lado_3):
    print("Esses valores formam um triângulo equilátero.")
elif (lado_1 == lado_2) or (lado_1 == lado_3) :
    print("Esses valores formam um triângulo isosceles.")
elif (lado_2 == lado_1) or (lado_2 == lado_3):
    print("Esses valores formam um triângulo isosceles.")
else:
    print("Esses valores formam um triângulo escaleno.")