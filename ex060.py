print('*'*40)
print('{:^40}'.format('CALCULADORA DE FATORIAL'))
print('*'*40)
n = int(input('Digite um número: '))
fatorial = 0
print('{}! = '.format(n), end=' ')
for c in range(n, 0, -1):
    print('{} x '.format(c), end=' ')
    fatorial = n*(n-c)
print(' = {} '.format(fatorial), end='')
