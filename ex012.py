print('='*20, 'Calculando Desconto', '='*20)
print('-'*61)
preco = float(input('Qual o preço do produto? R$ '))
desconto = preco*(1-0.05)
print('O valor do produto que custava R$ {:.2f} com o desconto ficará custando R$ {:.2f}.'.format(preco, desconto))
print('-'*61)