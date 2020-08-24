salario = input(‘Insira seu salário: ‘)
if salario <= 280.00:
      x = (20 / 100.0) * salario
      r = salario + x
      print ‘Seu salário antes do reajuste: R$’,salario
      print ‘Percentual aumentado: %’,20
      print ‘O valor do aumento é: R$’,x
      print ‘Com o reajuste, o seu salário é: R$’,r
elif salario > 280.00 and salario <= 700.00:
        x = (15 / 100.0) * salario
        r = salario + x
        print ‘Seu salário antes do reajuste: R$’,salario
        print ‘Percentual aumentado: %’,15
        print ‘O valor do aumento é: R$’,x
        print ‘Com o reajuste, o seu salário é: R$’,r
elif salario > 700.00 and salario <= 1500.00:
        por = (10 / 100.0) * salario
        r = salario + x
        print ‘Seu salário antes do reajuste: R$’,salario
        print ‘Percentual aumentado: %’,10
        print ‘O valor do aumento é: R$’,x
        print ‘Com o reajuste, o seu salário é: R$’,r
elif salario > 1500.00:
        x = (5 / 100.0) * salario
        r = salario + x
        print ‘Seu salário antes do reajuste: R$’,salario
        print ‘Percentual aumentado: %’,5
        print ‘O valor do aumento é: R$’,x
        print ‘Com o reajuste, o seu salário é: R$’,r
