""" ======== MINHA LISTA COMPLETA DE FUNÇÕES ========"""

""" 01- Função que calcula a area de um retangulo"""
def area_retangulo (lado_1, lado_2):
    return (lado_1 * lado_2)

"""------------------------------------------------"""

""" 02- Função que calcula a area de um triangulo"""
def area_triangulo (base, altura):
    return ((base * altura) / 2)

"""------------------------------------------------"""

""" 03- Função que calcula a area de um circulo"""
def area_circulo (raio):
    return (3.14 * (raio ** 2))

"""------------------------------------------------"""

""" 04- Função que calcula o IMC com entrada de dado de peso """
def calculo_imc (peso, altura):
    definicao_imc = ""
    imc = (peso / (altura * altura))  # Até aqui somente coletei informações e calculei o IMC
    if (imc < 18.5): #Qui inicio a validação do tipo de imc
        definicao_imc = "Abaixo do peso."
    elif (imc > 18.5) and (imc <= 25):
        definicao_imc = "Peso ideal."
    elif (imc > 25) and (imc <= 30):
        definicao_imc = "Acima do peso."
    elif (imc > 30) and (imc <= 40):
        definicao_imc = "Obeso."
    else:
        definicao_imc = "Obeso mórbido."
    return definicao_imc

"""------------------------------------------------"""

""" 04.A - Função que calcula o IMC com entrada de dado de peso """
def calculo_imc2 (numero_anlises, decisao):
    abaixo_peso = 0
    peso_ideal = 0
    sobrepeso = 0
    obeso = 0
    obeso_morbido = 0
    contador = 1
    while (contador <= numero_anlises):
        peso = float(input("Insira o peso: "))
        altura = float(input("Insira a altura: "))
        imc = (peso / (altura * altura))  # Até aqui somente coletei informações e calculei o IMC
        if (imc < 18.5): #Qui inicio a validação do tipo de imc
            abaixo_peso += 1
        elif (imc > 18.5) and (imc <= 25):
            peso_ideal += 1
        elif (imc > 25) and (imc <= 30):
            sobrepeso += 1
        elif (imc > 30) and (imc <= 40):
            obeso += 1
        else:
            obeso_morbido += 1
        contador += 1
    if (decisao == "1"):
        return ("Quantidade total de pesos classificados.\nAbaixo do peso: ", abaixo_peso, "Peso ideal: ", peso_ideal, "Sobre peso: ", sobrepeso, "Obeso: ", obeso, "Obeso mórbido: ", obeso_morbido)
    elif(decisao == "A"):
        return print("Abaixo do peso: ", abaixo_peso)
    elif (decisao == "B"):
        return print("Peso ideal: ", peso_ideal)
    elif (decisao == "C"):
        return print("Sobre peso: ", sobrepeso)
    elif (decisao == "D"):
        return print("Obeso: ", obeso)
    elif (decisao == "E"):
        return print("Obeso mórbido: ", obeso_morbido)
    else:
        return print("Sem retorno posível. Obrigado por usar nosso software.")

"""------------------------------------------------"""

""" 04.B - Função que calcula o IMC"""
def imc(peso, altura):
    return (peso / (altura * altura))

"""------------------------------------------------"""

""" 05- Função que calcula o maior valor"""
def maior_valor (numero_002, maior):
    if(numero_002 > maior):  #Aqui valido se o peso é maior que o meu maior peso
        maior = numero_002
        return maior

"""------------------------------------------------"""

""" 05.A - Função que calcula o maior valor: """
def maior_valor1 (numero_valores):
    contador = 0
    maior = 0
    while (contador < numero_valores):
        num_usuario = float(input(("Insira o valor: ")))
        if (num_usuario > maior):
            maior = num_usuario
        contador += 1
    print("O maior valor é:", maior)

"""------------------------------------------------"""

""" 05.B - Função que calcula maior valor"""
def maior_valor2 (*argumentos):
    print (max(argumentos))
    return max(argumentos)

