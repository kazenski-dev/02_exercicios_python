#Criar um script em phyton, usando format na letra abaixo, trocando os termos específicos:

#(A gente) (tá vendo tudo), (ta vendo) a gente
#(Ta vendo), no nosso espelho, (na nossa frente)
#(Ta vendo), (na nossa frente), aberração
#(Ta vendo), ta sendo visto, querendo ou não
#(Ta vendo), (no fim do túnel), (escuridão)
#(Ta vendo), (no fim do túnel), (escuridão)

#Declaração de variáveis x índices do format
a= "A gente" #indice zero
b= "Ta vendo" #indice 1
c= "na nossa frente" # indice 2
d= "no fim do túnel" # indice 3
e= "escuridão" #indice 4

#Programa Principal com print em cada linha
print(42*"¨")
print("{0}, {1} tudo, {1} {0}".format(a,b,c,d,e))
print("{1}, no nosso espelho, {2}".format(a,b,c,d,e))
print("{1}, {2}, aberração".format(a,b,c,d,e))
print("{1}, ta sendo visto, querendo ou não".format(a,b,c,d,e))
print("{1}, {3}, {4}".format(a,b,c,d,e))
print("{1}, {3}, {4}".format(a,b,c,d,e))
print(42*"¨")

#Programa Principal com print em cada linha
print("{0}, {1} tudo, {1} {0}\n{1}, no nosso espelho, {2}\n{1}, {2}, aberração\n{1}, ta sendo visto, querendo ou não\n{1}, {3}, {4}\n{1}, {3}, {4}" .format(a,b,c,d,e))
