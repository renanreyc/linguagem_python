#tupla é imutavel

# tupla0 = "a","b","c"
# print(tupla0)
#
# tupla1 = (1,2,3)
# print(tupla1)
#
# tupla2 = ("d",1,[1,2,3])
# print(tupla2)
#
# tupla3 = tuple()
# print(tupla3)
#
# tupla4 = tuple('UEPB')
# print(tupla4)

#----------------------------------------------------------------------

# tupla1 = (1)
# print(type(tupla1))
#
# tupla = (1,)
#
#
# print(type(tupla))
# print(tupla)

#----------------------------------------------------------------------

# tupla = (1,2,3,4)
#
# print(tupla[1])
# print(tupla[1:3])

#----------------------------------------------------------------------

# tupla1[0] = 4  # tuplas são imutáveis

#----------------------------------------------------------------------

# # update de tuplas
# tupla = (1,2,3,4)
# tupla = (10,) + tupla[1:]
# print(tupla)

#----------------------------------------------------------------------

# Atribuição de tuplas

# tupla1 = (1,2,3,4)
# tupla2 = (5,6,7,8)
#
# temp = tupla1
# tupla1 = tupla2
# tupla2 = temp
#
# print(tupla1)
# print(tupla2)

#----------------------------------------------------------------------

# # Atribuição de tuplas
#
# tupla1 = (1,2,3,4)
# tupla2 = (5,6,7,8)
#
# tupla1, tupla2 = tupla2,tupla1
#
#
# print(tupla1)
# print(tupla2)

#----------------------------------------------------------------------

# #Tuplas como valores de retorno
#
# t = divmod(10, 3)
# print(t)
#
# divisor, modulo = divmod(5, 3)
# print(divisor)
# print(modulo)

#----------------------------------------------------------------------

# #Tuplas como valores de retorno

# def min_max(t):
#     return min(t), max(t)
#
# t = (10,2,3,-8,6)
# print(min_max(t))
#
# t = ("f","z","c","b")
# print(min_max(t))
#
# t = ("a","z","bgtf")
# print(min_max(t))

#----------------------------------------------------------------------
#
# # Tuplas e listas
#
# # zip é uma função integrada que recebe duas ou mais sequências e devolve uma lista de tuplas
# # onde cada tupla contém um elemento de cada sequência
#
# s = 'abcm'
# t = [0, 1, 2]
#
# for pair in zip(s, t):
#     print(pair)

#----------------------------------------------------------------------

# l1 = list(zip('ABC', 'DEF'))
# print(l1)
#
# l2 = list(zip('MARIA', 'joao'))
# print(l2)

#----------------------------------------------------------------------

# # Itera sobre uma sequência de pares; cada par contém um índice (começando de 0) e
# # um elemento da sequência dada
#
# for index, element in enumerate('abc'):
#     print(index, element)

#----------------------------------------------------------------------

# #criar lista
# l2 = list(range(1,7))
# print(l2)
#
# # criar listas com tuplas
# l1 = ["a","b","c"]
# lista1 = list(enumerate(l1))
# print(lista1)

#----------------------------------------------------------------------

# listaMenu = ["Cadastrar","Atualizar", "Remover"]
# for index, element in enumerate(listaMenu):
#     print(index+1, element)

#----------------------------------------------------------------------

# Mais operações

tupla = (10,20,30,40)

del tupla

#print(tupla)

tupla = (10,20,30,40,10)

print ("len:", len(tupla))
print("count: ", tupla.count(10))
print("index: ", tupla.index(20))
print("in: ", 40 in tupla)
print ("max:", max(tupla))
print ("min:", min(tupla))

#----------------------------------------------------------------------


