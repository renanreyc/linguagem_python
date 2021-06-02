listaBinario = [[0,0,0,0],[0,0,0,1],[0,0,1,0],[0,0,1,1],[0,1,0,0],[0,1,0,1],[0,1,1,0],[0,1,1,1],[1,0,0,0],[1,0,0,1],[1,0,1,0],[1,0,1,1],[1,1,0,0],[1,1,0,1],[1,1,1,0],[1,1,1,1]]
listaHexadecimal = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]

numBinario = []
numHexadecimal = []

dadosValidados = False
cont = 0

while dadosValidados == False:
    digitos = int(input("Informe quantos dígitos tem o número binário: \n"))

    if digitos > 16 or digitos < 0:
        print("Não é possível representar o binário em hexadecimal, por favor, informe um número positivo com no máximo 16 dígitos.\n")
        dadosValidados = False

    elif digitos == 0:
        dadosValidados = True

    else:
        print("Digite o número binário bit a bit da direita para esquerda.")
        while cont < digitos:
            bit = int(input(f"bit {cont + 1}:"))
            if bit != 0 and bit != 1:
                print("Esse número não é binário, por favor, digite novamente.")
                cont += 0
            else:
                numBinario.append(bit)
                cont += 1
                dadosValidados = True

# Completa com zero, se necessário. Deve ter um total de 16 bits:

for i in range(16-len(numBinario)):
    numBinario.append(0)

numBinario.reverse()

# Laço transformando de binário para hexadecimal

for i in range(0,16,4):
    for j in range(16):
        if numBinario[i:i+4] == listaBinario[j]:
            numHexadecimal.append(listaHexadecimal[j])

print("\nnúmero binário:",numBinario)
print("número hexadecimal:",numHexadecimal)
