# matriz = [[1,2,3],[4,5,6],[7,8,9]]

# print(matriz) #visualização desconfortavel
# for i in range(len(matriz)): #visualização confortavel
#     print(matriz[i])

#-------------------------------------------
#inicialliar matriz com elementos zero

#inicializar lista vazia

# lista = []
# for i in range(3):
#     lista.append(0)
#
# print("Lista: ", lista)
#
# lista1 = [0] + [0] + [0] # ou [0]*3
# print("Lista1: ", lista1)
#
# # Inicializar matriz
#
# matriz = []
# for i in range(4):
#     matriz.append([0]*3)
# print("Matriz: ", matriz)

#-------------------------------------------
# Inicializar matriz com elementos zero e as dimensões
# informadas pelo usuário

# n = int(input('Digite a dimensão n da matriz: '))
# m = int(input('Digite a dimensão m da matriz: '))
#
# matriz = []
#
# for i in range(n):
#     matriz.append([0]*m)
# print(matriz)

#-------------------------------------------
# Exemplo 1: inicializar uma matriz com elementos informados pelo usuário

# matriz = []
# for i in range(2):
#     linha = []
#     for j in range(2):
#         linha.append(int(input('Informe o numero: ')))
#     matriz.append(linha)
# print(matriz)

# Exemplo 2: inicializar matriz com elementos informados pelo usuário

# matriz = []
# for i in range(2):
#     linha = []
#     for j in range(2):
#             linha.append(int(input('Digite a nota [' + str(i) + ',' + str(j) + ']:')))
#     matriz.append(linha)
# print(matriz)

# Exemplo 3: inicializar matriz com elementos informados pelo usuário

# matriz = []
# for i in range(3):
#     linha = []
#     linha.append(input("Nome: "))
#     linha.append(int(input("idade: ")))
#     matriz.append(linha)
# print(matriz)

#-------------------------------------------
# Conta a quantidade de números pares em uma matriz
# matriz = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# contPares = 0
#
# for i in range(len(matriz)):
#     for j in range(len(matriz[0])):
#         if matriz[i][j] % 2 == 0:
#             contPares += 1
#
# print(contPares)

#-------------------------------------------
#Calcula a média aritmetica dos elementos de uma matriz
# matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# soma = 0
#
# for i in range(len(matriz)):
#     for j in range(len(matriz[0])):
#         soma += matriz[i][j]
#
# quantElementos = len(matriz) * len(matriz[0])
# media = soma/quantElementos
#
# print(media)


#Informa a quantidade de numeros anima da média dos elementos

# cont = 0
#
# for i in range(len(matriz)):
#     for j in range(len(matriz[0])):
#         if matriz[i][j] > media:
#             cont+= 1
#
# print(cont)

#-------------------------------------------
# Menor elemento de uma matriz

# matriz = [[1,2],[1,-9]]
# menor = matriz[0][0]
#
# for i in range(len(matriz)):
#     for j in range(len(matriz[0])):
#         if matriz[i][j] < menor:
#             menor = matriz[i][j]
#
# print("menor ", menor)

#-------------------------------------------
# Verifica se um elemento pertence a uma matriz

matriz = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

elementoAprocurar = int(input("Informe o valor: "))

achou = False
i = 0

while (not achou) and (i < len(matriz)):
    if elementoAprocurar in matriz[i]:
        print("Achei o elemento")
        achou = True
    i += 1
    
#a negação de falso é verdade
if not achou:
    print("Não achei o elemento")