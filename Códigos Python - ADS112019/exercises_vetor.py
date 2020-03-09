"""EXERCÍCIOS LISTAS"""

"""
1.	Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

vetor = []
for cont in range(5):
    valor = int(input("Insira o valor do vetor: "))
    vetor.append(valor)
print(vetor)


2.	Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

vetor = []
for cont in range (2):
    valor = int(input("Insira o valor do vetor: "))
    vetor.append(valor)
vetor.reverse()
print(vetor)


3.	Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

vetor = []
for cont in range (4):
    nota = float(input("Insira a nota: "))
    vetor.append(nota)
print(vetor)
print("A soma dos cont é: ", (sum(vetor)))
print("A média do vetor é: ", (sum(vetor)/len(vetor)))

4.	Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

vetor_caractere = []
vetor_consoante = ["a", "e", "i", "o", "u"]
for cont in range(10):
    valor = input("Insira a primeira letra: ")
    vetor_caractere.append(valor)
for elem_fora in range(10):
    for elem_dentro in range(len(vetor_consoante)):
        if vetor_caractere[elem_fora] == vetor_consoante[elem_dentro]:
            print("Um consoante encontrada:" + vetor_consoante[elem_dentro])

5.	Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

vetor = []
vetor_par = []
vetor_impar = []

for cont in range(6):
    valor = int(input("Insira o valor: "))
    vetor.append(valor)
    if (valor % 2 == 0):
        vetor_par.append(valor)
    else:
        vetor_impar.append(valor)
print("Vetor: = ",vetor)
print("Vetor Par: = ",vetor_par)
print("Vetor Impar: = ",vetor_impar)

6.	Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

vetor = []
notas = []
acumulador = 0
for cont in range(10):
    for alunos in range (4):
        nota = float(input("Insira a nota: "))
        notas.append(nota)
    vetor.append(sum(notas)/len(notas))
    if (vetor[cont] >= 7):
        acumulador += 1
print("Número de alunos com média maior ou igual a SETE:", acumulador)

7.	Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

vetor = []
multiplica = 1
for cont in range (5):
    valor = int(input("Insira o valor: "))
    vetor.append(valor)
    multiplica = (multiplica * vetor[cont])
print("Vetor =", vetor)
print("Soma dos valores do vetor =", (sum(vetor)))
print("Multiplicação dos valores do vetor =", multiplica)

8.	Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

vetor_idade = []
vetor_altura = []
for cont in range(5):
    idade = int(input("Insira a idade: "))
    vetor_idade.append(idade)
    altura = float(input("Insira a altura: "))
    vetor_altura.append(altura)
vetor_idade.reverse()
vetor_altura.reverse()
print("Vetor de idades revertido = ", vetor_idade)
print("Vetor de alturas revertido = ", vetor_altura)

9.	Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos cont do vetor.

vetor = []
for cont in range (10):
    valor = int(input("Insira o valor: "))
    vetor.append(valor ** 2)
print("Vetor de cont elevados ao quadrado =", vetor)

10.	Faça um Programa que leia dois vetores com 10 cont cada. Gere um terceiro vetor de 20 cont, cujos valores deverão ser compostos pelos cont intercalados dos dois outros vetores.

vetor1 =[]
vetor2 = []
vetor3 = []
for cont in range(20):
    valor = int(input("Insira o valor: "))
    if (valor % 2 == 0):
        vetor1.insert(cont, valor)
        vetor2.insert(cont, valor)
    else:
        vetor1.insert((cont + 1), valor)
        vetor3.insert(cont, valor)
print("Vetor 1 = ", vetor2)
print("Vetor 2 = ", vetor3)
print("Vetor Intervalado = ", vetor1)

12.	Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

vetor_idade = []
vetor_altura = []
contador = 0
for cont in range (5):
    idade = int(input("Insira a %.d ª idade: ".format(cont + 1)))
    vetor_idade.append(idade)
    altura = float(input("Insira a %.2f ª altura".format(cont + 1)))
    vetor_altura.append(altura)
media = (sum(vetor_altura)/ len(vetor_altura))
for cont in range(5):
    if (vetor_idade[cont] > 13) and (vetor_altura[cont] < media):
        contador += 1
print("Vetor de idades = ", vetor_idade)
print("Vetor de idades = ", vetor_altura)
print("A media de alturas é: ", media)
print("A quantidade de alunos com mais de 13 anos e altura menor que a media geral de altura: ", contador)

13.	Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

temperaturas = []
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
for cont in range(12):
    valor = float(input("Insira a temperatura: "))
    temperaturas.append(valor)
media = (sum(temperaturas)/ len(temperaturas))
for cont in range(12):
    if (temperaturas[cont] > media):
        print((cont + 1), " - ", meses[cont], " tem temperatura ", temperaturas[cont], " acima da média ", media)

14.	Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a.	"Telefonou para a vítima?"
b.	"Esteve no local do crime?"
c.	"Mora perto da vítima?"
d.	"Devia para a vítima?"
e.	"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".


perguntas = ["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para a vítima?","Já trabalhou com a vítima?"]
contador = 0
conta_crime = 0
print("Responda as perguntas com 1-SIM, 2-NÃO\n")
while (contador < (len(perguntas))):
    print(perguntas[contador])
    resposta = int(input("Resposta: "))
    contador += 1
    if (resposta == 1):
        conta_crime += 1
if (conta_crime == 2):
    print("Você é Suspeito.")
elif(conta_crime == 3) or (conta_crime == 4):
    print("Você é Cúmplice.")
elif (conta_crime == 5):
    print("Você é Assassino.")
else:
    print("Você é Inoscente.")

15.	Faça um programa que leia um número indeterminado de valores, correspondentes a notas, 
encerrando a entrada de dados quando for informado um valor igual a -1 
(que não deve ser armazenado). Após esta entrada de dados, faça:
a.	Mostre a quantidade de valores que foram lidos;
b.	Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
c.	Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
d.	Calcule e mostre a soma dos valores;
e.	Calcule e mostre a média dos valores;
f.	Calcule e mostre a quantidade de valores acima da média calculada;
g.	Calcule e mostre a quantidade de valores abaixo de sete;
h.	Encerre o programa com uma mensagem;

valor = 0
vetor_valores = []
cont = 0
contador = 0
contador2 = 0
while (valor != -1):
    print("Insira um valor ou (-1) para SAIR.")
    valor = float(input("Insira o valor: "))
    if (valor == -1):
        print("Obrigado por usar nosso software.")
        break
    else:
        vetor_valores.append(valor)
print("Quantidade de valores lidos: ", len(vetor_valores))
print("Vetor de valores = ", vetor_valores)

media = (sum(vetor_valores)/len(vetor_valores))
vetor_valores.reverse()

while (cont < len(vetor_valores)):
    print(vetor_valores[cont])
    if (vetor_valores[cont] > media):
        contador += 1
    if (vetor_valores[cont] < 7):
        contador2 += 1
    cont += 1
print("A soma dos cont é = ", (sum(vetor_valores)))    
print("A média é = ", media)

print("Quantidade de valores acima da média: ", contador)
print("Quantidade de valores abaixo de 7: ", contador2)
print("Obrigado por usar nosso software.")


17.	Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
O resultado do atleta será determinado pela média dos cinco valores restantes. Você 
deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta 
em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve 
ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser 
conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo
	 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m	
Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m

"""
nomes = []
distancias = []
nome = " "
while (nome != ""):
    nome = input("Insira o nome: ")
    if (nome == ""):
        print("Obrigado por usar nosso software.")
        break
    nomes.append(nome)
    pulo = float(input("Insira a distância do pulo: "))
    distancias.append(pulo)

print("Vetor de nomes: ", nomes)
print("Vetor de distância dos pulos: ", distancias)



































