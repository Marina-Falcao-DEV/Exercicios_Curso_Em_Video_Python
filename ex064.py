from time import sleep
print('^'*60)
print('{:^60}'.format('\033[1;34mTratando vários valores\033[m'))
print('^'*60)
n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input('Digite um número [escreva 999 para parar]: '))
    if n != 999:
        cont = cont + 1
        soma = soma + n
print('\nPROCESSANDO...')
sleep(2)
print('\n\033[1;34mVocê digitou {} números e a soma entre eles foi igual a {}.\033[m'.format(cont, soma))