#Python
num = int(input("Informe um número inteiro: "))
while num < 0:
    num = int(input("Número inválido. Digite um número maior ou igual a 0: "))

#Função
def fatorial(num):
    fatorial = 1
    for i in range(num, 0, -1):
        fatorial *= i

    return fatorial

print(f"\nO valor do fatorial de {num} é:",fatorial(num))
