print('<>'*40)
print('{:^80}'.format('LOJÃO DA INFORMÁTICA'))
print('<>'*40)
continuar = ' '
valorcompras = 0
cont1000 = 0
precoproduto = 0
barato = ' '
contbarato = 0
menorpreco = 0
while True:
    nomeproduto = str(input('Nome do produto: ')).strip().title()
    precoproduto = float(input('Preço do produto: R$ '))
    contbarato = contbarato + 1
    if contbarato == 1 or precoproduto <= menorpreco:
        menorpreco = precoproduto
        barato = nomeproduto
    valorcompras = valorcompras + precoproduto
    if precoproduto > 1000:
        cont1000 = cont1000 + 1
    continuar = str(input('Quer continuar adicionando produtos [S/N]? ')).strip().upper()[0]
    print('-'*45)
    if continuar == 'N':
        break
print('='*80)
print(f'O total das compras foi R$ {valorcompras:.2f}.')
print(f'Há {cont1000} produtos custando acima de R$ 1.000,00.')
print(f'O produto mais barato foi {barato} e custou {menorpreco:.2f}.')
