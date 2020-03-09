"""Exemplo com 3 variáveis de controle"""

#Variáveis:
gremio = 0
cruzeiro = 0
sao_jose = 0
numero_alunos = 0
time = 0

#Código Principal
numero_alunos = int (input ("Insira o total de times que deseja analisado: "))
while (gremio + cruzeiro + sao_jose) < numero_alunos:
    time = int (input("Insira o time: 1 para Grêmio/ 2 para Cruzeiro/ 3 para São José: "))
    if time == 1:
        gremio = gremio + 1
    elif time == 2:
        cruzeiro = cruzeiro + 1
    elif time == 3:
        sao_jose = sao_jose + 1
print("Chegamos a um total de times devidamente classificados:")
print("O total de alunos que torcem para o Grêmio é: ", gremio)
print("O total de alunos que torcem para o Cruzeiro é: ", cruzeiro)
print("O total de alunos que torcem para o ão José é: ", sao_jose)
