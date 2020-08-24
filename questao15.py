l1 = input('Insira a medida do primeiro lado: ')
l2 = input('Insira a medida do segundo lado: ')
l3 = input('Insira a medida do terceiro lado: ')
 
if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    if l1 == l2 and l1 == l3:
        print 'Triângulo Equilátero'
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print 'Triângulo Isósceles'
    elif l1 != l2 and l3 or l2 != l1 and l3 or l1 != l3:
        print 'Triângulo Escaleno'
else:
    print 'Não é um triângulo'
