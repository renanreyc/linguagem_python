# QUESTÂO (3):
#
# """
# Escreva um programa que imprima os N termos de uma Progressão Aritmética,
# conforme fórmula a seguir. O usuário deverá fornecer o valor de:
# n (número de termos), r (razão) e a1 (primeiro termo da série).
#
# a1 = a1
# a2 = a1 + r
# a3 = a2 + r
# a4 = a3 + r
# an = a1 + + (n-1).r
#
# """

termos = int(input("Digite o número de termos:\n"))
razao = int(input("Digite a razão:\n"))
a1 = int(input("Digite o primeiro termo da série:\n"))
a = 0
razaoZero = 0
if termos == 0:
    print('Nenhum termo foi inserido na PA')

else:
    for i in range(termos):
        a += a1 + razaoZero
        razaoZero = razao
        aux = a
        a1 = aux
        print(f'a{i+1} = {a}')
        a = 0