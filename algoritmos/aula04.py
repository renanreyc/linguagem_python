# for i in range(5):
#     print("kezia")

# for i in range(5):
#     num = int(input("Num:"))
#     print(num)

#for i in range(inicio, fim, i/d):
    #i/d é o incremento

# for i in range(0,10,):
#     print(i)
# for i in range(11):
#     print(i)

# for i in range(10,0,-1):
#     print(i)

# for i in range(1,50,2):
#     print(i)
# ##or    a de baixo eu executo 2x mais para executar
# for i in range(1,50):
#     if i%2 != 0:
#         print(i)

#01. Escreva um programa que efetua a leitura de 20 valores números e
# apresente no final o total do somatório e a média dos valores lidos.

# soma = 0
#
# for i in range(3):
#     num = int(input("num:"))
#     soma = soma + num
#
# media = soma/3
#
# print(soma)
# print(media)

#04. Fazer um programa para ler o sexo de dez pessoas e mostrar a quantidade
# de pessoa de cada sexo, separadamente.

contMasculino = 0
contFeminino = 0
# contMasculino = contFeminino = 0

for i in range(10):
    sexo = input("sexo: ")

    if sexo == "m":
        contMasculino += 1

    elif sexo == "f":
        contFeminino += 1

    else:
        print("sexo invalido")

print(contMasculino)
print(contFeminino)