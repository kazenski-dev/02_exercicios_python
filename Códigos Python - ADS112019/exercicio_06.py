#Formatação de saída:
dia="15"
mes="08"
ano="2019"

print("Hoje é dia "+ dia + "/" + mes + "/"+ ano) #o sinal de + concatena os elementos
print("Hoje é dia ", dia , "/" , mes , "/", ano) #a vírgula coloca um espaço a mais entre cada elemento
print(dia, mes, ano) #imprime os elementos com um espaçamento

#segue o padrão brasileiro
print("\nPadrão usando o format")
print("Hoje é dia {0}/{1}/{2}".format(dia,mes,ano)) #o format identifica que entre chaves vão os valores do format

#segue o padrão americano
print("\nPadrão brasileiro")
print("Hoje é dia {1}/{0}/{2}".format(dia,mes,ano)) #o format identifica que entre chaves vão os valores do format

#segue o padrão para programação e arquivamento
print("\nPadrão americano")
print("Hoje é dia {2}/{1}/{0}".format(dia,mes,ano)) #o format identifica que entre chaves vão os valores do format

#Então o formato que usarei é o imput fixo e alterando os valores somente entre chaves.
#print("Hoje é dia {0}/{1}/{2}".format(dia,mes,ano))
