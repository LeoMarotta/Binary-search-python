import math
import random
from re import M

lista = []

#criando lista aleatória

for x in range(99):
    lista.append(math.ceil(10*random.random()))

print("A lista não ordenada:", lista)

#definindo insertion sort

def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = chave

insertion_sort(lista)

print("A lista ordenada:", lista)

#definindo a busca

def binary_search(lista, item, begin=0, end=None):
    #arrumando a chamada da função da busca binária
    if end is None:
        end = len(lista)-1
    if begin <= end:
        m = (begin + end) // 2
        if lista [m] == item:
            return m
        if item < lista[m]:
            return binary_search(lista, item, begin, m-1)
        else:
            return binary_search(lista, item, m+1, end)
    return None

e = int(input("Elemento a ser buscado: "))
i = binary_search(lista, e)
print("\n Índice encontrado:", i)