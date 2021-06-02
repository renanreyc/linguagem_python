#1. (5.0) Escreva um programa em Python para converter um número binário em um
# hexadecimal. O programa deve receber uma lista (cada posição representa um bit) e
# produzir como saída uma lista para cada símbolo do número convertido na base
# hexadecimal. Além disso deve ser feita a verificação se o número pode ser
# representado, considere uma representação com 2 bytes.
# OBS:

#Não utilizar soluções com strings, while True, funções prontas e todas as
#possibilidades possíveis.

listaBinario = [[0,0,0,0],[0,0,0,1],[0,0,1,0],[0,0,1,1],[0,1,0,0],[0,1,0,1],[0,1,1,0],[0,1,1,1],[1,0,0,0],[1,0,0,1],[1,0,1,0],[1,0,1,1],[1,1,0,0],[1,1,0,1],[1,1,1,0],[1,1,1,1]]
listaHexadecimal = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]

numHexadecimal = []
numBinario = []

dadosValidados = False

while dadosValidados == False:
    digitos = int(input("Informe quantos dígitos tem o número binário: "))

    if digitos > 16 or digitos < 0:
        print("Não é possível representar o binário em hexadecimal, por favor, informe um número positivo com no máximo 16 dígitos.\n")
        dadosValidados = False

    else:
        for i in range(digitos):
            num = int(input("Informe o número binário bit a bit da esquerda à esquerda\n")

            if num != 1 or num != 0:
                print("Esse número não é válido.")
            else:
                numBinario.append((num))


print(numBinario)

# Completa com zero, se necessário. Deve ter um total de 16 bits:

numBinario.reverse()
for i in range(16-len(numBinario)):
    numBinario.append(0)

print(numBinario)
numBinario.reverse()

# Laço transformando de binário para hexadecimal

for i in range(0,16,4):
    for j in range(16):
        if numBinario[i:i+4] == listaBinario[j]:
            numHexadecimal.append(listaHexadecimal[j])

print("numero binario: ",numBinario)
print("numero hexadecimal: ",numHexadecimal)




