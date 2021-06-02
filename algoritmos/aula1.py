print("Hello world")
print('Hello world')

#   Os tipos básicos em Python são:
    # - int - um número inteiro
    # - float - um número em ponto flutuante ex.:5.5
    # - string - sequência de caracteres delimitados por aspas simples ou duplas

# Número completos: real + imag j. Exemplo: 2 + 3j

print(3)
print(4.9)
print(3+4j)

# ---------------------------------------------------------------------------

msg = "Hellow world"
idade = 4
altura = 1.8

print(msg)
print(idade)
print(altura)

print(type(msg))
print(type(idade))
print(type(altura))

# Algumas boas práticas de programação python:
    # começar a variável com letra minuscula;
    # as vaviáveis tem que ter nome junto, ex.: nomeAluno ou nome_aluno
    # as variáveis não pode começar com digitos ou simbolos especiais

# Na linguagem Python não é preciso declarar o tipo da variável

# ---------------------------------------------------------------------------

control = True
print(control)

control2 = False
print(control2)

# ---------------------------------------------------------------------------
# o usuário informa algo
entrada = input()
print(entrada)

entrada = input("Digite um nome:")

entrada = input("Digite um nome:")
print("O nome informado foi: ", entrada) # na virgula ele da um espaço
print("O nome informado foi: " + entrada) # na concatenação ele junta a string imediatamente com a próxima

entrada = int(input("Digite um númeroe:"))
print(entrada)

entrada = int(input("Digite um númeroe:"))
print(type(entrada))