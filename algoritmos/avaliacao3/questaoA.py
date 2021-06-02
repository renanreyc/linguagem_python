# 18g25m1s 21g 1g50s 49s 46g59m

angulos = [x for x in input("Digite o ângulo em graus(g), minutos(m) e segundos(s): ").split()]

print(angulos)

g = minu = True
lista_graus = []
lista_min = []
lista_seg = []
dic_angulos = {}



def valores(angulos):
    for i in angulos:
        if 'g' in i:  # [18, 25m1s]
            grau = i.split('g')
            lista_graus.append(int(grau[0]))
            g = True
        else:
            lista_graus.append(0)
            g = False

        if 'm' in i and g == True:
            minuto = i.split('m')
            lista_min.append(int(minuto[0].split('g')[1]))
            minu = True
        elif 'm' in i and g == False:
            minuto = i.split('m')
            lista_min.append(int(minuto[0]))
            minu = True
        else:
            lista_min.append(0)
            minu = False

        if 's' in i and minu:
            segundo = i.split('s')
            lista_seg.append(int(segundo[0].split('m')[-1]))
        elif 's' in i and grau:
            segundo = i.split('s')
            lista_seg.append(int(segundo[0].split('g')[-1]))
        elif 's' in i:
            segundo = i.split('s')
            lista_seg.append(int(segundo[0]))
        else:
            lista_seg.append(0)


valores(angulos)


def dicionario(angulos, lista_graus, lista_min, lista_seg):
    c = 0
    for i in angulos:
        dic_angulos[i] = (lista_graus[c], lista_min[c], lista_seg[c])
        c += 1



dicionario(angulos, lista_graus, lista_min, lista_seg)


def imprimir(dic_angulos, angulos):
    print(dic_angulos)
    print()

    for i in angulos:
        print(' ' * (25 - len(i)), i)

    print('+ ___')


imprimir(dic_angulos, angulos)


def calculos(lista_graus, lista_min, lista_seg):
    soma_graus = sum(lista_graus)
    media_graus = soma_graus // len(lista_graus)
    resto_graus = (soma_graus % len(lista_graus)) * 60

    soma_minutos = sum(lista_min)
    media_min = (soma_minutos + resto_graus) // len(lista_min)
    resto_min = ((soma_minutos + resto_graus) % len(lista_min)) * 60

    soma_seg = sum(lista_seg)
    media_seg = ((soma_seg + resto_min) // len(lista_seg)) + ((soma_seg + resto_min) % len(lista_seg))

    if soma_seg >= 60:
        soma_minutos += soma_seg // 60
        soma_seg = soma_seg % 60

    if soma_minutos >= 60:
        soma_graus += soma_minutos // 60
        soma_minutos = soma_minutos % 60

    if media_seg >= 60:
        media_min += media_seg // 60
        media_seg = media_seg % 60

    if media_min >= 60:
        media_graus += media_min // 60
        media_min = media_min % 60
    print('                  {}g{}m{}s\n'.format(soma_graus, soma_minutos, soma_seg))
    print('          Media: {}g{}m{:.1f}s'.format(media_graus, media_min, media_seg))


calculos(lista_graus, lista_min, lista_seg)