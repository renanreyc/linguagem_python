# QUESTÂO (2):

# """
# Desenvolver um programa em Python para calcular a conta de água para a CAGEPA.
# O custo da água varia dependendo se o consumidor é residencial,
# comercial ou industrial. A regra para calcular a conta é:
# – Residencial: R$50,00 de taxa mais R$0,05 por m³ gastos;
# – Comercial: R$500,00 para os primeiros 80 m³ gastos mais R$0,25 por m³ gastos acima dos 80 m³;
# – Industrial: R$800,00 para os primeiros 100 m³ gastos mais R$0,04 por m³ gastos acima dos 100 m³;
# O programa deverá ler o número da conta do cliente,
# consumo de água por metros cúbicos e o tipo de consumidor (residencial, comercial e industrial).
# Como resultado, imprima o número da conta do cliente e o valor real a ser pago pelo mesmo.
# """

taxaResidencial = 0.05
taxaComercial = 0.25
taxaIndustrial = 0.04

conta = int(input('Digite o seu número de conta:\n'))
consumo = float(input("Digite o seu consumo de água(m³):\n"))
tipo = int(input('Digite o seu tipo de consumo: [1-residencial, 2-comercial, 3-industrial]\n'))
valor = 0

while conta <= 0 or consumo <=0 or tipo <=0:
    print('\033[1;31mUm dos valores é 0 ou negativo, por favor, digite novamente os valores\033[m\n')

    conta = int(input('Digite o seu número de conta:\n'))
    consumo = float(input("Digite o seu consumo de água(m³):\n"))
    tipo = int(input('Digite o seu tipo de consumo: [1-residencial, 2-comercial, 3-industrial]\n'))
    valor = 0

while tipo > 3:
    print('\033[1;31mO tipo de conta é consumo é inválido, por favor, digite novamente o valor:\033[m\n')

    tipo = int(input('Digite o seu tipo de consumo: [1-residencial, 2-comercial, 3-industrial]\n'))

if tipo == 1 or tipo == 2 or tipo == 3:
    if tipo == 1:
        valor = 50 + consumo * taxaResidencial

    elif tipo == 2:
        if consumo <= 80:
            valor = 500
        else:
            valor = 500 + (consumo - 80) * taxaComercial
    elif tipo == 3:
        if consumo <= 100:
            valor = 800
        else:
            valor = 800 + (consumo - 100) * taxaIndustrial
    print(f'\033[1;32mNúmero da conta do cliente:\033[m {conta}\n\033[1;32mValor a ser pago:\033[m R${valor}')





