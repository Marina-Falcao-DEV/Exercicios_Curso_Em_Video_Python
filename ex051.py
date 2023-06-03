print('\033[1;36mDez termos de uma PA')
print('='*30, '\033[m')
n1 = int(input('Primeiro número: '))
r = int(input('Razão: '))
n = n1
for c in range(1, 11):
    n = n1 + (c-1)*r
    print(n, end=' -> ')
print('\033[31mFIM\033[m')