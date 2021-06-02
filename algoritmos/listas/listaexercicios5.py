#1.	Faça um Programa que leia 5 números inteiros, armazene-os em uma lista.

# lista = []
#
# for i in range(5):
#     num = int(input("Número: "))
#     lista.append(num)
#
# print(lista)

# 2.	Faça um Programa que leia 10 números reais e mostre-os na ordem inversa.

# lista2 = []
#
# for i in range(10):
#     num = int(input("Número: "))
#     lista2.append(num)
#
# lista2.reverse()
# print(lista2)

# 3.	Faça um Programa que leia 40 notas, mostre as notas e a média na tela.
# lista3 = []
#
# for i in range(40):
#     num = int(input("Nota: "))
#     lista3.append(num)

# 4. 4.	Faça um Programa que leia 20 números inteiros e armazene-os numa lista.
# Armazene os números pares na lista PAR e os números IMPARES na lista impar. Imprima as três listas.

# lista = []
# listaPar = []
# listaImpar = []
#
# for i in range(20):
#     num = int(input(f'Número {i+1}: '))
#     lista.append(num)
#     if num % 2 == 0:
#         listaPar.append(num)
#     else:
#         listaImpar.append(num)
#
# print(f'lista: {lista}')
# print(f'listaPar: {listaPar}')
# print(f'listaImpar: {listaImpar}')

#5.	Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.
# lista=[]
# alunoMedia = 0
# for a in range(10):
#     notaTotal = 0
#     print(f'Notas do aluno {a+1}')
#     for i in range(4):
#         nota = float(input(f'nota {i+1}: '))
#         notaTotal = notaTotal + nota
#     notaMedia = notaTotal/4
#     lista.append(notaMedia)
#     if notaMedia >= 7:
#         alunoMedia += 1
# print(f'Medias de cada alunos: {lista}')
# print(f'{alunoMedia} alunos ficaram na média')

#outra maneira
# lista=[]
# alunoMedia = 0
# for a in range(10):
#     notaTotal = 0
#     print(f'Notas do aluno {a+1}')
#     for i in range(4):
#         nota = float(input(f'nota {i+1}: '))
#         notaTotal = notaTotal + nota
#     notaMedia = notaTotal/4
#     lista.append(notaMedia)
#
# for i in range(10):
#     if notaMedia[i] >= 7:
#         alunoMedia += 1

# 7.	Faça um Programa que peça a idade e a altura de 10 pessoas, armazene cada informação na sua respectiva lista.
# Imprima a idade da pessoa que possui maior altura.
# maiorIdade = 0
# for i in range(2):
#     lista = []
#     idade = float(input(f'Idade da pessoa {i+1}: '))
#     altura = float(input(f'Altura da pessoa {i+1}: '))
#     lista.append(idade)
#     lista.append(altura)
#     print(f'Lista {i+1}: {lista}')
#     if altura > maiorAltura:
#         pessoaMaisAlta = maiorAltura
#         pessoa = i

#8.	Faça um Programa que leia uma lista A com 10 números inteiros, calcule e mostre a soma dos quadrados
# dos elementos do vetor.

# listaA = [1,2,3,4,5,6,7,8,9,10]
# b = 0
# for i in listaA:
#     a = (listaA[i-1])**2
#     b += a
# print(b)

#9.	Faça um Programa que leia duas listas com 10 elementos cada. Gere uma terceira lista de 20 elementos, cujos valores
# deverão ser compostos pelos elementos intercalados das duas outras listas.

# l_intercalada = []
#
# for i in range(10):
#     l.append(int(input("num na lista l: ")))
#
# for i in range(10):
#     li.append(int(input("num na lista li: ")))
#
# for i in range(len(l)):
#     l_intercalada.append(l[i])
#     l_intercalada.append(l1[i])
#
# print(l_intercalada)


#10.	Altere o programa anterior, intercalando 3 listas de 10 elementos cada.

# l_intercalada = []
#
# for i in range(10):
#     l.append(int(input("num na lista l: ")))
#
# for i in range(10):
#     l1.append(int(input("num na lista l1: ")))
#
# for i in range(10):
#     l2.append(int(input("num na lista l2: ")))
#
# for i in range(len(l)):
#     l_intercalada.append(l[i])
#     l_intercalada.append(l1[i])
#     l_intercalada.append(l2[i])
#
# print(l_intercalada)


# 11.	Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de
# 13 anos possuem altura inferior à média de altura desses alunos.

# 12.	Escreva um algoritmo que permita a leitura dos nomes de 10 pessoas  e armazene os nomes lidos em uma lista.
# Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de pessoa e depois escrever a mensagem ACHEI,
# se o nome estiver entre os 10 nomes lidos anteriormente (guardados na lista), ou NÃO ACHEI caso contrário.

# lista = []
# for i in range(3):
#     nome = input(f'Nome da pessoa {i + 1}: ')
#     lista.append(nome)
# print(lista)
# nomeAProcurar = input(f'Nome à procura: ')
#
# i = 0
#
# while nomeAProcurar in lista:
#     if nomeAProcurar == lista[i]:
#         a = 1
#     i += 1
#
# if a == 1:
#     print('ACHEI')
# else:
#     print('NÃO ACHEI')


# 16.	Escreva um programa em Python para encontrar o segundo maior elemento
# de uma lista com 20 números inteiros.

# OBS: todos os valores informados serão de valores diferentes e a solução
# não deve fazer este tratamento das entradas. Além disso, a solução não
# deve modificar a lista original com a ordem fornecida dos números.

# primeira maneira (errado pois altera a lista original
# l = [-1,0,89,-5,56,4]
# l.sort()
# print(l)
# print("Maior: ",l[-2]) /ou ~
# print("Maior ",l[len(l)-2]) /ou/

#segunda maneira
# l=[]
# for i in range(20):
#     l.append(input("Informe o numero: "))

# l1 = l.copy() # l1 = l[:]
# l1.sort()
# print(l1)
# print(l)
# print("Maior: ",l1[-2])

# 17.	Escreva um programa em Python para converter um número inteiro
# em binário de acordo com a representação de grandeza com sinal
# (sinal e magnitude). O programa deve receber um número inteiro e
# produzir como saída uma lista com os bits do número convertido (um bit
# para cada posição da lista). Além disso deve ser feita a verificação se
# o número pode ser representado, considere uma representação com 8 bits
# (um para o sinal e 7 para a magnitude).

num = int(input("Informe o número: "))
numBinario = []

if num > 127 or num < -127:
    print("Não é possível representar")

else:
    #Analisa o sinal
    if num < 0:
        sinal = 1
        num = num * (-1) #Converte para positivo - facilitar condição do while

    else: sinal = 0

    #Calcula a magnitude
    while num > 0:
        resto = num % 2
        numBinario.append(resto)
        num = num // 2

    # Completa com zero, se necessário. Deve ter um total de 7 bits (maginitude)
    for i in range(7-len(numBinario)):
        numBinario.append(0)

    # Completa com zero, se necessário. Deve ter um total de 7 bits (magnitude)
    for i in range(7-len(numBinario)):
        numbinario.append(0)

    numBinario.append(sinal) #adiciona o sinal

    #Inverter o número
    numBinario.reverse()

print(numBinario)





