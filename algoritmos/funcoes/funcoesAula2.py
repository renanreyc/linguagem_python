# Um exemplo clássico de recursão é a definição do fatorial de um número natural n:
#
# n! = n(n − 1)(n − 2). . . 1
#
# Ex: 4! = 4 * 3 * 2 * 1
#
# podemos também definir n! de forma recursiva

# def fatorial(num):
#     if num == 0:
#         return 1
#     return num * fatorial(num -1)
#
# num = int(input())
# print(fatorial(num))

#------------------------------------------------------------------------------------------------

# def fib(i):
#     if i == 1:
#         return 0
#     elif i == 2:
#         return 1
#     return fib(i - 1) + fib(i - 2)
#
#
# for i in range(1, 11):
#     print(fib(i), end=" ")

#------------------------------------------------------------------------------------------------

# def infinitamenteRecursiva(num):
#     if (num == 10):
#         return True
#     return infinitamenteRecursiva(num)
#
#
# print(infinitamenteRecursiva(10))
# print(infinitamenteRecursiva(11))

#------------------------------------------------------------------------------------------------

# # Variáveis Globais e Locais
# # a variavel local tem prioridade em relação a variavel global
# variavel = 5
#
# def funcao( ) :
#     global variavelglobal
#     variavel = 7
#     return variavel
#
# print ( "Retorno função : " , funcao() )
# print ( "Valor da variável global: " , variavel)

#------------------------------------------------------------------------------------------------

# Variáveis Globais e Locais


# def somaNumeros(n1,n2):
#     global soma
#     soma = n1 + n2
#     return soma
#
# soma = 0
# print("Soma antes: ", soma)
#
# somaNumeros(1,2)
# print("Soma depois: ", soma)

#------------------------------------------------------------------------------------------------

# # Variáveis Globais e Locais
# def somaC():
#     return soma + 2
#
#
# print(somaC())

#------------------------------------------------------------------------------------------------

# # Parâmetros com valores default
# # Realiza login no sistema.
#
# def login(msg1, msg2, tentativas=3, aviso='Informe novamente!'):
#     while tentativas != 0:
#         login = input(msg1)
#         senha = input(msg2)
#
#         if login == 'kezia' and senha == "123":
#             return "Login feito com sucesso"
#
#         tentativas = tentativas - 1
#
#         if tentativas < 1:
#             return "Tentativas esgotadas"
#
#         print(aviso)
#
#
# # login("Informe login ", "Informe a senha ")
# # login("Informe login ","Informe a senha ",2)
# # login("Informe login ","Informe a senha ",2,"Informe outra vez")

#------------------------------------------------------------------------------------------------

# O comando pass não faz nada, passa o corpo da função sem quebrar.

# def function(a):
#     pass
#
# function(0)

#------------------------------------------------------------------------------------------------

# #Funções com número arbitrário de argumentos de entrada
#
# def concat(*args, sep="/"):
#     return sep.join(args)
#
# print(concat("a","b"))
# print(concat("e","f","g"))
# print(concat("e","f","g","h"))
# # print(concat("e","f","g",9))

#------------------------------------------------------------------------------------------------

# print(list(range(3, 6)))
#
# args = [3, 6]
# print(list(range(*args)))
#
# args = [3]
# print(list(range(*args)))
#
# args = [8, 6]
# print(list(range(*args)))
#
# args = [0, 11,2]
# print(list(range(*args)))
#
# args = [0, 11,2,1]
# # print(list(range(*args)))
# # A função range só tem 3 argumetos, inicio fim e o incremento
#------------------------------------------------------------------------------------------------

# Valores default são avaliados apenas uma vez.
# Isso faz diferença quando o valor default é um objeto mutável como uma lista ou dicionário

# def adicionaElementoLista(elemento, lista=[]):
#     lista.append(elemento)
#     return lista
#
# print(adicionaElementoLista(1))
# print(adicionaElementoLista(2))
# print(adicionaElementoLista(3))

#------------------------------------------------------------------------------------------------
#
# #Se você não quiser que o valor default seja compartilhado entre chamadas subsequentes,
# #pode reescrever a função assim:
#
# def adicionaElementoLista(elemento, lista=None):
#     if lista is None:
#         lista = []
#     lista.append(elemento)
#     return lista
# print(adicionaElementoLista(1))
# print(adicionaElementoLista(2))
# print(adicionaElementoLista(3))

#------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------------