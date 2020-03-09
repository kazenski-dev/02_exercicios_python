"""
Iniciamos pedindo uma letra ao usuário e armazenando na variável 'resposta' que vai ser
uma String. Se digitou M - é masculino, F - feminino
"""

#Codigo Principal
resposta = input("Insira M - masculino ou F - feminino").upper()
if (resposta == "M"):
    print("Você inseriu sexo Masculino.")
else:
    print("Você inseriu sexo Feminino.")