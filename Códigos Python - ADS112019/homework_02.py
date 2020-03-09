"""Tendo como dados de entrada a distância total(em km) percorrida por um automóvel e a
 quantidade de combustível(em litros) consumida para percorê-la, calcule e imprima
 o consumo médio de combustível:"""

#Variaveis
DISTANCIA = float
COMBUSTIVEL = float
consumo_medio = float

#Codigo principal
DISTANCIA = float(input("Insira o valor da distância em km: "))
COMBUSTIVEL = float(input("Insira o valor de combustível utilizado em litros: "))
consumo_medio = DISTANCIA/COMBUSTIVEL
print("O consumo médio de combustível é de = : ", consumo_medio)
