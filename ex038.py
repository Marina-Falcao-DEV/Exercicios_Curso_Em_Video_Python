print('\033[1;34m**-\033[m'*10)
print(' '*5,'Contando os números',' '*5)
print('\033[1;34m**-\033[m'*10)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('O primeiro número é maior do que o segundo.')
elif n2 > n1:
    print('O segundo número é maior do que o primeiro.')
else:
    print('Os dois números são iguais!!!')
print('\033[1;33m-'*30)
print('FIM')

