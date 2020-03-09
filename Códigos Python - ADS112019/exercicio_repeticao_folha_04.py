"""
Supondo que a população de umpaís A seja de ordem de 80000 habitantes com uma taxa anual de crescimento
 de 3% e que a população B seja 200000 habitantes com taxa de cresimento de 1,5%. Faça um programa que calcule e
 escreva o número de anos necessários para que a população de A ultrapasse a população de B, mantidas as
 taxas de crescimento.
"""
#Variaveis
populacao_a = 80000
populacao_b = 200000
taxa_a = 3
taxa_b = 1.5
contador_ano = 1 # A informação que preciso!

#Codigo Principal
while (populacao_a <= populacao_b):
    populacao_a = populacao_a + ((populacao_a * taxa_a) / 100)
    print("Pop. de A ano:", populacao_a, "no ano",contador_ano)
    populacao_b = populacao_b + ((populacao_b * taxa_b) / 100)
    print("Pop. de B ano:",  populacao_b, "no ano", contador_ano)
    contador_ano += 1
    print("===================")
print("A quantidade de anos para a pop. de A ultrapassar a pop. de B é:", (contador_ano - 1))