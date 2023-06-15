print('+=+'*15)
print('{:^60}'.format('\033[1;7;31;47mLeitura de número\033[m'))
print('+=+'*15)
tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatrorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
continua = ' '
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if n < 0 or n > 20:
        print('ERRO!!! Tente novamente.')
    else:
        print(f'Você digitou o numero {tupla[n]}.')
        print('-'*45)
        continua = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
        if continua == 'S':
            print('\033[1;34mContinua...\033[m')
        elif continua == 'N':
            break
print('\033[1;43mFIM\033[m')