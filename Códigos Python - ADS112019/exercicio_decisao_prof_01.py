"""1. Faça um script para duas notas parciais de um aluno. O programa deve
calcular a media alcançada por aluno e apresentar:
A mensagem 'Aprovado': - se a media alcançada for maior ou igual a sete.
A mensagem 'Reprovado': - se a media alcançada for menor do que sete.
A mensagem 'Aprovado com Distinção': - se a media for igual a dez."""

#Código Principal:
nota_01 = float(input("Insira a primeira nota: "))
nota_02 = float(input("Insira a segunda nota: "))
media = (nota_01 + nota_02)/2
if media == 10:
    print("Aprovado com distinção. Parabens!")
elif media >=7:
    print("Aprovado com nota: ",media)
else:
    print("Reprovado")
