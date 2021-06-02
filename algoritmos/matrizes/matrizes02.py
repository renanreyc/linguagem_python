# A = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#
# B = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

#B = [[1,2,3,4],[5,6,7,8]]

#B = [[1,2,3,4],[5,6,88,8],[9,10,11,12]]

# diferente = False
#
# if (len(A) != len(B)) or (len(A[0]) != len(B[0])):
#     diferente = True
# else:
#     for i in range(len(A)):
#         for j in range(len(A[0])):
#             if A[i][j] != A[i][j]:
#                 diferente = True
#
# if diferente:
#     print("São matrizes diferentes")
# else:
#     print("São matrizes iguais")

#-----------------------------------------------------------
# A = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#
# B = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#
# #B = [[1,2,3,4],[5,6,7,8]]
#
# if (len(A) != len(B)) or (len(A[0]) != len(B[0])):
#     print("A operação não pode ser realizada. Dimensões incompatíveis.")
#
# else:
#     # Inicializa a matriz C
#     C = []
#     for i in range(len(A)): #vai criar a estrutura da matriz com zeros
#         C.append([0]*len(A[0]))
#
#     for i in range(len(A)): #vai atribuir a soma para a matriz C
#         for j in range(len(A[0])):
#             C[i][j] = A[i][j] + B[i][j]
#
#     print(C)

# -----------------------------------------------------------
# Multiplicação por escalar

# A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
#
# B = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
#
# escalar = int(input("Informe o valor do escalar:"))
#
# for i in range(len(A)):
#     for j in range(4):
#         B[i][j] = A[i][j] * escalar
# print(B)

# -----------------------------------------------------------
# A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
#
# B = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
#
# #B = [[1, 2, 3, 4], [5, 6, 7, 8]
#
# if (len(A) != len(B)) or (len(A[0]) != len(B[0])):
#     print("A operação não pode ser realizada. Dimensões incompatíveis.")
#
# else:
#     #Inicializa a matriz C
#     C = []
#     for i in range(len(A)):
#         C.append([0]*len(A[0]))
#
#     for i in range(len(A)):
#         for j in range (len(A[0])):
#             C[i][j] = A[i][j] + (-1)*B[i][j]
#     print(C)

# -----------------------------------------------------------
#Calcula a matriz transposta

# matrizA = [[1, 2, -5], [3, 0, -3], [5, 7, -6]]
#
# # Cria a matriz transposta
# matrizTranspostaA = []
# for i in range(len(matrizA[0])):
#     matrizTranspostaA.append([0] * len(matrizA))
#
# for i in range(len(matrizTranspostaA)):
#     for j in range(len(matrizTranspostaA[0])):
#         matrizTranspostaA[i][j] = matrizA[j][i]
#
# for i in range(len(matrizTranspostaA)):
#     print(matrizTranspostaA[i])

# -----------------------------------------------------------
# Multiplicação de Matrizes

matrizA = [[3,1],[2,-1],[0,4]]
matrizB = [[1,-1,2],[3,0,5]]


linhasA = len(matrizA)
colunasA = len(matrizA[0])
linhasB = len(matrizB)
colunasB = len(matrizB[0])

# A quantidade de colunas de A deve ser igual a quantidade de linhas de B
if colunasA != linhasB:
    print("Não é possível realizar a operação de multiplicação")

else:
    matrizAB = []
    for i in range(linhasA):
        matrizAB.append([])
        for j in range(colunasB):
            somatorio = 0
            for k in range(linhasB):
                    somatorio += matrizA[i][k]*matrizB[k][j]
            matrizAB[i].append(somatorio)
print(matrizAB)