# Funções Prontas:
#
# len
# range
# sum
# Definindo suas próprias funções:
#
# def nome_da_função(argumento1,argumento2,...): corpo da função

# Definido uma função

# def helloWorld():
#     print("Hello World")

#------------------------------------------------------------------------------------------------
# # Definido uma função
#
# def helloWorld():
#     print("Hello World")
#
#
# # Chamada de uma função
# helloWorld()

#------------------------------------------------------------------------------------------------

# # Definido uma função
#
# def soma(num1,num2):
#     print(num1 + num2)
#
#
# # Chamada de uma função
# soma(2,3)
# soma(7,3)

#------------------------------------------------------------------------------------------------

# # Definido uma função
#
# def soma(num1,num2):
#     print(num1 + num2)
#
#
# n1 = int(input("n1: "))
# n2 = int(input("n2: "))


#------------------------------------------------------------------------------------------------
#
# # Definido uma função (ERRO)
#
# def soma(num1,num2):
#     print(num1 + num2)
#
#
# n1 = int(input("n1: "))
# n2 = int(input("n2: "))
#
# soma(n1,n2)
#
# print(soma(1,2) + soma(3,4))

#------------------------------------------------------------------------------------------------
#
# def soma(num1,num2):
#     return num1 + num2
#
# ###
#
# n1 = int(input("n1: "))
# n2 = int(input("n2: "))
# n3 = int(input("n3: "))
# n4 = int(input("n4: "))
#
# resultado = soma(n1,n2) + soma(n3,n4)
# print(resultado)

#------------------------------------------------------------------------------------------------

# Função para verificar se um número é par ou ímpar

# def classificacaoNum(num):
#     if num == 0:
#         return "Neutro"
#     elif num % 2 == 0:
#         return "par"
#     return "impar"
#
# ##############################################
#
# num = int(input("n1: "))
# while num < 0:
#     num = int(input("n1: "))
# print(classificacaoNum(num))

#------------------------------------------------------------------------------------------------

def maiorLista(lista):
    if lista == []:
        return "Lista Vazia"
    else:
        maior = lista[0]
        for i in range(len(lista)):
            if lista[i] > maior:
                maior = lista[i]
        return maior


###############################################3

l = [3, -8, 5, 800, 6]
print(maiorLista(l))

l = [3, -8, 5, 800, 60000]
print(maiorLista(l))

#------------------------------------------------------------------------------------------------

# def intersecao(l1,l2):
#     l3 = []
#
#     for i in range(len(l1)):
#         if (l1[i] in l2) and  (l1[i] not in l3):
#             l3.append(l1[i])
#     return l3
#
#
# l1 = [3, 3, 2, 1, 0, -5,4]
# l2 = [4, 345, 0, -4, 2, 56,3]
#
# print(intersecao(l1,l2))

#------------------------------------------------------------------------------------------------

# def uniao(l1, l2):
#     l3 = []
#
#     for i in range(len(l1)):
#         if l1[i] not in l3:
#             l3.append(l1[i])
#
#     for i in range(len(l2)):
#         if l2[i] not in l3:
#             l3.append(l2[i])
#
#     return l3
#
#
# l1 = [3, 2, 1, 0, -5, 4, 3]
# l2 = [4, 345, 0, -4, 2, 56, 3]
#
# print(uniao(l1, l2))
# print(uniao([], []))

#------------------------------------------------------------------------------------------------

# matriz = [[1,2,2],[2,5,6],[1,1,1]]
#
# def somaElementosDiagonalMatriz(matriz):
#     soma = 0
#     for i in range(len(matriz)):
#         for j in range(len(matriz[0])):
#             if i == j:
#                 soma += matriz[i][j]
#     return soma
#
# print("A soma dos elementos da diagonal principal é: ", somaElementosDiagonalMatriz(matriz))

#------------------------------------------------------------------------------------------------

# def ehTriangular(numero):
#     num = 1
#
#     while num * (num + 1) * (num + 2) <= numero:
#         if num * (num + 1) * (num + 2) == numero:
#             return True
#         num += 1
#     return False
#
#
# print(ehTriangular(24))
# print(ehTriangular(25))

#------------------------------------------------------------------------------------------------
#
# def matrizValida(matriz):
#     if len(matriz) == 0 or len(matriz) != len(matriz[0]):
#         return False
#     return True

#------------------------------------------------------------------------------------------------

# def matrizValida(matriz):
#     if len(matriz) == 0 or len(matriz) != len(matriz[0]):
#         return False
#     return True
#
#
# def somaElementosDiagonalMatriz(matriz):
#     if not matrizValida(matriz):
#         return "Não é possível realizar a operação"
#     else:
#         soma = 0
#         for i in range(len(matriz)):
#             for j in range(len(matriz[0])):
#                 if i == j:
#                     soma += matriz[i][j]
#         return soma
#
# matrizA = []
# print(somaElementosDiagonalMatriz(matrizA))
#
# matrizB = [[1,2,2],[2,5,6]]
# print(somaElementosDiagonalMatriz(matrizB))
#
# matrizC = [[1,2,2],[2,5,6],[1,1,1]]
# print(somaElementosDiagonalMatriz(matrizC))

#------------------------------------------------------------------------------------------------

# def mediaElementosLista(lista):
#     if lista == []:
#         return 0
#     else:
#         return sum(lista)/len(lista)
#
# l = [3,4,5,6,7]
# print(mediaElementosLista(l))

#------------------------------------------------------------------------------------------------
#
# def calculaPA(a1,razao,nTermos):
#     l = []
#     an = a1
#     for i in range(nTermos):
#         l.append(an)
#         an+= razao
#     print(l)
#     return l
#
#
# calculaPA(2,2,6)

#------------------------------------------------------------------------------------------------

# # 0! = 1
# # 1! = 1
# # 5! = 5 * 4 * 3 * 2 * 1
#
# def fatorial(num):
#     fatorial = 1
#     for i in range(num, 0, -1):
#         fatorial *= i
#
#     return fatorial
# #
#
# num = int(input())
# while num < 0:
#     num = int(input())
#
# print(fatorial(num))

#------------------------------------------------------------------------------------------------

# def e_x(x, n):
#     if n <= 0:
#         return ("Erro")
#     else:
#         somaTermos_e_x = 0
#         for i in range(n):
#             somaTermos_e_x += (x ** i) / fatorial(i)
#         return somaTermos_e_x
#
#
# print(e_x(1, -1))
# print(e_x(1, 0))
# print(e_x(-1, 10))
# print(e_x(1, 2))
# print(e_x(1, 15))

#------------------------------------------------------------------------------------------------

# #Agenda telefônica
#
#
#     print("1. Mostra Lista Telefonica")
#     print("2. Acrescentar Entrada (Nome, Número)")
#     print("3. Retirar Entrada (Nome)")
#     print("4. Procurar Número")
#     print("5. Mostra todos os nomes dos contatos")
#     print("6. Atualizar contato")
#     print("7. Terminar")





