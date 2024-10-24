
# importamos o módulo sys para visualizarmos o tipo da exceção

import sys

item = 0         # testar também com 22 e 'Bóson'

try:
    divisao = 1/item
    print("Valor:", item) 
    print("1 dividido por", item, "é", divisao)
except:
    print("Ocorreu a exceção", sys.exc_info()[0])
    print()
