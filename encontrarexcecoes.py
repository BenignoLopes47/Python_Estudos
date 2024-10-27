
# importamos o módulo sys para visualizarmos o tipo da exceção

import sys

item = 0         

try:
    divisao = 1/item
    print("Valor:", item) 
    print("1 dividido por", item, "é", divisao)
except:
    print("Ocorreu a exceção", sys.exc_info()[0])
    print()



item = 'python'         # testar com 'python'

try:
    divisao = 1/item
    print("Valor:", item) 
    print("1 dividido por", item, "é", divisao)
except:
    print("Ocorreu a exceção", sys.exc_info()[0])
    print()


item = 22         # testar também com 22 

try:
    divisao = 1/item
    print("Valor:", item) 
    print("1 dividido por", item, "é", divisao)
except:
    print("Ocorreu a exceção", sys.exc_info()[0])
    print()



#Organizado por tipo

import sys
item =  0  # testar tb com 22 e 'python'
try:
    print("Valor:", item)
    divisao = 1/item
    print("1 dividido por", item, "é", divisao)
except (TypeError):
    # Manipular tipo incorreto
    print("Você deve digitar apenas números!")
    print()
except (ZeroDivisionError):
    # Manipular divisão por zero
    print("Não é possível dividir por zero.")
    print()
except:
    # Manipular outras exceções não conhecidas
    print("Ocorreu a exceção", sys.exc_info()[0])
