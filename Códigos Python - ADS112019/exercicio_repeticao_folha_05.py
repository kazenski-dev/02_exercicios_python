"""
Altere o programa anterior...
'Supondo que a população de umpaís A seja de ordem de 80000 habitantes com uma taxa anual de crescimento
 de 3% e que a população B seja 200000 habitantes com taxa de cresimento de 1,5%. Faça um programa que calcule e
 escreva o número de anos necessários para que a população de A ultrapasse a população de B, mantidas as
 taxas de crescimento.'
 ...
 permitindo que o usuário possa informar as populações e as taxas de crescimento iniciais.
 Valide a entrada e permita repetir a operação:
"""

#Variaveis
contador_ano = 1 # A informação que preciso!
repetir = 1

#Codigo Principal
while (repetir == 1):
    populacao_a = int(input("Insira a população do país A: "))
    populacao_b = int(input("Insira a população do país B: "))
    taxa_a = float(input("Insira a taxa de crescimento do país A: "))
    taxa_b = float(input("Insira a taxa de crescimento do país A: "))
    if (populacao_a != populacao_b) and (taxa_a != taxa_b):
            while (populacao_a < populacao_b) or (populacao_b < populacao_a):
                populacao_a = populacao_a + ((populacao_a * taxa_a) / 100)
                print("Pop. de A ano:", populacao_a, "no ano",contador_ano)
                populacao_b = populacao_b + ((populacao_b * taxa_b) / 100)
                print("Pop. de B ano:",  populacao_b, "no ano", contador_ano)
                contador_ano += 1
                print("=================================")
                repetir = 0
    else:
        print("Valores idnticos, por favor reinsira os valores:\n\n")
        repetir = 1
    repetir = input("Digite '1' se deseja iniciar/refazer o procedimento: ")
print("A quantidade de anos para a pop. de A ultrapassar a pop. de B é:", contador_ano)