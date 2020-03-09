"""
PROVA 1
Desenvolva um script que leia o peso e a altura de 10 pessoas.
Calcule o IMC (Indice de Massa Corpórea) e mostre seu status de acordo com a tabela abaixo:
       Indice      /     Mensagem
abaixo de 18.5     /  Abaixo do peso
Entre 18.5 e 25    /  Peso Ideal
Entre 25 até 30    /  Sobrepeso
Entre 30 até  40   /  Obesidade
Acima de 40        /  Obesidade Mórbida

Ao final imprima:
a) A quantidade de pessoas abaixo do peso;
b) A quantidade de pessoas no peso ideal;
c) A quantidade de pessoas com sobrepeso;
d) A quantidade de pessoas com obesidade;
e) A quantidade de pessoas com obesidade mórbida;
f) O total de pesos lidos;
g) A média total dos pesos;
h) A maior altura;
i) O maior peso;

"""
#Variaveis
cont = 1 # controla meu loop
abaixo_peso = 0
peso_ideal = 0
sobre_peso = 0
obeso = 0
obeso_morbido = 0
conta_pesos = 0 #Vai somar peso em KG atual + novo peso a cada iteração
contador_peso = 1 #Aqui vou contar quantos pesos foram inseridos, não a soma do KG deles
media_pesos = 0
maior_altura = 0
maior_peso = 0
imc = 0 #aqui vou calcular o IMC com cada dupla de peso e altura (peso /(altura * altura))

#Codigo Principal
while (cont <= 10):
    peso = float(input("Digite o peso: "))
    altura = float(input("Digite a altura: "))
    imc = (peso /(altura * altura))         #Até aqui somente coletei informações e calculei o IMC
    conta_pesos = conta_pesos + peso #Aqui vou acumular os pesos
    if (imc < 18.5): #Qui inicio a validação do tipo de imc
        abaixo_peso += 1
    elif (imc > 18.5) and (imc <= 25):
        peso_ideal += 1
    elif (imc > 25) and (imc <= 30):
        sobre_peso += 1
    elif (imc > 30) and (imc <= 40):
        obeso += 1
    else:
        obeso_morbido += 1
    if(peso > maior_peso):  #Aqui valido se o peso é maior que o meu maior peso
        maior_peso = peso
    if (altura > maior_altura):   #Aqui valido se a altura é maior que a minha maior altura
        maior_altura = altura
    contador_peso += 1
    cont += 1
media_pesos = (conta_pesos / contador_peso)
#Agora eu vou imprimir todos resultados
print("A quantidade de pessoas abaixo do peso é: ", abaixo_peso)
print("A quantidade de pessoas no peso ideal é: ", peso_ideal)
print("A quantidade de pessoas com sobrepeso é: ", sobre_peso)
print("A quantidade de pessoas com obesidade é: ", obeso)
print("A quantidade de pessoas com obesidade mórbida é: ", obeso_morbido)
print("O total de pesos lidos é: ", conta_pesos)
print("A média total dos pesos é: ", media_pesos)
print("A maior altura é: ", maior_altura)
print("O maior peso é: ", maior_peso)