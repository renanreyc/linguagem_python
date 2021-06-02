#Python
num = str(input("Digite um número binário(use apenas 1 ou 0): "))

#Função
def converteEmDecimal(num):
    soma = 0
    pot = 0  #potencia

    for i in range(len(num), 0, -1):
        soma = soma + ((int(num[i-1]) * (2 ** pot)))
        pot = pot + 1
    return soma

print(converteEmDecimal(num))
