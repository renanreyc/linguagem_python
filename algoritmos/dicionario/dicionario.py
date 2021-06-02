# lista = [1,2,3] tupla = (1,2,3) string = "123"

# dicionario = {chave1: valor1, chave2: valor2, chave3: valor3}

# eng_sp = {'three': 'tres', 'one': 'uno', 'two': 'dos'}
# print(eng_sp)
#
#
# dic = {(0, 3): 1, (2, 1): 2, (4, 3): 3}
# print(dic)
#
# dic = {0.3: 1, 0.3: 2, 0.6: 3}
# print(dic)
#
#
# eng2sp = {}
# eng2sp['one'] = 'uno'
# eng2sp['two'] = 'dos'
# eng2sp['three'] = 'tres'
# print(eng2sp)

#----------------------------------------------------------------------

# Valores são acessados pelas chaves

# eng2sp = {'three': 'tres', 'one': 'uno', 'two': 'dos'}
# value = eng2sp['two']
# print(value)

#----------------------------------------------------------------------

# O comando del remove um par chave-valor de um dicionário
# frutas = {'kiwis': 430, 'bananas': 312, 'laranjas': 525, 'peras': 217}
# del frutas['peras']
# print(frutas)

#----------------------------------------------------------------------

# Update de valor
# frutas = {'kiwis': 430, 'bananas': 312, 'laranjas': 525, 'peras': 217}
# frutas['peras'] = 0
# print(frutas)

#----------------------------------------------------------------------

# #clear
# x = { "Joao":"a", "Maria":"b" }
# y = x
# x.clear()
# print(x,y)
#
#
# print()
#
# #copy
# x = { "Joao":"a", "Maria":"b" }
# y = x.copy()
# x.clear()
# print (x,y)

#----------------------------------------------------------------------

#items: devolve uma sequência de tuplas, onde cada tupla é um par chave-valor
#
# d = {'a':0, 'b':1, 'c':2}
# t = d.items()
# print(t)
#
# print()
#
# for key, value in d.items():
#     print(key, value)

#----------------------------------------------------------------------

# #A função dic é usada para construir dicionários e requer como parâmetros:
# #    - Uma lista de tuplas, cada uma com um par chave/conteúdo, ou
# #    - Chaves ser strings, mas são escritas sem aspas
#
#
#1
# d = dict([(1,2),('chave','conteudo')])
# print(d)
#
#
# #2
# d = dict(x=1,y=2)
# print(d)

#----------------------------------------------------------------------

# # Combinar dic e zip
#
# d = dict(zip('abc', range(3)))
# print(d)

#----------------------------------------------------------------------

# #keys - Retorna as chaves do dicionário
#
# frutas = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
#
# chaves = list(frutas.keys())
# print(chaves)
#
#
# print()
#
# for key in frutas.keys():     # the order in which we get the keys is not defined
#     print("key = ", key, " value = ", frutas[key])

#----------------------------------------------------------------------

# # #Retorna os valores do dicionário
# # frutas = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
# #
# # print(list(frutas.values()))
#
# # operador in
# frutas = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
#
# print('apples' in frutas)
# print('melon' in frutas)
#
# if 'bananas' in frutas:
#     print(frutas['bananas'])
# else:
#     print("We have no bananas")

#----------------------------------------------------------------------

# # Get - acessa o valor associado a uma chave
#
# frutas = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
#
# print(frutas.get("apples"))
# print(frutas.get("melon"))
#
# print(frutas.get("melon",0))

#----------------------------------------------------------------------

# #pop: obtém o valor correspondente à chave e remove o par chave/valor do dicionário
#
# notas = {"Pedro":[8.0], "Joao":[9.0,8.0], "Maria":[10.0]}
# print(notas.pop("Joao"))
# print(notas)

#----------------------------------------------------------------------

# #popitem: retorna e remove o último par chave/valor inserido no dicionário.
# #Em versões anteriores à 3.7, o popitem() remove um par chave/valor aleatório.
#
#
# notas = {"Joao":[9.0,8.0], "Pedro":[8.0], "Maria":[10.0]}
# print(notas.popitem())
# print(notas)
#
# print(notas.popitem())
# print(notas)

#----------------------------------------------------------------------

# #update: Atualiza um dicionário com  pares chave/valor
#
# x = {"a":1, "b":2, "c":3}
# y = {"z":9, "b":7}
# x.update(y)
# print(x)
#
# x.update(a=10,c="xxx")
# print(x)

#----------------------------------------------------------------------

# # Particularidades
#
# dic1 = {'up': 'down', 'right': 'wrong', 'true': 'false'}
# dic2 = dic1
# print(dic2 is dic1)
# dic2['right'] = 'left'
# print(dic2)
# print(dic1)
# print(dic1['right'])
#
#
# x = {"a":1, "b":2, "c":3, "a": 4}
# print(x)

#----------------------------------------------------------------------

# #Agenda telefônica
#
#
    # print("1. Mostra Lista Telefonica")
    # print("2. Acrescentar Entrada (Nome, Número)")
    # print("3. Retirar Entrada (Nome)")
    # print("4. Procurar Número")
    # print("5. Mostra todos os nomes dos contatos")
    # print("6. Atualizar contato")
    # print("7. Terminar")

