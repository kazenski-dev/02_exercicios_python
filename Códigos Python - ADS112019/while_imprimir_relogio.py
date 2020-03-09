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
        segundo = 0
        while (segundo < 60):
            print("%d h %d min %d seg"%(hora, minuto, segundo))
            segundo+= 1
        minuto += 1
    hora += 1