"""------------------------------------------------"""

""" 06- Função que calcula menor valor"""
def menor_valor (numero_001, menor):
    if(numero_001 < menor):  #Aqui valido se o peso é maior que o meu maior peso
        menor = numero_001
        return menor

"""------------------------------------------------"""

""" 06.A- Função que calcula menor valor"""
def menor_valor1 (numero_valores):
    contador = 0
    menor = 9999999999999999999999999999999999999999
    while (contador < numero_valores):
        num_usuario = float(input(("Insira o valor: ")))
        if (num_usuario < menor):
            menor = num_usuario
        contador += 1
    print("O menor valor é:", menor)

"""------------------------------------------------"""

""" 06.B - Função que calcula menor valor"""
def menor_valor2 (argumentos):
    print (min(argumentos))
    return min(argumentos)

"""------------------------------------------------"""

""" 07- Função que calcula a media de N valores"""
def media (soma_total, numero_valores):
    return (soma_total / numero_valores)

"""------------------------------------------------"""

""" 08- Função que calcula Tabuada"""
def tabuada (MULTIPLICADOR, num_inicial, num_final):
    while (num_inicial <= num_final):
        print("", MULTIPLICADOR, "X", num_inicial, " = ", (MULTIPLICADOR * num_inicial))
        num_inicial = num_inicial + 1

"""------------------------------------------------"""

""" 09- Função que calcula o valor do salario"""
def salario (qtd_horas, valor_hora):
    return (qtd_horas * valor_hora)

"""------------------------------------------------"""

""" 09.A- Função que calcula o valor do salario"""
def calcular_pagamento (qtd_horas, valor_hora):
    #Agora converto esses valores para FLOAT, para eu trabalhar com $$
    horas = float (qtd_horas)
    taxa = float (valor_hora)
    if (horas <= 40):
        salario = (horas * taxa)
    else:
        horas_excedentes = horas - 40
        salario = (40 * taxa) + (horas_excedentes * (1.5 * taxa))
    return salario

"""------------------------------------------------"""

""" 10- Função que calcula se é Numero PAR ou IMPAR"""
def par_ou_impar (numero):
    if (numero % 2 == 0):
        print("É número PAR.")
    else:
        print("É número IMPAR.")

"""------------------------------------------------"""

""" 11- Função que funcione como uma Calculadora - ADICAO """
def calculadora_adicao (numero_01, numero_02):
    soma = (numero_01 + numero_02)
    return soma

"""------------------------------------------------"""

""" 12- Função que funcione como uma Calculadora - SUBTRAÇÃO """
def calculadora_subtracao (numero_01, numero_02):
    subtracao = (numero_01 - numero_02)
    return subtracao

"""------------------------------------------------"""

""" 13- Função que funcione como uma Calculadora - MULTIPLICAÇÃO """
def calculadora_multiplicacao (numero_01, numero_02):
    produto = (numero_01 * numero_02)
    return produto

"""------------------------------------------------"""

""" 14- Função que funcione como uma Calculadora - DIVISÃO """
def calculadora_divisao (numero_01, numero_02):
    divisao = (numero_01 / numero_02)
    return divisao

"""------------------------------------------------"""

""" 15- Função que calcula a velocidade média - FÍSICA """
def velocidade_media (espaco, tempo):
    vel_media = (espaco / tempo)
    print("A velocidade média é:{} m/s".format(vel_media))

"""------------------------------------------------"""

""" 16- Função que calcule o fatorial"""
def fatorial (numero):
    fatorar = 1
    while (numero > 0):
        fatorar = (fatorar * numero)
        numero -= 1
    print("O fatorial desse número é:", fatorar)

"""------------------------------------------------"""

""" 16.A - Função que calcule o fatorial"""
def fatorial2 (numero):
    fatorar = 1
    for elemento in range (1, (numero +1)):
        fatorar = (fatorar * numero)
    print("O fatorial desse número é:", fatorar)

"""------------------------------------------------"""

