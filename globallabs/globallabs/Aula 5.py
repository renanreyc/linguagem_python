lista = [12, 10, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']
lista_animal [0] = 'macaco'

tupla =  (1, 10, 12, 14)
print (len(tupla))
print (len(lista_animal))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list (tupla)
print(type(lista_numerica))
lista_numerica [0] = 100
print(lista_numerica)

# print(lista_animal[1])
# nova_lista = lista_animal * 3
# print (nova_lista)


# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)
# lista_animal.reverse()
# print(lista_animal)


# if 'lobo' in lista_animal:
#     print('existe um lobo na lista')
# else:
#     print('não existe o animal na lista')
#     lista_animal.append('lobo')
#     print(lista_animal)

# lista_animal.pop(0)
# print(lista_animal)

# lista_animal.remove('elefante')
# print(lista_animal)

# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print (soma)
#ou
# print(sum(lista))