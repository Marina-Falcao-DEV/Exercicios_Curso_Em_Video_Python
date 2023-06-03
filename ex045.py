print('\033[1;32m==+'*20)
print('{:^40}'.format('GAME: Pedra, Papel e Tesoura'))
print('==+'*20,'\033[m')
print(' ')
from random import randint
computador = randint(0,2)
itens = ('pedra', 'papel', 'tesoura')
jogador = int(input("""Selecione uma das opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
Sua jogada: """))
from time import sleep
print ('\033[1;34mAguarde ... processando!!!\033[m')
sleep(1)
print('\033[1;31mJO')
sleep(1)
print('{:^10}'.format('KEN'))
sleep(1)
print('{:^20}'.format('PÔ\033[m'))
print('\033[1;32m==+'*20)
print('O computador escolheu {}'.format(itens[computador]), end =' ')
print('e você escolheu {}.'.format(itens[jogador]))
if computador == 0:
    if jogador == 0:
        print('EMPATE!!!')
    elif jogador == 1:
        print ('Você GANHOU!!!')
    elif jogador == 2:
        print ('Você PERDEU!!!')
    else:
        print('ERRO!!! Repita, número inválido.')
elif computador == 1:
    if jogador == 0:
        print ('Você PERDEU!!!')
    elif jogador == 1:
        print('EMPATE!!!')
    elif jogador == 2:
        print('Você GANHOU!!!')
    else:
        print('ERRO!!! Repita, número inválido.')
elif computador == 2:
    if jogador == 0:
        print('Você GANHOU!!!')
    elif jogador == 1:
        print('Você PERDEU!!!')
    elif jogador == 2:
        print('EMPATE!!!')
    else:
        print('ERRO!!! Repita, número inválido.')
print('==+'*20,'\033[m')