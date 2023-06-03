print('+'*40)
print('{:^40}'.format('SOMA DOS PARES'))
print('+'*40)
soma = 0
contadorsoma = 0
for c in range(1,7):
    n = int(input('Digite o {}o valor: '.format(c)))
    if n % 2 == 0:
        contadorsoma = contadorsoma + 1
        soma = soma + n
print('\033[7;42mA soma dos {} valores pares encontrados é igual a {}.\033[m'.format(contadorsoma, soma))


