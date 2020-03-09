"""
Crie um script usando todos os recursos aprendidos (REPETIÇÃO, CONDIÇÃO, VARIÁVEIS, CONSTANTES)
b)Ler a idade e nome de 15 pessoas, mostrar:
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
    nome = input("Digite seu nome: ")
    idade = int(input("Digite a idade: "))
    if (idade >= 0) and (idade <= 11):
        conta_crianca += 1
        print("Menor de idade.")
    elif (idade >= 12) and (idade <= 18):
        conta_jovens += 1
        print("Maior de idade.")
    elif (idade >= 19) and (idade <= 60):
        conta_adultos += 1
        print("Maior de idade.")
    else:
        conta_idosos += 1
        print("Idoso")
    contador_while += 1
print("Quantiade de crianças: ", conta_crianca)
print("Quantiade de jovens: ", conta_jovens)
print("Quantiade de adultos: ", conta_adultos)
print("Quantiade de idosos: ", conta_idosos)