""" 17- Função que imprima uma lista na ordem INVERSA"""
def lista_inversa (tamanho_lista):
    lista = []
    contador = 0
    while (contador < tamanho_lista):
        nome = input("Digite seu nome: ")
        idade = float(input("Digite sua idade: "))
        sexo = input("Digite seu sexo: M- maculino ou F- feminino: ")
        lista.append(nome)
        lista.append(idade)
        lista.append(sexo)
        lista.reverse()
        contador += 1
    print(lista)

"""------------------------------------------------"""

""" 18- Função que mostre a nota do aluno em LETRA"""
def boletim (numero_notas):
    contador = 0
    soma = 0
    avaliacao = ""
    while (contador < numero_notas):
        nota = float(input("Insira o valor da nota: "))
        soma= soma + nota
        contador += 1
    media = (soma / (contador + 1))
    if (media == 10):
        avaliacao = "Aprovado = A+"
    elif (media >= 7.5) and (media <10):
        avaliacao = "Aprovado = A"
    elif (media >= 6 ) and (media < 7.5):
        avaliacao = "Aprovado = B"
    elif (media >= 4 ) and (media < 6):
        avaliacao = "Aprovado = C"
    elif (media >= 0 ) and (media < 4):
        avaliacao = "Reprovado = D"
    else:
        avaliacao = "Reprovado = E"
    return avaliacao

"""------------------------------------------------"""

""" 19- Função que imprima um número lado a lado/ embaixo - usuário define"""
def imprimir_num_lado (numero_limite, tipo_impressao):
    contador = 0
    if (tipo_impressao == 1):
        while (contador < numero_limite):
            print(contador, end= " .")
            contador += 1
        print("\n")
    else:
        while (contador < numero_limite):
            print(contador)
            contador += 1
        print("\n")

"""------------------------------------------------"""

""" 20- Função que imprima um intervalo de números inteiros - USUARIO define inicio e fim"""
def intervalo_personalizado (primeiro_num, ultimo_num):
    while (primeiro_num <= ultimo_num):
        print(primeiro_num, end= " .")
        primeiro_num += 1
    print("\n")

"""------------------------------------------------"""

""" 21- Função que imprima a série Fabonacci pelo nº do USUARIO"""
def fibonacci_usuario (numero_iteracoes):
    anterior = 0
    posterior = 0
    contador = 0
    while (contador < numero_iteracoes):
        print(posterior)
        posterior = posterior + anterior
        anterior = posterior - anterior
        if (posterior == 0):
            posterior += 1
        contador += 1

"""------------------------------------------------"""

""" 22- Função similar a MERCADO queretorna valor total e produtos:"""
def banco_produtos (codigo):
    quantidade = 0
    total_pagar = 0
    soma = 0
    preco = 0
    invalido = 0
    contador = 1 #usado para contar os itens comprados
    while (codigo > 0):
        print("---------------------------------")
        print("Produto                    Código")
        print("Cachorro Quente             100  ")
        print("Bauru Simples               101  ")
        print("Bauru com Ovo               102  ")
        print("Hambúrger                   103  ")
        print("Cheesebúerger               104  ")
        print("Refrigerante                105  ")
        print("---------------------------------")
        codigo = int(input("Insira o código do produto: \n-- Ou digite 0 (zero) para finalizar a compra. --"))
        if (codigo == 100):
            produto = "Cachorro Quente"
            preco = 1.20
            quantidade = int(input("Insira a quantidade que deseja: "))
            print(quantidade,  "º x Cachorro Quente R$", preco)
        elif (codigo == 101):
            produto = "Bauru Simples"
            preco = 1.30
            quantidade = int(input("Insira a quantidade que deseja: "))
            print(quantidade,  "º x Bauru Simples R$", preco)
        elif (codigo == 102):
            produto = "Bauru com Ovo"
            preco = 1.50
            quantidade = int(input("Insira a quantidade que deseja: "))
            print(quantidade, "º x Bauru com Ovo R$", preco)
        elif (codigo == 103):
            produto = "Hambúrger"
            preco = 1.20
            quantidade = int(input("Insira a quantidade que deseja: "))
            print(quantidade, "º x Hambúrger R$", preco)
        elif (codigo == 104):
            produto = "Cheesebúerger"
            preco = 1.30
            quantidade = int(input("Insira a quantidade que deseja: "))
            print(quantidade, "º x Cheesebúerger R$", preco)
        elif (codigo == 105):
            produto = "Refrigerante"
            preco = 1.00
            quantidade = int(input("Insira a quantidade que deseja: "))
            print(quantidade, "º x Refrigerante R$", preco)
        else:
            print("Código Inválido. Compra finalizada.")
            invalido = 1

        soma = (quantidade * preco)
        total_pagar = (total_pagar + soma)
        contador += 1
        print("Toral parcial = R$ ", total_pagar)

        if (invalido == 0):
            print("Total a pagar: R$", total_pagar)

