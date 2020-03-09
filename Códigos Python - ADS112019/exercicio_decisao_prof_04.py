"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe
contrataram para desenvolver um programa que calcula´ra os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste seguindo o seginte critério, baseado no salário:
-salários até R$ 280,00 (incluindo): aumento de 20%
-salários entre R$280,00 e R$ 700,00 : aumento de 15%
-salários entre R$700,00 e R$ 1500,00 : aumento de 10%
-salários de R$ 1500,00 em diante : aumento de 5%
Após o aumento ser realizado, informe na tela:
-o salário antes do reajuste
-o percentual do aumento aplicado
-o valor do aumento
-o novo salário, após o reajuste
"""

#Variaveis
salario = float(input("Insira o valor do seu salário: "))
reajuste = 0
salario_reajustado = 0

#Codigo Principal
if (salario <= 280):
    reajuste = 20
elif (salario>280) and (salario<=700):
    reajuste = 15
elif (salario>700) and (salario<=1500):
    reajuste = 10
elif (salario>1500):
    reajuste = 5
salario_reajustado = salario + (salario * reajuste)/100
print("Salário base: R$", salario)
print("Percentual de reajuste: ", reajuste, "%")
print("Valor do aumento: R$", (salario_reajustado-salario))
print("Salário atualizado: R$", salario_reajustado)




