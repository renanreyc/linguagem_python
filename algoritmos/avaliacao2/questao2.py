# 2. (5.0) Uma loja vende sapatos femininos de três marcas: A, B e C e tamanhos de 35 a
# 40. O gerente da loja lhe solicitou um programa para manipular dados referentes ao
# estoque desta loja. Desta forma, você deve ler para cada marca de sapato e
# numeração a sua respectiva quantidade e informar a numeração que possui a maior
# quantidade em estoque. A seguir é apresentado um exemplo de tabela com os dados
# do estoque.

quantidadeA = []
quantidadeB = []
quantidadeC = []
matriz = []

somaMaior = 0

    #Entrada dos valores na matriz
for i in range(6):
    marcaA = int(input(f'Entre com a quantidade de sapatos tamanho {35 + i} da marca A: '))
    quantidadeA.append(marcaA)
    marcaB = int(input(f'Entre com a quantidade de sapatos tamanho {35 + i} da marca B: '))
    quantidadeB.append(marcaB)
    marcaC = int(input(f'Entre com a quantidade de sapatos tamanho {35 + i} da marca C: '))
    quantidadeC.append(marcaC)

matriz.append(quantidadeA)
matriz.append(quantidadeB)
matriz.append(quantidadeC)

    #Busca da numeração com mair estoque
for l in range(len(matriz[0])):
    soma = 0
    for m in range(len(matriz)):
        soma += matriz[m][l]

    if soma > somaMaior:
        somaMaior = soma
        numeracaoMaiorEstoque = 35 + l
        estoqueIgual = False

    elif soma == somaMaior:
        numeracaoMaiorEstoqueA = numeracaoMaiorEstoque
        numeracaoMaiorEstoqueB = 35 + l
        estoqueIgual = True

    #print da matriz de marcas e tamanhos e print do mairo número em estoque
for i in range(len(matriz)):
     print(matriz[i])
print('\n'+'-='*30)
if estoqueIgual == True:
    print(f'\nNúmerações com maior número em estoque: {numeracaoMaiorEstoqueA} e {numeracaoMaiorEstoqueB} ({somaMaior} unidades cada)')
else:
    print(f'\nNúmeraçao com maior número em estoque: {numeracaoMaiorEstoque} ({somaMaior} unidades)')
