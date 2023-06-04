print('*'*40)
print('{:^40}'.format('MENU OPÇÕES'))
print('*'*40)
from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
menu = 0
while menu != 5:
    print('-'*40)
    menu = int(input("""MENU OPÇÕES:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Qual a sua opção? """))
    print('-' * 40)
    if menu == 1:
        soma = n1 + n2
        print('O resultado da soma entre {} e {} é igual a {}.'.format(n1, n2, soma))
    elif menu == 2:
        multiplicacao = n1 * n2
        print('O resultado da multiplicação entre {} e {} é igual a {}.'.format(n1, n2, multiplicacao))
    elif menu == 3:
        if n1 > n2:
            print('O número {} é maior do que o número {}.'.format(n1, n2))
        elif n2 > n1:
            print('O número {} é maior do que o número {}.'.format(n2, n1))
        elif n1 == n2:
            print('Os números {} e {} são iguais.'.format(n1, n2))
    elif menu == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif menu == 5:
        print('FNALIZANDO...')
    else:
        print('ERRO... Digite a opção de menu correta.')
sleep(2)
print('Saiu do programa. Obrigado pela preferência!!!')
