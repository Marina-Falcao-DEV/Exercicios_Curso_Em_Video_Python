print('\033[1;33mLeitor de de PA')
print('+=+'*20, '\033[m')
n = int(input('Qual o primeiro termo?'))
r = int(input('Qual a razão? '))
print('{}'.format(n), end=' -> ')
c = 0
repeticoes = 9
passos = 1
while passos != 0:
    somapassos = passos + 10
    while c < repeticoes:
        c = c + 1
        n = n + r
        print('{}'.format(n), end=' -> ')
    print('PAUSA...')
    passos = int(input('\nQuantos passos mais você quer realizar? '))
print('FIM. Foram mostrados {} termos nesta PA.'.format(somapassos))