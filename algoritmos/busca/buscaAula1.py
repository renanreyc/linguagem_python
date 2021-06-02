# Busca Sequencial
# OBS:  toda a sequência precisa ser varrida quando x não está presente em seq.

def busca_sequencial(seq, x):
    for i in range(len(seq)):
        if seq[i] == x:
                return True
                #Quando ele entra no return ele já sai da função
    return False

'''seq do tipo lista'''
#print(busca_sequencial( [1,4,2,77,-9,0,3] , -9))
#print(busca_sequencial( [1,4,2,77,-9,0,3] , 30))


'''seq do tipo tupla'''
#print(busca_sequencial( ((1,2,3)) , 1))
#print(busca_sequencial( ((1,2,3)) , 10))



'''seq do tipo string'''
#print(busca_sequencial("ahbdbdvfyhvfhvfh" , "v"))
#print(busca_sequencial("vcgdsgvwsdfwtdf", "!"))
#print(busca_sequencial("vcgdsgvwsdfwtdf", 1))

#------------------------------------------------------------------------------------------------

# # Busca Binária Iterativa
#
# def pesquisa_binaria(seq, item):
#
#     inicio, fim = 0, len(seq) - 1
#
#     while inicio <= fim:
#         meio = (inicio + fim) // 2 #divide e pega a parte inteira
#         if seq[meio] == item:
#             return True
#         elif seq[meio] > item:
#             fim = meio - 1
#         else: #seq[meio] < item
#             inicio = meio + 1
#     return False
#
# print(pesquisa_binaria([10,21,32,43,54,65],32))
# print(pesquisa_binaria([10,21,32,43,54,65],54))
# print(pesquisa_binaria([10,21,32,43,54,65],65))
# print(pesquisa_binaria([10,21,32,43,54,65],7))

#------------------------------------------------------------------------------------------------

# Busca Binária Recursiva

def busca_binaria(seq, inicio, fim, item):
    if fim < inicio:
        return False

    meio = (inicio + fim) // 2

    if seq[meio] == item:
        return True
    elif item > seq[meio]:
        return busca_binaria(seq, meio + 1, fim, item)
    else:
        return busca_binaria(seq, inicio, meio - 1, item)


print(busca_binaria([10, 21, 32, 43, 54, 65], 0, 5, 32))
print(busca_binaria([10, 21, 32, 43, 54, 65], 0, 5, 54))
print(busca_binaria([10, 21, 32, 43, 54, 65], 0, 5, 65))
print(busca_binaria([10, 21, 32, 43, 54, 65], 0, 5, 7))

#------------------------------------------------------------------------------------------------

import timeit

print(timeit.timeit("busca_sequencial([10,21,32,43,54,65,67,68,69,70,76,77,89,90],10)", setup="from __main__ import busca_sequencial"))
print(timeit.timeit("busca_sequencial([10,21,32,43,54,65,67,68,69,70,76,77,89,90],67)", setup="from __main__ import busca_sequencial"))
print(timeit.timeit("busca_sequencial([10,21,32,43,54,65,67,68,69,70,76,77,89,90],32)", setup="from __main__ import busca_sequencial"))
print(timeit.timeit("busca_sequencial([10,21,32,43,54,65,67,68,69,70,76,77,89,90],90)", setup="from __main__ import busca_sequencial"))
print(timeit.timeit("busca_sequencial([10,21,32,43,54,65,67,68,69,70,76,77,89,90],900)", setup="from __main__ import busca_sequencial"))

#------------------------------------------------------------------------------------------------

# import timeit
#
# print(timeit.timeit("busca_binaria([10,21,32,43,54,65,67,68,69,70,76,77,89,90],0,13,10)", setup="from __main__ import busca_binaria"))
# print(timeit.timeit("busca_binaria([10,21,32,43,54,65,67,68,69,70,76,77,89,90],0,13,67)", setup="from __main__ import busca_binaria"))
# print(timeit.timeit("busca_binaria([10,21,32,43,54,65,67,68,69,70,76,77,89,90],0,13,32)", setup="from __main__ import busca_binaria"))
# print(timeit.timeit("busca_binaria([10,21,32,43,54,65,67,68,69,70,76,77,89,90],0,13,90)", setup="from __main__ import busca_binaria"))
# print(timeit.timeit("busca_binaria([10,21,32,43,54,65,67,68,69,70,76,77,89,90],0,13,900)", setup="from __main__ import busca_binaria"))
#


#------------------------------------------------------------------------------------------------

# print(timeit.timeit("pesquisa_binaria([10,21,32,43,54,65,67,68,69,70,76,77,89,90],10)", setup="from __main__ import pesquisa_binaria"))
# print(timeit.timeit("pesquisa_binaria([10,21,32,43,54,65,67,68,69,70,76,77,89,90],67)", setup="from __main__ import pesquisa_binaria"))
# print(timeit.timeit("pesquisa_binaria([10,21,32,43,54,65,67,68,69,70,76,77,89,90],32)", setup="from __main__ import pesquisa_binaria"))
# print(timeit.timeit("pesquisa_binaria([10,21,32,43,54,65,67,68,69,70,76,77,89,90],90)", setup="from __main__ import pesquisa_binaria"))
# print(timeit.timeit("pesquisa_binaria([10,21,32,43,54,65,67,68,69,70,76,77,89,90],900)", setup="from __main__ import pesquisa_binaria"))
#
#
