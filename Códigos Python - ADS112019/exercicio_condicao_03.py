"""Calcular a conta de um telefone celular na empresa Tchau
Os planos da empresa são bem interessantes e oferecem preços
diferenciados com a quantidade de minutos usados por mês.
Abaixo de 200 minutos, a empresa cobra R$ 0,20 por minuto
Entre 200 e 400 minutos, o preço é de R$ 0,18. Acima de 400
minutos, o preço por minuto é de R$ 0,15."""

#Código Principal
minutos = int (input("Quantos minutos você utilizou neste mês?"))
if minutos < 200:
    preco = 0.20
    print("Você utilizou",minutos, "minutos, com tarifa de: R$%6.2f"%(preco))
    print("Valor a ser cobrado: R$%6.2f " %(minutos * preco))
else:
    if (200 >= minutos < 400):
        preco = 0.18
        print("Você utilizou",minutos, "minutos, com tarifa de: R$%6.2f"%(preco))
        print("Valor a ser cobrado: R$%6.2f " %(minutos * preco))
    else:
        preco = 0.15
        print("Você utilizou",minutos, "minutos, com tarifa de: R$%6.2f"%(preco))
        print("Valor a ser cobrado: R$%6.2f " %(minutos * preco))
