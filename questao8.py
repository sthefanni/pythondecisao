p1 = input('Digite o primeiro preço: ')
p2 = input('Digite o segundo preço: ')
p3 = input('Digite o terceiro preço: ')

def menor():
    if p1 < p2 and p1 < p3:
        menor = p1
    elif p2 < p1 and p2 < p3:
        menor = p2
    else:
        menor = p3
    return menor

print 'O menor preço é:', menor()

