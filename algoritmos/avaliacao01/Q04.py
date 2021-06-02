# QUESTÂO (4):
#
# """
# Faca um programa para validar o login e a senha de um usuário.
# Caso o usuário informe algum valor inválido informar e pedir novamente os dados.
# A leitura dos dados deve ser encerrada quando o usuário digitar 3 vezes um valor inválido (login ou senha).
# Considere o login válido como "kezia" e a senha como "123".
# """

cont = 0
loginValido = 0
while cont < 2:
    login = input("Digite o login:\n")
    senha = input("Digite a senha:\n")
    if login == 'kezia' and senha == '123':
        print("\033[1;32mLogin confirmado, seja bem-vindo! :)\033[m")
        cont += 3
        loginValido = 1
    else:
        print("\033[1;31mLogin inválido, tente novamente.\033[m")
        cont += 1
        loginValido = 0

if loginValido == 0:
    login = input("Digite o login:\n")
    senha = input("Digite a senha:\n")
    if login == 'kezia' and senha == '123':
        print("\033[1;31mLogin confirmado, seja bem-vindo! :)\033[m")
    else:
        print("\033[1;31mLogin inválido, sua conta foi bloqueada! :(\033[m")


