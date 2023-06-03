print('=+='*25)
print('{:^80}'.format('\033[1;7;34mJogo da Advinhação\033[m'))
print('=+='*25)
print('\033[1;34mEu sou seu computador ...\nAcabei de pensar em um número entre 1 e 10.\nTente adivinhar que número é ele.\033[m\n')
from random import randint
computador = randint(1, 10)
palpite = int(input('Seu palpite: '))
tentativa = 1
while palpite != computador:
    if palpite > computador:
        palpite = int(input('Você errou para MAIS. Tente novamente.\nSeu novo palpite: '))
        tentativa = tentativa + 1
    elif palpite < computador:
        palpite = int(input('Você errou para MENOS. Tente novamente.\nSeu novo palpite: '))
        tentativa = tentativa + 1
if computador == palpite:
    print('\n\033[31mVocê ACERTOU o número \033[1;7;33m{}\033[m\033[31m após \033[1;7;36m{}\033[m\033[31m tentativas. Parabéns!!!\033[m'.format(computador, tentativa))




