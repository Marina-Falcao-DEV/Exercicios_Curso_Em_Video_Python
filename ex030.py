print('PAR ou ÍMPAR')
print('-'*15)
numero = int(input('Digite um número inteiro:'))
n = numero%2
if n == 0:
    print ('O número {} é PAR.'.format(numero))
else:
    print('O número {} é ÍMPAR.'.format(numero))

