# 14.	Escreva um programa em Python para corrigir uma prova com 10 questões
# de múltipla escolha (a, b, c, d ou e), em uma turma com 15 alunos. Cada questão
# vale 1 ponto. Leia o gabarito apenas uma vez, e para cada aluno leia sua
# matricula (número inteiro) e suas respostas. Calcule e escreva para cada aluno:
# sua matrícula, suas respostas, e sua nota. OBS: utilizar matrizes na solução.

# matrizAlunos = []
# gabarito = ["a", "b", "a","b","a","b","a","b","a","b"]
#
# for i in range(2): #15, para todos os 15 alunos
#     linha = []
#     contrespostasCertas = 0
#     matricula = int(input())
#     linha.append(matricula)
#     for i in range(10):
#         resposta = input("Resposta questão " + str(i+1))
#         linha.append(resposta)
#         if resposta == gabarito[i]:
#             contrespostasCertas += 1
#     linha.append(contrespostasCertas)
#     matrizAlunos.append(linha)
#
# print("g = ", gabarito)
# for i in range(len(matrizAlunos)):
#     print(matrizAlunos[i])


# 15.	Um produtor agrícola lhe contratou para desenvolver um sistema de
# controle de grãos produzidos em três regiões; Sul, Sudeste e Centro-Oeste.
# A ideia da solução consistem em inserir a quantidade de grãos produzidos
# por cada região nos anos de 2017 e 2018 e ao final o programa deve gerar
# uma nova matriz com previsão de produção para o ano de 2019. A previsão é
# calculada a partir da porcentagem de crescimento para cada tipo de grão,
# que se mantém fixa a cada ano. A seguir é apresentado um exemplo de tabelas
# com os dados fornecidos pelo produtor.

# Ano de 2017	Produção de Grãos (miT)
# 	            Soja	Feijão	Arroz	Milho
# Sudeste	    100	    200	    300	    400
# Centro-Oeste	2700	450	    600	    1000
# Sul	        600	    400	    550	    450
#
# Ano de 2018	Produção de Grãos (miT)
# 	            Soja	Feijão	Arroz	Milho
# Sudeste	    130	    230	    600	    500
# Centro-Oeste	3000	500	    700	    1200
# Sul	        800	    450	    700	    600

# Ano de 2019	Previsão da Produção de Grãos (miT)
# 	        Soja	Feijão	Arroz	Milho
# Sudeste	169     264,5   1200    625
#           (30%)   (15%)	(100%) 	(25%)
# Centro-Oeste
# Sul

# ano_2017 = [[100,200,300,400],[2700,450,600,1200],[600,400,550,450]]
#
# ano_2018 = [[130,230,600,500],[3000,500,700,1200],[500,200,200,100]]
#
# ano_2019 = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#
# #ano_2017 = []
# # for i in range(3):
# #     linha = []
# #     for j in range(4):
# #         linha.append(int(input("Informe a quantidade de grãos")))
# #     ano_2017.append(linha)
#
# for i in range(len(ano_2017)):
#     for j in range(len(ano_2017[0])):
#         porcentagem = (ano_2018[i][j] - ano_2017[i][j])/ano_2017[i][j]
#         ano_2019[i][j] = (1+ porcentagem) * ano_2018[i][j]
#
#     for i in range(len(ano_2019)):
#         print(ano_2019[i])

#Matriz secundaria
#     | a11 a12 a13 |
# A = | a21 a22 a23 |
#     | a31 a32 a33 | 3 x 3
#
#     soma = a02 + a11 + a20
#     if (i + j) == len(A) - 1
#
# #Abaixo daMatriz principal
# abaixo = a21 + a31 + a32 # o i é maior que o j



