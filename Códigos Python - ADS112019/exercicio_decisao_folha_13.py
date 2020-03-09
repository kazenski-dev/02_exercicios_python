"""
Faça um programa que leia um número e exiba o dia correspondente da semana:
(1-domingo, 2-segunda, etc). Se digitar outro valor, deve aparecer invalido:
"""
#Variaveis
dia_semana = 0
validacao = 0

#Codigo Principal
while validacao ==0:
    print("1-domingo, 2-segunda, 3-terça, 4-quarta, 5-quinta, 6-sexta, -7 sabado")
    dia_semana = int(input("Digite o dia da semana:"))
    if dia_semana ==1:
        print("Domingo")
        validacao = 1
    elif dia_semana == 2:
        print("Segunda")
        validacao = 1
    elif dia_semana == 3:
        print("Terça")
        validacao = 1
    elif dia_semana == 4:
        print("Quarta")
        validacao = 1
    elif dia_semana == 5:
        print("Quinta")
        validacao = 1
    elif dia_semana == 6:
        print("Sexta")
        validacao = 1
    elif dia_semana == 7:
        print("Sabado")
        validacao = 1
    else:
        print("Opção Inválida!")
        validacao = 0