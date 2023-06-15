print('='*80)
print('{:^80}'.format('JOGO: PAR OU ÍMPAR'))
print('='*80)
from random import randint
cont = 0
jogo = ' '
resultado = ' '
while True:
    numero = randint(1,10)
    n = int(input('Digite um número [entre 1 e 10]: '))
    jogo = str(input('Par ou Ímpar [P/I]? ')).upper().strip()[0]
    soma = n + numero
    print(f'Você jogou {n} e o computador jogou {numero}. O total foi {soma} que é um número...', end='')
    if soma % 2 == 0:
        print('PAR!!!')
        resultado = 'P'.upper().strip()[0]
        if resultado == jogo:
            cont = cont + 1
            print('Você ganhou. Parabéns!!!')
        elif resultado != jogo:
            print('Você perdeu.')
            break
    else:
        print('ÍMPAR!!!')
        resultado = 'I'.upper().strip()[0]
        if resultado == jogo:
            cont = cont + 1
            print('Você ganhou. Parabéns!!!')
        elif resultado != jogo:
            print('Você perdeu.')
            break
print('='*80)
print(f'FIM DO JOGO!!! Você venceu {cont} vezes.')


