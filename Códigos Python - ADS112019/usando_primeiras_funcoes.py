from funcoes_all import *
"""Aqui estou importando de outro script o que tiver dentro dele"""

"""Codigo Principal"""
print("Escolha a opção de calculo que você desej realizar...")
print("1- area do retangulo, 2- area do triangulo, 3- areado circulo, 4- media, 5- tabuada, "
      "6- maior, 7- menor, 8- PAR ou IMPAR, 10- calculr pagamento, 11- lista em ordem INVERSA, 12- calculo de IMC, 13- gerar boletim de LETRAS, 14- imprimir números lado a lado/abaixo, 15- imprimir intervalo personalizado, 17- gerar Série Fabonacci, 18- gerar BOLETIM em letras, 19- Efetuar compras no aplicativo, 20- criar uma AGENDA diária, 0- para sair")
opcao = "1"
while (opcao != "0"):
    opcao = input("Insira sua opção:")
    if (opcao == "1"):
        lado_1 = int(input("Insira o primeiro valor: "))
        lado_2 = int(input("Insira o primeiro valor: "))
        print("Área do retângulo: ", area_retangulo(lado_1,lado_2))

    elif (opcao == "2"):
        base = int(input("Insira o primeiro valor: "))
        altura = int(input("Insira o primeiro valor: "))
        print("Área do triângulo: ", area_triangulo(base, altura))

    elif (opcao == "3"):
        raio = int(input("Insira o primeiro valor: "))
        print("Área do círculo: ", area_circulo(raio))

    elif (opcao == "4"):
        numero_valores = 0
        while True:
            nota = int(input("Insira a nota do aluno e encerre o processo digitando -1 (MENOS 1): "))
            if (nota == -1):
                print("Operação de inserção de notas Encerrada.")
                break
            soma_valores = soma_valores + nota
            numero_valores += 1
        print("Media dos valores: ", media(soma_valores, numero_valores))

    elif (opcao == "5"):
        multiplicador = int(input("Insira o valor do multiplicador: "))
        num_comeco = int(input("Insira o valor inicial da tabuada: "))
        num_terminar = int(input("Insira o valor final da tabuada: "))
        print(tabuada(multiplicador, num_comeco, num_terminar))

    elif (opcao == "6"):
        """
        cont = 0
        limite = 0
        while (cont < 2):
            num = int(input("Insira o numero a ser analisado: "))
            maior_valor(num, limite)
            cont += 1
        print(maior_valor(num, limite))
        """
        usuario = int(input("Insira o número de valores a ser inseridos para descobrir o MAIOR: "))
        print(maior_valor1 (usuario))


    elif (opcao == "7"):
        """
        cont = 0
        minimo = 9999999999999
        while (cont < 5):
            numero = int(input("Insira o numero a ser analisado: "))
            menor_valor(numero, minimo)
            cont += 1
        print(menor_valor(numero, minimo))
        """
        usuario = int(input("Insira o número de valores a ser inseridos para descobrir o MENOR: "))
        print(menor_valor1(usuario))

    elif (opcao == "8"):
        numero_01 = int(input("Insira o valor para ver se é PAR ou IMPAR: "))
        par_ou_impar(numero_01)

    elif (opcao == "9"):
        while True:
            operacao = int(input("Escolha sua opção: 1- soma, 2- subtração, 3- multiplicação, 4- divisão ou 0 (ZERO) para sair: "))

            if (operacao == 1):
                num_1 = float(input("Insira o valor do primeiro número a ser analisado:"))
                num_2 = float(input("Insira o valor do segundo número a ser analisado:"))
                print("O resultado é: ", calculadora_adicao(num_1, num_2))
            elif (operacao == 2):
                num_1 = float(input("Insira o valor do primeiro número a ser analisado:"))
                num_2 = float(input("Insira o valor do segundo número a ser analisado:"))
                decisao_subtracao = input("Deseja realizar: primeiro - segundo? 1-sim, 2-inverter: ")
                if (decisao_subtracao == "1"):
                    print("O resultado é: ", calculadora_subtracao(num_1, num_2))
                else:
                    print("O resultado é: ", calculadora_subtracao(num_2, num_1))
            elif (operacao == 3):
                num_1 = float(input("Insira o valor do primeiro número a ser analisado:"))
                num_2 = float(input("Insira o valor do segundo número a ser analisado:"))
                print("O resultado é: ",calculadora_multiplicacao(num_1, num_2))
            elif (operacao == 4):
                num_1 = float(input("Insira o valor do primeiro número a ser analisado:"))
                num_2 = float(input("Insira o valor do segundo número a ser analisado:"))
                decisao_divisao = input("Deseja dividir: o primeiro pelo segundo? 1-sim, 2-inverter: ")
                if (decisao_divisao == "1"):
                    print("O resultado é: ",calculadora_divisao(num_1, num_2))
                else:
                    print("O resultado é: ",calculadora_divisao(num_2, num_1))
            elif (operacao == 0):
                print("Obrigado por usar nosso software.")
                break
    elif (opcao == "10"):
        qtd_horas = input("Digite a quantidade de horas: ")
        acrescimo = input("Digite o valor de acrécimo da hora extra: R$ ")
        total_salario = calcular_pagamento(qtd_horas, acrescimo)
        print("O valor dos seus rendimentos é: R$ ", total_salario)

    elif (opcao == "11"):
        tamanho = int(input("Insira o nº de elementos que deseja na lista antes de ver na ordem inversa: "))
        print(lista_inversa(tamanho))

    elif (opcao == "12"):
        peso = float(input("Insira o peso: "))
        altura = float(input("Insira a altura: "))
        print(calculo_imc(peso, altura))

    elif (opcao == "13"):
        numero_notas = int(input("Insira o número de notas para gerar o boletim: "))
        print(boletim(numero_notas))

    elif (opcao == "14"):
        tipo_impressao = int(input("Como deseja imprimir? 1- lado a lado, 2- um abaixo do outro: "))
        numero_maximo = int(input("Insira o valor limite para imprimir: "))
        imprimir_num_lado(numero_maximo, tipo_impressao)

    elif (opcao == "15"):
        primeiro_num = int(input("Insira o primeiro valor do intervalo: "))
        ultimo_num = int(input("Insira o último valor do intervalo: "))
        intervalo_personalizado(primeiro_num, ultimo_num)

    elif (opcao == "16"):
        numero_analises = int(input("Insira o número de análises que deseja fazer: "))
        print("Digite o que você precisa em questão de análise de IMC:")
        decisao = input("1- Análise de peso contando o total de cada classificação \n Análise de uma classificação isolada: (A-abaixo do peso, B-peso ideal, C-sobre peso, D-obeso, E- obeso mórbido: ").upper()
        print(calculo_imc2(numero_analises, decisao))

    elif (opcao == "17"):
        limite_sequencia = int(input("Insira o número de valores para formar a série de Fibonacci: "))
        fibonacci_usuario(limite_sequencia)

    elif(opcao == "18"):
        num_notas = int(input("Insira a quantidade de notas a ser analisadas: "))
        print(boletim(num_notas))

    elif (opcao == "19"):
        nova_compra = int(input("Digite 1 para niciar a compra: "))
        print(banco_produtos(nova_compra))

    elif (opcao == "20"):
        intervalo = int(input("Insira o valor em minutos para montar aagenda diária: "))
        agenda_diaria(intervalo)

    elif( opcao == "21"):
        caractere_natural = input("Insira o caractere que deseja ser a matriz toda: ")
        caractere_desenho = input("Insira o caractere que deseja ver formando o diamante: ")
        diamante(caractere_desenho, caractere_natural)

    elif (opcao == "22"):
        quantidade = int(input("Insira a quantidade de elementos INTEIROS que deseja na lista: "))
        ordenar_lista(quantidade)

    elif (opcao == "23"):
        quantidade = int(input("Insira a quantidade de elementos da lista que deseja contar e mostrar a lista completa: "))
        soma_lista(quantidade)

    elif (opcao == "24"):
        numero_notas = int(input("Insira a quantidade de matérias: "))
        media_lista(numero_notas)

    elif (opcao == "25"):
        num_valores = int(input("Insira o número de valores a ser analisado: "))
        busca_caractere(num_valores)


    elif (opcao == "999"):
        print("Obrigado pela preferência.")
        break

    else:
        print("Opção Inválida!")
        opcao = "1"
        print("1- area do retangulo, 2- area do triangulo, 3- areado circulo, 4- media, 5- tabuada, "
              "6- maior, 7- menor, 8- PAR ou IMPAR, 0- para sair")
        print("Insira a opção novamente.")

