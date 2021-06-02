#1.	(2.5) A equipe de Fórmula 1 da Ferrari deseja calcular o número mínimo de litros que deverá colocar
# no tanque de seus carros para que eles possam percorrer um determinado número de voltas até o primeiro
# reabastecimento. Desenvolva um programa que leia o comprimento da pista (em metros), o número total de
# voltas a ser percorrido em um grande prêmio, o número de reabastecimentos desejado e o consumo de
# combustível do carro em (km/litros). Calcular e escrever o número mínimo de litros necessários para
# percorrer até o primeiro reabastecimento.

#   OBS: Considere que o número de voltas entre os reabastecimentos é o mesmo.

pista = float(input("Informe o comprimento da pista em metros:\n"))
totalVoltas = int(input("Informe o número total de voltas:\n"))
numReabastecimentos = int(input("Informe o número de reabastecimentos desejado:\n"))
consumoCombstv = float(input("Informe o consumo de combustível do carro(km/litros):\n"))

while pista <= 0 or totalVoltas <=0 or numReabastecimentos <=0 or consumoCombstv <=0:
    print('\033[1;31mUm dos dados é 0 ou negativo, por favor, digite novamente os valores.\033[m\n')

    pista = float(input("Informe o comprimento da pista em metros:\n"))
    totalVoltas = int(input("Informe o número total de voltas:\n"))
    numReabastecimentos = int(input("Informe o número de reabastecimentos desejado:\n"))
    consumoCombstv = float(input("Informe o consumo de combustível do carro(km/litros):\n"))


pistaKm = pista / 1000

totalLitros = (pistaKm * totalVoltas) / consumoCombstv
print(f'\nO total de litros necessários para o circuito é de {totalLitros}L')

litrosMin = totalLitros/numReabastecimentos
print(f'\nO número mínimo de litros necessários para percorrer até o primeiro reabastecimento é {litrosMin}L')


