# str1 = 'Hello World!'
# print(str1)
#
# str2 = "Hello World!"
# print(str2)
# str3 = '''Hello World!'''
# print(str3)
#
# str4 = """Hello World!"""
# print(str4)
#
# str5 = '''Esta é uma string multi-line. Esta é a primeira linha.
# Esta é a segunda linha.
#     "Esta é a terceira linha"
# '''
# print(str5)

#----------------------------------------------------------

# str1 = 'Hello World!'
# str2 = "Python Programming"
#
# print("str1[0]: ", str1[0])
# print("var2[1:5]", str2[1:5])
#
# print ("str1[:5] :",str1[:5])
# print ("str1[:] :", str1[:])

#----------------------------------------------------------

# var1 = 'Hello World!'
# var2 = "Python Programming"
#
# print(var1 + var2)
# print(var1*5)

#----------------------------------------------------------

#var1 = 'Hello World!'
#var2 = "Python Programming"
#
#print ("e" in var1)
#print ("ython" in var2)
#print ("h" not in var1)
#print ("H" not in var1)

#----------------------------------------------------------

# %s - string     %d- inteiro    %f - float

# print ("My name is %s and weight is %i kg!" % ('''Zara''', 21))
#
# print ("My name is %s and weight is %f kg!" % ('Zara', 21))
#
# print ("My name is %s and weight is %.2f kg!" % ('Zara', 21))

#----------------------------------------------------------

# var1 = 'What's your name?' #erro


# var2 = "What's your name?"
# var3 = 'What\'s your name?'
#
# print(var2)
# print(var3)
#
# var4 = "Essa é a primeira linha\nEssa é a segunda linha"
# print(var4)
#
# var5 = "Essa é a primeira linha\tEssa ainda é a mesma linha" #pra dar um tab
# print(var5)

#----------------------------------------------------------

# #Strings são imutáveis
#
# msg = "Ola, mundo!"
# msg[0] = 'B'            # ERROR!
# print(msg)

#----------------------------------------------------------

# l = [4,50,-1,89.0]
# print("Max l: ", max(l))
# print("Min l: ", min(l))

# l = [4,50,-1,89,"a",-0.9] # não vai conseguir realizar essa comparação pq tem números e letras
# print(max(l))
# print(min(l))


# str1 = 'examE' # diferencia maiusculo e minusculo
# print("Max suffix: ", max(str1))
# print("Min suffix: ", min(str1))

#----------------------------------------------------------

# string = "nOme"
#
# # Retorna uma string com todas as letras maiúsculas
# print("string.upper(): ", string.upper())

#----------------------------------------------------------

# string = "nOme"
#
# # Retorna uma string com todas as letras em minúsculas
# print("string.lower() ", string.lower())

#----------------------------------------------------------
#
# string = "nOme"
#
# # Retorna um string com o primeiro caractere em maiúscula, e o resto em minúsculas
# print("string.capitalize(): ", string.capitalize())

#----------------------------------------------------------

# string = "  nome "
#
# #Retorna um string removendo caracteres em branco do início e do fim
#
# print("string.strip():", string.strip())
# print(len(string)) #verificar a quantidade de caracteres
# print(len(string.strip()))

#----------------------------------------------------------

# string = "  nome "
#
# #Retorna um string removendo caracteres em branco do início
#
# print("string.lstrip():", string.lstrip())
# print(len(string))
# print(len(string.lstrip()))
# print(len(string))

#----------------------------------------------------------

# string = "  nome "
#
# #Retorna um string removendo caracteres em branco do fim
#
# print("string.rstrip():", string.rstrip())
# print(len(string))
# print(len(string.rstrip()))

#----------------------------------------------------------

# string = "  nome "
#
# #Retorna o número de ocorrências de item
#
# print("string.count(item):", string.count(" "))

#----------------------------------------------------------

# #Substitui todas as ocorrências do substring old por new
#
# string = "nome  nome"
# print("string.replace(old, new):", string.replace("nome","Nome"))
#
#
# print("string.replace(old, new):", string.replace("Nome","NOME"))

#----------------------------------------------------------

# #Retorna um string centrado em um campo de tamanho largura
# string = "maria"
# print("string.center(largura):", "*"+string.center(25)+"*")

#----------------------------------------------------------
#
# #Retorna um string justificado à esquerda em um campo de tamanho largura
# string = "maria"
# print("string.ljust(largura):", "*"+string.ljust(25)+"*")

#----------------------------------------------------------

# #Retorna um string justificado à direita em um campo de tamanho largura
# string = "maria"
# print("string.rjust(largura):", "*"+string.rjust(25)+"*")

#----------------------------------------------------------

# # Retorna o índice mais à esquerda onde o substring item é encontrado
# string = "maria"
# print("string.find(item):", string.find("a"))
# print("string.find(item):", string.find("u")) #-1 se n for encontrado

#----------------------------------------------------------

# # Retorna o índice mais à direita onde o substring item é encontrado
# string = "maria"
# print("string.rfind(item):", string.rfind("a"))
# print("string.rfind(item):", string.rfind("p"))

