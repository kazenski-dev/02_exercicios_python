"""
Fazer um programa que imprima um relógio que imprima hora e minutos:
"""
#Variaveis
hora = 0
minuto = 0

#Codigo Primcipal
while (hora < 24):
    minuto = 1
    while (minuto < 60):
        print("%d h %d min"%(hora, minuto))
        minuto += 1
    hora += 1