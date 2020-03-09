"""
INTERROMPENDO A REPETIÇÃO - BREAK
"""
#Variaveis
soma = 0

#Codigo Principal
while True: #Aqui o WHILE inicia DIRETO - forço ele a começar
    valor_usuario = int(input("Insira o valor a ser somado ou ZERO para sair:"))
    if valor_usuario == 0:
        break
    soma = soma + valor_usuario
print("A soma é:",soma)