#Python
texto = str(input("Digite um texto: "))

#Função
def polindromo(texto):
    textoAlto = texto.strip().upper()
    palavras = textoAlto.split()
    junto = ''.join(palavras)
    inverso = junto[::-1]
    print(f"O inverso de {junto} é {inverso}")
    if inverso == junto:
        print("True! O texto digitado é um políndromo.")
    else:
        print("False! O texto digitado NÃO é um políndromo.")

    return junto

polindromo(texto)