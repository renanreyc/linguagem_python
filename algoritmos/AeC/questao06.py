#Python
lista = []
posicoesEncotrado = []

num = int(input("Informe quantos números tem a lista: "))

for i in range(num):
    elementoLista = input(f'Digite o elemento da posição {i}: ')
    lista.append(elementoLista)

elementoAProcura = input("Informe o elemento a ser procurado: ")

#Função
def procuraNumero(elementoAProcura,lista):
    posicoesEncotrado = []
    if lista == []:
        return "Erro - Lista Vazia"
    else:
        for i in range(len(lista)):
            if lista[i] == elementoAProcura:
                posicoesEncotrado.append(i)

    return posicoesEncotrado

if procuraNumero(elementoAProcura,lista) == []:
    print(f"-1, nenhum elemento igual a {elementoAProcura} foi encontrado na lista.")
else:
    print("O elemento foi encontrado nas posições da lista:")
    print(procuraNumero(elementoAProcura,lista))

