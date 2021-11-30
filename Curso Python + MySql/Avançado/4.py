
def pares(i):
    if i % 2 == 1:
        return i

x = [1,2,3,4,5,450]

lista = filter(pares,x)
print(list(lista))