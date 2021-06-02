a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
soma = a+b
subtracao = a-b
multiplicacao = a*b
divisao = a/b
resto = a%b

resultado = ('Soma: {soma} \nSubtração: {sub} \nMultiplicação: {multi}'
      '\nDivisão: {div} \n Resto: {res}'.format(soma=soma, sub=subtracao, multi=multiplicacao,
                              div=divisao, res=resto))

print(resultado)

# x = '1'
# soma2 = int(x) + 1
# print(soma2)
