p = input('Primeiro numero: ')
s  = input('Segundo numero : ')
t = input('Terceiro numero: ')

    if(t > s):
        x = t
        terceiro = s
        s = x

    if(s > p):
        x = s
        s = p
        p = x

    if(t > s):
        x = t
        t = s
        s = x

    print(p,', ',s,', ',t)

