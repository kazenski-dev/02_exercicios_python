"""MATRIZES
- São organizadas em LINHAS e COLUNAS
- o Primeiro número sempre é linha
- o segundo número sempre é coluna
"""

minha_matriz = [[1,2,3], [4,5,6], [7,8,9]]
print(minha_matriz)

for elementos in range(0,3):
    print(minha_matriz[elementos])

minha_matriz[0][0] = 200
minha_matriz[1][1] = 300
minha_matriz[2][2] = 400

for elementos in range(0,3):
    print(minha_matriz[elementos])

