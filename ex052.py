print('='*40)
print('{:^50}'. format('\033[7;48mNÚMERO PRIMO\033[m'))
print('='*40)
n = int(input('Digite um número: '))
total = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[32m', end=' ')
        total = total + 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print('\n')
print('\033[mO número {} foi divisível {} vezes.'.format(n, total))
if total == 2:
    print('Este número é \033[1;34mPRIMO\033[m!!!')
else:
    print('Este número \033[1;33mNÃO\033[m é primo.')