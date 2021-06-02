# listas

# [1,2,3]
# [1.0,2.0,4.0]
# ["a","b","c"]
# [1,1.0,"a"]
# []
# [1,[2,4]]

# pode ser armazenado em váriaveis e apresentado em prints

# lista1 = [1,2,3]
# lista2 = [1.0,2.0,4.0]
# lista3 = ["a","b","c"]
# lista4 = [1,1.0,"a"]
# lista5 = []
# lista6 = [1,[2,4]]
#
# print(lista1)
# print(lista2)
# print(lista3)
# print(lista4)
# print(lista5)
# print(lista6)

#função len apresenta quantos elementos tem na lista

# lista1 = [1,2,3]
# print(len(lista1))
#
# lista6 = [1,[2,4]]
# print(len(lista6))

#pegar o elementro dentro da lista

# numeros_inteiros = [10,20,30,40,50]
# print(numeros_inteiros[0])
# print(numeros_inteiros[5-3])
# print(numeros_inteiros[len(numeros_inteiros)-1])

#for junto com a listas

# numeros_inteiros = [10,20,30,40,50]
#
# for i in range(len(numeros_inteiros)):
#     print(numeros_inteiros[i])

# for numero in numeros_inteiros:
#     print(numero) #rescrever for

#while junto com as listas

# meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
# n = 1
#
# while(n < 4):
#     mes = int(input("Escolha um mês (1-12): "))
#     if 1 <= mes < 13:
#         print('O mês é', meses[mes-1])
#     else:
#         print('Mês inválido')
#         n += 1

#Indices negativos
# meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
#
# print(meses[-1])
# print(meses[-12])

#in e notin para saber se o termo tem na sequencia
# nomes = ["maria", "jose", "joao"]
#
# nomeAprocurar = input("Informe o nome:")
#
# if nomeAprocurar in nomes:
#     print("Achei")
# else:
#     print("Não achei")
#
# numeros = [10, 20, 30]
#
# numerosAprocurar = input("Informe o numero:")
#
# if numerosAprocurar not in numeros
#     print("Achei")
# else:
#     print("Não achei")


#operação com as listas
# lista1 = [1,2,3]
# lista2 = [4,5,6]
# lista3 = lista1 + lista2
# print(lista3)
#
# lista4 = lista1 * 3
# print(lista4)
#
# lista5 = [0]*5
# print(lista5)

#fatias de uma lista
# lista = [2,3,4,5,6]
# print(lista[0:2]) #até a posição 2(-1)
#
# print(lista[2:4])
# print(lista[:3])
# print(lista[1:])
# print(lista[:])

# fatias com numeros negativos
# lista = [2,3,4,5,6]
#
# print(lista[-2:-4]) #errado, começa pelo numero menro
# print(lista[-4:-2])

#Modificara um elemento da lista
# lista = [2,3,4,5,6]
# lista[1] = 1
# print(lista)
#
# lista = ["a","b", "c", "d", "e", "f"]
# lista[1:3] = ["x", "y"]
# print(lista)

# atribuição vazia
# lista = ["a", "b", "c", "d", "e", "f"]
# lista[1:3] = []
# print(lista)

# Acrescentar novos elementos
lista = ["a", "d", "f"]
lista[1:1] = ["b","c"]
print(lista)
lista[4:4] = ["e"]
print(lista)


