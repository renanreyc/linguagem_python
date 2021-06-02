#19.    Desenvolva um gerador de tabuada, capaz de gerar a tabuada
# de qualquer número inteiro entre 1 a 10. O usuário deve informar
# de qual número ele deseja ver a tabuada. A saída deve ser conforme
# o exemplo abaixo:

# num = int(input("numero: "))
#
# for j in range(1,num+1): #(1,2,3,4)
#     for i in range(1,11): #(1...10)
#         print(j,"x",i,"=",j*i)
#     print("-------------------")

# =====================================================================

# 13. Faça um programa para:

# a) Ler um valor x qualquer
# b) Calcular Y = (x+1)+(x+2)+(x+3)+(x+4)+(x+5)+...(x+100).

# x = float(input("Digite o valor de X: "))
# y = 0
#
# for i in range(1,101):
#     y += (x + i)
#
# print(y)

# =====================================================================

#12. Sendo H = 1/1 + 1/2 + 1/3 + 1/4 + ... + 1/N. Faça um programa para
# gerar e mostrar o número H. O número N será fornecido como entrada:

# n = int(input("informe n: "))
# h = 0
#
# for i in range(1, n+1):
#     h += 1/i
#
# print(h)

# =====================================================================

# 14. 1000/1 + 997/2 + 944/3 + ... Para 50 termos

# serie = 0
# numerador = 1000
#
# for i in range(1,51):
#     serie += numerador/i
#     numerador = numerador - 3
#
# print(serie)

# =====================================================================

# 16. x^1/1 - x^3/3 + x^5/5 - ...
arctan = 0
x = float(input())
expoente = 1
sinal = 1


for i in range(50):
    arctan += sinal * (x**expoente/expoente)
    expoente += 2
    sinal = sinal * -1
