print('{:^40}'.format('A soma de ímpares múltiplos de 3:'))
print('-'*40)
soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c, end=' ')
        contador = contador + 1
        soma = soma + c
print('\nA soma de todos os {} números encontrados será: {}.'.format(contador, soma))
print('FIM')
print(' ')
