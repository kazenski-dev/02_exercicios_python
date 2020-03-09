"""Excreva um programa que pergunte a velocidade do carro de um usuario
Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi
multado. Nesse caso exiba o valor da multa cobrado, cobrando R$ 5,00 por km
acima de 80km/h"""

#Variaveis:
CONTROLE = 80
multiplicador_multa = 5

#Código Principal:
velocidade = float (input("Digite a velocidade do carro:"))
if velocidade>CONTROLE:
    print("Você ultrapassou o limite de velocidade e foi multado!\nCalculando valor . . . ")
    multa = (velocidade - CONTROLE)* multiplicador_multa
    print("O valor da multa é de: R$%4.2f"%(multa))
else:
    print("Velocidade dentro do permitido.")
