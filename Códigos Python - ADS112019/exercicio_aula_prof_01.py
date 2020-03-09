"""
Crie um script em Phyton que insira números ate´que seja digitado 0 para sair.
Conte a quantidade de numeros inseridos:

#Variaveis
contador = 0

#Codigo principal
while True:
    num = int(input("Digite um número: "))
    if(num ==0):
        break
    contador += 1
print("Você inseriu ", contador, "números.")

"""
#Variaveis
contador = -1 #Porque quando eu inserir o ZERO, vai passar pelo LOOP,
              # então isso vai "anular" essa ultima entrada
num = 1

#Codigo principal
while (num != 0):
    num = int(input("Digite um número: "))
    contador += 1
print("Você inseriu ", contador, "números.")
