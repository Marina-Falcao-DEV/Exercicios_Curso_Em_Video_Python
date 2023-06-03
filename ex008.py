print('='*10, 'Coversor de Medidas', '='*10)
#Conversor com várias variáveis
n = float(input('Qual o tamanho em metros? '))
cm = n*100
mm = n*1000
print('\n''O tamanho em cm é: {:.2f}'.format(cm))
print('O tamanho em mm é: {:.2f}'.format(mm))
print('-'*41)
#Conversor com 1 variável
n = float(input('\n''Qual o tamanho em metros?'))
print('O tamanho em cm é: {:.2f}'.format(n*100))
print('O tamanho em mm é: {:.2f}'.format(n*1000))
print('='*41)
