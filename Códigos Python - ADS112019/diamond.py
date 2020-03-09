"""CODIGO DO DIAMANTE FODASTICO"""

caractere_natural = input("Insira o caractere que deseja ser a matriz toda: ")
caractere_desenho = input("Insira o caractere que deseja ver formando o diamante: ")
#Primeira parte do diamante
diamante =[caractere_natural,caractere_natural,caractere_natural,caractere_natural,caractere_natural,caractere_natural,caractere_natural,caractere_natural,caractere_natural,caractere_natural]
inicio = 4
final = 4
linhas = 0

while (linhas <= 4):
    diamante[inicio] = caractere_desenho
    diamante[final] = caractere_desenho
    inicio -= 1
    final += 1
    linhas += 1
    print(diamante)

#Segunda parte do diamante
inicio = 0
final = 8
linhas = 1
while (linhas <= 4):
    inicio += 1
    final -= 1
    linhas += 1
    diamante[inicio - 1] = caractere_natural
    diamante[final + 1] = caractere_natural
    print(diamante)




