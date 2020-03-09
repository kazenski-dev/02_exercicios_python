"""Um funcionário de uma empresa recebe R$x.xxx,xx de salário. Ao atingir  sua meta de produtividade
esse funcionário receberá uma bonificação de xx% do seu salário. Ajude o dedicado funcionário a descobrir
quantos reais ele receberá no fim do mês, caso atingir sua meta.
Escreva um programa em Phyton que possua uma variável -salario- do tipo float com valor inicial xxxx
e uma variável -novo_salario- que receberá o salário final com bonificação. O programa deve exibir o
valor da variável -novo_salario. """

#Variaveis
salario = float
BONIFICACAO = float
meta = 0
salario_final = float

#Codigo principal
salario = float(input("Insira o valor de seu salário base: R$ "))
bonificacao = float(input("Insira o valor de porcentagem de bônus: % "))
meta = int(input("Você bateu a meta? 0-não/1-sim: "))
if meta == 0:
    print("Seu salário não sofreu alteração: R$ %.2f"%(salario))

else:
    salario_final = salario+(salario*BONIFICACAO/100)
    print("Parabens! Você bateu sua meta! Seu salário, este mês, será de: R$ %.2f"%(salario_final))
