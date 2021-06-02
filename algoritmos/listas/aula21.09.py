# cont = 0
# while True:
#     nome = input()
#     senha = input()
#     if nome == "kezia" and senha == "123":
#         print("Login válido")
#         break   #o break sai do laço
#     else:
#         cont += 1
#         print("Inválido")
#         if cont == 3:
#             print("Esgotou as possibilidades")
#             break


#-----------------------------------------------------

nome = input()
senha = input()

cont = 1

while cont < 3 and (nome != "kezia" or senha !="123"):
    print("erro")
    nome = input()
    senha = input()
    cont += 1

if nome == "kezia" and senha == "123":
    print("Login valido")
else: print("Esgotou as possibilidades")

#-----------------------------------------------------