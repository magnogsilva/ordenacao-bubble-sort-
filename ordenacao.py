from random import randint

def bubble_sort(lista):
    for i in range(len(lista)): 
        for j in range(0, len(lista) - i - 1):
            if lista[j] > lista[j+1]:
                troca = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = troca
                print(lista)
    
lista = list()
cont = 0
while True:
    num = randint(1,30)
    if num not in lista:
        lista.append(num)
        cont += 1
    if cont >= 10:
        break 
print(lista)
print('='*40)
bubble_sort(lista)