"""------------------------------------------------"""

""" 23- Função que imprima uma agenda diária de 15 em 15 min"""
def agenda_diaria (intervalo_minutos): #esse argumento definirá de quantos em quantos min
    for hora in range (6, 22): #6 porque começará as 6h manha e termina as 22h da noite
        for minuto in range (0, 60, intervalo_minutos):
            print("- " + str(hora) + ": " + str(minuto) + " = ")

"""------------------------------------------------"""

""" 24- Função que imprime um DIAMENTE de caracteres """
def diamante (char_desenho, char_base):
    # Primeira parte do diamante
    diamante = [char_base, char_base, char_base, char_base, char_base,
                char_base, char_base, char_base, char_base, char_base]
    inicio = 4
    final = 4
    linhas = 0

    while (linhas <= 4):
        diamante[inicio] = char_desenho
        diamante[final] = char_desenho
        inicio -= 1
        final += 1
        linhas += 1
        print(diamante)

    # Segunda parte do diamante
    inicio = 0
    final = 8
    linhas = 1
    while (linhas <= 4):
        inicio += 1
        final -= 1
        linhas += 1
        diamante[inicio - 1] = char_base
        diamante[final + 1] = char_base
        print(diamante)

"""------------------------------------------------"""

""" ------------  FUNCOES COM LISTAS  ------------"""

""" 25- Função que ordene uma lista de nºs INTEIROS"""
def ordenar_lista(quantidade):
    lista = []
    for elementos in range(quantidade):
        notinha = int(input("Insira o valor da lista: "))
        lista.append(notinha)
        lista.sort()
    print(lista)
#para inserir float, somente trocar o tipo da variavel 'notinha'

"""------------------------------------------------"""

""" 26- Função que soma os valores da lista e depois imprime ela"""
def soma_lista (numero_elementos):
    lista = []
    for elementos in range(numero_elementos):
        valor = input("Insira a nota: ")
        lista.append(valor)
    print(len(lista)+1)

"""------------------------------------------------"""

""" 27- Função que calcule a media de uma lista"""
def media_lista (numero_notas):
    lista_notas = []
    for elementos in range(numero_notas):
        nota = float(input("Insira a nota: "))
        lista_notas.append(nota)
        print(lista_notas.sort())
    print(lista_notas)
    print("A média é: ", (sum.lista_notas / len(lista_notas)))

"""------------------------------------------------"""

""" 28- Função que procura um caractere especifico na STRING"""
def busca_caractere (num_valores):
    vetor_caractere = []
    vetor_consoante = ["a", "e", "i", "o", "u"]
    for elementos in range(num_valores):
        valor = input("Insira a primeira letra: ")
        vetor_caractere.append(valor)
    for elem_fora in range(num_valores):
        for elem_dentro in range(len(vetor_consoante)):
            if vetor_caractere[elem_fora] == vetor_consoante[elem_dentro]:
                print("Um consoante encontrada:" + vetor_consoante[elem_dentro])

"""------------------------------------------------"""

""" 29- Função que """




"""------------------------------------------------"""