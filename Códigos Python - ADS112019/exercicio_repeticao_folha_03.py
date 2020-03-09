"""
Faça um programa que leia e valide as seguintes informações:
-nome: maior que 3 caracteres
-idade: entre zero e 150
-salário: maior que zero
-sexo: 'f' ou 'm'
-estado civil: 's', 'c', 'v', 'd'
"""
#Variaveis


#Codigo Principal
while True:
    nome = input("Insira seu nome: ")
    if (len(nome) > 3):
        print("Nome válido.")
        validacao_nome = 1
        while (validacao_nome == 1):
            idade = int(input("Insira sua idade (entre zero e 150): "))
            if (idade > 0) and (idade < 150):
                print("Idade válida")
                validacao_idade = 1
                while (validacao_idade == 1):
                    salario = float(input("Insira o valor do seu salário: "))
                    if (salario > 0):
                        print("Salário válido.")
                        validacao_salario = 1
                        while (validacao_salario == 1):
                            sexo = input("Insira seu sexo: M - masculino ou F - feminino: ").upper()
                            if (sexo == "M") or (sexo == "F"):
                                print("Sexo válido.")
                                validacao_sexo = 1
                                while (validacao_sexo == 1):
                                    estado_civil = input(
                                        "Insira seu estado civil, 'C'-casado, 'S'-solteiro, 'V'-vúvo ou 'D'-divorciado: ").upper()
                                    if (estado_civil == "C") or (estado_civil == "S") or (estado_civil == "V") or (
                                            estado_civil == "D"):
                                        print("Estado cicil válido.")
                                        validacao_sexo = 0
                                        validacao_civil = 0
                                        validacao_salario = 0
                                        validacao_idade = 0
                                        validacao_nome = 0
                                        break
                                    break
                                break
                                       # Aqui eu poderia pedir pra imprimir todos dados p/ usuário ver.
                            else:
                                print("Sexo inválido, favor digite novamente.")
                            break
                    else:
                        print("Salário inválido, favor digite novamente.")
                    break
            else:
                print("Idade inválida, favor digite novamente.")
        break
    else:
        print("Nome inválido, favor digite novamente.")
