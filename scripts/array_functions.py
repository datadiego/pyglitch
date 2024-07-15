from random import shuffle

def shift(lista, n):
    return lista[n:] + lista[:n]

def randomize(lista):
    shuffle(lista)
    return lista


