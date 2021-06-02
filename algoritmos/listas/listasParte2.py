#lista[inicio:fim:passo]

# lista = [1,2,3,4,5,6]
# print(lista[:-1:2])
# print(lista[5:0:-1])
# print(lista[::-1])
#
# lista2 = [10,11,12,13,14]
# del lista2[0] #vc esta mudando a lista original
# print(lista2)

#-----------------------------------------------------
# lista = [1,2,3,4,5]
# print(max(lista))
# print(min(lista))
#
# lista1 = ["a","f","z","b"]
# print(max(lista1))
# print(min(lista1))
#
# lista2 = [1,1,1,1]
# print(max(lista2))
# print(min(lista2))
#
# lista3 = ["a","ab","ze","z"]
# print(max(lista3))
# print(min(lista3))

#-----------------------------------------------------
# lista1 = [1,2,3]
# lista2 = [1,2,3]
#
# if lista1 ==lista2:
#     print("são iguais")
# else:
#     print("nao")
#
# lista1 = [1,2,3]
# lista2 = [2,1,3]
#
# if lista1 == lista2:
#     print("são iguais")
# else:
#     print("nao")

#-----------------------------------------------------

# lista1 = [1,2,3]
# lista2 = lista1
#
# lista1[0] = 10
# print(lista1)
# print(lista2)
#
# lista3 = lista1[:]
#
# lista1[0] = 12
#
# print(lista1)
# print(lista3)
#
# print(lista2 is lista1)
# print(lista3 is lista1)

#-----------------------------------------------------
# objeto.metodo(args)
#adiciona um elemento na lista
# lista = []
# lista.append(2)
#
# print(lista)
#
# lista.append(4)
# print(lista)

#-----------------------------------------------------
#junta duas listas
# lista1 = [1,2,3]
# lista2 = [4,5,6]
#
# lista1.extend(lista2)
# print(lista1)

#-----------------------------------------------------

# lista = [1,3,4]
# lista.insert(1,2) #inserir na posição 1 o elemento 2;
# print(lista)
#
# lista.insert(10,20)
# print(lista)

#-----------------------------------------------------

# lista = [1,2,3,2]
# lista.remove(2)
# print(lista)

#-----------------------------------------------------
#apaga a lista de acordo com a posição do elemento
# lista = [1,2,3]
# lista.pop(0)
# print(lista)
#
# lista.pop()
# print(lista)

#-----------------------------------------------------
#limpa toda a lista
# lista = [1,2,3]
# lista.clear()
# print(lista)

#-----------------------------------------------------
# conta quantos elementos tem na lista
# lista = [1,2,1,3,4]
# print(lista.count(1))

#-----------------------------------------------------
#mostra a posição (indice) onde está o elemento "1"
#~mostra a primeira ocorrencia do elemento
# lista = [1,2,1,3,4]
# print(lista.index(1))

#-----------------------------------------------------
# deixa a lista na ordem inversa
# lista = [2,5,2,7]
# lista.reverse()
# print(lista)

#-----------------------------------------------------
# metodo pronto que copia a lista
# lista1 = [1,2,3]
# lista2 = lista1.copy()
#
# print(lista2)
# print(lista2 is lista1)

#-----------------------------------------------------
#ordenação da lista de maneira crescente
#sort(key=None, reverse=False)

# lista = [1,6,-3,0,34,-9]
# lista.sort()
# print(lista)
#
# lista1 = ["abc","de","a"]
# lista1.sort()
# print(lista1)
#
# lista = [1,6,-3,0,34,-9]
# lista.sort(reverse=True)
# print(lista)
#
# lista1 = ["abc","de","a"]
# lista1.sort(key=len)
# print(lista1)