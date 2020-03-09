"""
Faça um programa que leia um nome de usuário e senha e não aceite a senha igual ao nome de usuário,
mostrando uma mensagem de erro e voltando a pedir as informações:
"""
#Variaveis

#Codigo Principal
while True:
    usuario = input("Insira o nome de usuário: ").upper()
    senha = input("Insira sua senha: ").upper()
    if (senha == usuario):
        print("Senha igual a usuário. Favor insira uma senha diferente do usuário: ")
    else:
        print("Acesso permitido.")
        print("Seja bem vindo", usuario)
        break
