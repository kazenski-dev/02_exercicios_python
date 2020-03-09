"""
REPETIÇÃO ALINHADA
Desenhe a tabuada do 1
"""
#Variaveis
tabuada = 1

#Codigo Principal
while (tabuada <= 10):
    numero = 1
    while (numero <= 10):
        print("%d X %d = %d"%(tabuada, numero, tabuada * numero))
        numero += 1
    print("================")
    print("Tabuada do: ", numero)
    tabuada += 1