#----------------------------------------------------------

# #Como find, mas causa um erro em tempo de execução caso item não seja encontrado
#
# string = "maria"
# print("string.index(item):", string.index("a"))
#
# print("string.index(item):", string.index("b")) #o programa vai quebrar por causa do programa n existir

#----------------------------------------------------------

# #Como rfind, mas causa um erro em tempo de execução caso item não seja encontrado
# string = "maria"
# print("string.rindex(item):", string.rindex("a"))
# print("string.rindex(item):", string.rindex("c"))

#----------------------------------------------------------
#
# string = "This is a text"
#
# # Coloca a letra inicial de cada palavra como maiúscula
# print(string.title())

#----------------------------------------------------------

# string = "This is a text"
#
# # Coloca as letras maiúscula como minúsculas e vice-versa
# print(string.swapcase())

#----------------------------------------------------------

# string = "This is a text"
#
# # Coloca as letras maiúscula como minúsculas e vice-versa
# print(string.swapcase())

#----------------------------------------------------------

# Verifica se a string dada é totalmente maiúscula.

# string = "oi"
# print("1 -", string.isupper())
#
# string = "OI"
# print("2 -",string.isupper())
#
# string = " "
# print("3 -",string.isupper()) # retorna "False" para espacos em branco
#
# string = "333"
# print("4 -",string.isupper()) # só dígitos e símbolos retorna False
#
# string = "OI 333"
# print("5 -",string.isupper()) # retorna True se a string tiver dígitos e símbolos e todas as letras forem maiúsculas.

#----------------------------------------------------------

# Verifica se a string dada é totalmente minúscula.

# string = "oi"
# print("1 -", string.islower())
#
# string = "OI"
# print("2 -",string.islower())
#
# string = " "
# print("3 -",string.islower()) # retorna "False" para espacos em branco
#
# string = "333"
# print("4 -",string.islower()) # só dígitos e símbolos retorna False
#
# string = " oi 33"
# print("5 -",string.islower()) # retorna True se a string tiver dígitos e símbolos e todas as letras forem minúsculas.

#----------------------------------------------------------

# Verifica se todas as palavras com a primeira letra são maiúscula.

# string = "This is a text"
# print(string.istitle())
#
# string = "This Is A Text 333"
# print(string.istitle())
#
# string = "333"
# print(string.istitle())

#----------------------------------------------------------

# Verifica se a string é alfa-numérica, ou seja, contém apenas letras e números, sem caracteres especiais

# string = "This"
# print(string.isalnum())
#
# string = "333"
# print(string.isalnum())
#
# string = "This11"
# print(string.isalnum())
#
# string = "This is a text"
# print(string.isalnum())
#
# string = "This &Is* A Text 333"
# print(string.isalnum())

#----------------------------------------------------------

# Verifica se a string só contém letras

# string = "This"
# print(string.isalpha())
#
# string = "This is a text"
# print(string.isalpha())
#
# string = "This &Is* A Text 333"
# print(string.isalpha())
#
# string = "333"
# print(string.isalpha())

#----------------------------------------------------------

# Verifica se a string só contém dígitos
#
#string = "333"
#print(string.isdigit())

#string = "This &Is* A Text 333"
#print(string.isdigit())

#----------------------------------------------------------

# Verifica se a string contém apenas espaços

# print('   '.isspace())
# print('z   '.isspace())

#----------------------------------------------------------

# string = "This is a text"
#
# # Separa uma string
# print("1 -", string.split())
# print("2 -", string.split("a"))
# print("3 -",string.split("is"))

#----------------------------------------------------------

# Retorna uma string na qual os elementos da sequencia de caracteres foram unidos por um separador.


# seq = ["a", "b", "c"] # sequência de strings.
# s = "-"
# print (s.join( seq ))
#
#
# string = "This is a text"
# print('other'.join(string.split('a'))) # string.split('a') = ["This is ", "  text"]

#----------------------------------------------------------

# Verifica se uma string termina com uma dada sentença

# string = 'this is string example....wow!!!'
# suffix = '!!'
# print (string.endswith(suffix))
# print (string.endswith(suffix,20))
#
# suffix = 'exam'
# print (string.endswith(suffix))
# print (string.endswith(suffix,0,19)) #delimitador de inicio e fim da string

#----------------------------------------------------------

# Verifica se uma string começa com uma dada sentença

# string = "this is string example....wow!!!"
#
# print (string.startswith( 'this' ))
# print (string.startswith( 'This' ))
# print (string.startswith( 'string', 8 ))
# print (string.startswith( 'this', 2, 4 )) #delimitador de inicio e fim
# print (string.startswith( 'this', 0, 5 ))

#----------------------------------------------------------

# txt1 = "My name is {name}, I'am {age}".format(name = "John", age = 36)
# print(txt1)
#
# txt2 = "My name is {0}, I'am {1}".format("John",36)
# print(txt2)
#
# txt3 = "My name is {}, I'am {}".format("John",36)
# print(txt3)
#
# txt4 = '{:.2f}'.format(3.141592653589793)
# print(txt4)

#----------------------------------------------------------
