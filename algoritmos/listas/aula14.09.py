# 04.Remover todas as ocorrências de um número informado
# pelo usuário. Considere a lista pronta


# lista = [1,2,1,4,1,7]
# numAProcurar = int(input("Informe o numero: "))
#
# i = 0
#
# while numAProcurar in lista:
#     if numAProcurar == lista[i]:
#         lista[i:i+1] = []
#     i += 1
#
# print(lista)

# 05. Realizar a interseção das duas listas abaixo e a
# mesma não apresentar números repetidos.

# l1 = [3, 2, 1, 3, 0, -5, 4, 3]
# l2 = [4, 345, 0, -4, 2, 56, 3]
#
# intersecao = []
# i = 0
#
# for elemento in l1:
#     if (elemento in l2) and (elemento not in intersecao):
#         intersecao[i:i] = [elemento]
#         i+= 1
# print(intersecao)

#01.Inserir 5 nomes informados pelo usuario em uma lista

# lista = [] #sempre começar com uma lista vazia
#
# for i in range(5):
#     nome = input("nome: ")
#     lista[i:i] = nome
# print(lista)

# 02. Considere a lista l = [1,2,3,4,5,6,7]. Realizar operações
# com a mesma lista para a saida ser l = [4,5,6,7,1,2,3]
# l = [1,2,3,4,5,6,7]
# l = l[3:] + l[:3]
#
# print(l)

#03 Encontrar o maior elemento de uma lista
# l = [3,2,1,3,0,-5,4,3]
# # #l = [-2,-7,-8]
#
# maior = l[0]
#
# for i in range(len(l)):
#     if l[i] > maior:
#         maior = l[i]
# print(maior)


