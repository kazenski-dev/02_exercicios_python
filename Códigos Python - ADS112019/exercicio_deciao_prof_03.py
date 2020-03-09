"""Faça um programa que pergunte em que turno você estuda. Peça para digitar M- matutino, V- vespertinoou N- noturno.
Imprima a mensagem 'Bom dia', 'Boa tarde' oi 'Boa noite', comforme o caso."""

#Variaveis
turno = input("Digite o turno que você estuda:\nM - matutino, V - Vespertino ou N - Noturno: ")
if (turno == "M") or (turno == "m"):
    print("Bom dia.")
elif (turno == "V") or (turno == "v"):
    print("Boa tarde.")
elif (turno == "N") or (turno == "n"):
    print("Boa noite.")
else:
    print("Opção Inválida.")