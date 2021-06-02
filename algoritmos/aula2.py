a  = 1
b = 2
c = 3.0
d = 4.0

soma = a + b
print("soma:", soma)

soma1 = c + d
print("soma1:", soma1)

soma2 = a + d
print("soma2:", soma2)
#Faz a coesão; transforma o número inteiro em um número flutuante

#------------------------------------------------------------

diferença = a - b
print("diferença:", diferença)

diferença1 = c - d
print("diferença1:", diferença1)

diferença2 = a - d
print("diferença2:", diferença2)

#------------------------------------------------------------

mult = a * b
print("mult:", mult)

mult1 = c * d
print("mult1:", mult1)

mult2 = a * d
print("mult2:", mult2)

#------------------------------------------------------------

div = a / b
print("div:", div)

div1 = c / d
print("div1:", div1)

div2 = a / d
print("div2:", div2)
#Sempre na divisão o valor é dado como número flutuante

#-------------------------------------------------------------

a = 7
b = 2

q = a//b
print("q:", q)
#pega o valor inteiro

resto = a % b
print("resti", resto)
#pega o resto da divisão

#--------------------------------------------------------------

potencia = a ** b
print("protencia", potencia)
#potência do número

#--------------------------------------------------------------

#5. FAÇA UM PROGRAMA QUE PEÇA O RAIO DE UM CÍRCULO, CALCULE E MOSTRE SUA ÁREA.

pi = 3.14
raio = float(input("informe o raio: "))

area = pi * raio ** 2
print(area)

v1 = 3 ** 1/2
v2 = 3 ** (1/2)

print("v1:", v1)
print("v2:", v2)

#--------------------------------------------------------------
#Faça a conversão de temperatura C = (5 * (F - 32) / 9)

farenheit = float(input("informe a temperatura: "))

celsius = (5 * (farenheit-32) / 9)

print(celsius)

#A loja mamão está vendendo seus produtos em 5 prestações sem juros. Fça um algoritmo que receba um valor de uma compra e mostre o valor das prestações;
valorCompra = float(input("valor da conta: "))

valorPrestacao = valorCompra / 5

print(valorPrestacao)

#--------------------------------------------------------------

quantParcelas = 10

valorCompra = float(input("valor da conta: ")  valorPrestacao = valorCompra / quantParcelas)

print(valorPrestacao)


