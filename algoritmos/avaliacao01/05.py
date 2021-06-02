cont = 0
while cont < 3:
    login = input("Digite o login:\n")
    senha = int(input("Digite a senha:\n"))
    if login == 'kezia' and senha == 123:
        cont += 1
    else:
        print("Valor inválido")