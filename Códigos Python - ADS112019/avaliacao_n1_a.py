"""
Crie um script usando todos os recursos aprendidos (REPETIÇÃO, CONDIÇÃO, VARIÁVEIS, CONSTANTES)
a)Ler a idade de 15 pessoas, mostrar:
- quantidade de crianças (0 a 11 anos)
- quantiade de jovens (12 a18 anos)
- quantidade de alunos (19 a 60 anos)
- quantidade de idosos (maiores que 60)
"""
#Variaveis
idade = 0
conta_crianca = 0
conta_jovens = 0
conta_adultos = 0
conta_idosos = 0
contador_while = 0

#Codigo Principal
while (contador_while < 15):
    idade = int(input("Digite a idade: "))
    if (idade >= 0) and (idade <= 11):
        conta_crianca += 1
    elif (idade >= 12) and (idade <= 18):
        conta_jovens += 1
    elif (idade >= 19) and (idade <= 60):
        conta_adultos += 1
    else:
        conta_idosos += 1
    contador_while += 1
print("Quantiade de crianças: ", conta_crianca)
print("Quantiade de jovens: ", conta_jovens)
print("Quantiade de adultos: ", conta_adultos)
print("Quantiade de idosos: ", conta_idosos)


