"""
FATIANDO STRING
"""
nome = "TAKEHIKO MARUYAMA"
print(nome[:6]) #aqui to fatiando do inicio ate meu limite 6

#-------------------------------------------------------------------------------------#
#Achar um pedaco de string

nome = "TAKEHIKO MARUYAMA"
print("re" in nome)
print("ru" in nome)
#ambos deram false porque tem o sense case que nao acha esse pedaco de string no nome

#-------------------------------------------------------------------------------------#
#Imprimir o tamanho de uma string

nome = "TAKEHIKO MARUYAMA"
print(len(nome)) #Imprime os indices de ZERO ate o final

#-------------------------------------------------------------------------------------#
#Imprimir em minusculo e em maiusculo

nome = "TAKEHIKO MARUYAMA"
print(nome.lower())
print(nome.upper())

#-------------------------------------------------------------------------------------#
#Imprimir a string - retornando cada palavra que for separada por ESPAÇO, em elementos de uma lsita

nome = "TAKEHIKO MARUYAMA"
print(nome.split())


