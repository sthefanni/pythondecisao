n1 = input('Insira a primeira nota: ')
n2 = input('Insira a segunda nota: ')

r = (n1 + n2) / 2

if r >= 7 and nota < 10:     
    print 'Aprovado' 
elif r >= 10:
    print 'Aprovado com Distinção'
else:
    print 'Reprovado'
