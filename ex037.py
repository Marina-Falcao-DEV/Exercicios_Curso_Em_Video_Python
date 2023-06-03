print('=-'*15)
print('\033[7;31mCONVERSOR DE BASES NUMÉRICAS\033[m')
print('=-'*15)
numero = int(input('Digite um número inteiro: '))
print("""Escolha uma das opções:
[ 1 ] Converter para BINÁRIO.
[ 2 ] Converter para OCTAL.
[ 3 ] Converter para HEXADECIMAL.""")
opcao = int(input('Digite o número de uma as 3 opções: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format(numero,bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido em OCTAL é igual a {}.'.format(numero,oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido em HEXADECIMAL é igual a {}.'.format(numero,hex(numero)[2:]))
else:
    print('\033[31mOpção INVÁLIDA!!! Tente novamente.\033[3m')
