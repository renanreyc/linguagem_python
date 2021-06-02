#Python
lista = []

num = int(input("Informe quantos números tem a lista: "))

for i in range(num):
    numLista = int(input(f'Digite o número inteiro na posição {i+1}: '))
    lista.append(numLista)

#Função
def numeroImpar(lista):
    numerosPrimos = 0
    for i in range(len(lista)):
        if lista[i] % 2 != 0:
            numerosPrimos += 1

    return numerosPrimos

if numeroImpar(lista) == 0:
    print("-1, nenhum número impar encontrado.")
else:
    print("A quantidade de números impar encontrados foi de:",numeroImpar(lista))

