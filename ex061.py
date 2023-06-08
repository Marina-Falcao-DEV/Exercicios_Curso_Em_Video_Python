print('\033[1;33mLeitor de de PA')
print('+=+'*20, '\033[m')
n = int(input('Qual o primeiro termo?'))
r = int(input('Qual a razão? '))
c = 1
print(n, end=' -> ')
while c < 10:
    c = c + 1
    n = n + r
    print(n, end=' -> ')
print('\033[1;33mFIM\033[m')

