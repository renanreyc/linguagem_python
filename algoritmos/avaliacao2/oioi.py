# entrada
marcas = ["A", "B", "C"]
tamanhos = [35, 36, 37, 38, 39, 40]
estoque_total = [0, 0, 0, 0, 0, 0]
quantidade = []

# processamento
for i in range(3):
    linha = []
    for j in range(6):
        quantidade = int(
            input("Informe a quantidade de sapato da marca {} e tamanho {}: ".format(marcas[i], tamanhos[j])))
        while quantidade < 0:
            print("Quantidade inválida! Informe valor válido.")
            quantidade = int(
                input("Informe a quantidade de sapato da marca {} e tamanho {}: ".format(marcas[i], tamanhos[j])))
        linha.append(quantidade)
        estoque_total[j] += linha[j]
estoque_total.append(linha)

maior = int(max(estoque_total)
numMaior = []
for i in range(len(estoque_total)):
    if
estoque_total[i] == num:
numMaior = tamanhos[i]

for i in range(3):
    print("Marca {}: ".format(marcas[i], quantidade[i]))

print("Estoque máximo: ", numMaior, "unidades[i]".format(maior))