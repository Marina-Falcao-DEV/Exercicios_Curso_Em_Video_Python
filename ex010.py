print('<'*15,'Conversor de Moedas','>'*15)
print('-'*50)
#Código com 2 variáveis
v = float(input('Digite o valor em R$: '))
d = v/3.27
print('O valor de R${:.2f} convertido para dolar é igual a U${:.2f}.'.format(v,d))
print('-'*50)
#Código com 1 variável
v = float(input('Digite o valor em R$: '))
print('O valor de R${:.2f} convertido para dolar é igual a U${:.2f}.'.format(v, (v/3.27)))
print('='*50)

