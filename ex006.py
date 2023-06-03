print('Dobro, Triplo e Raiz Quadrada')
print('='*25)
#Código com 1 variável
n = int(input('Digite um número:'))
print('O número {} tem como dobro o número {}, como triplo o número {} e como raiz quadrada o número {:.3f}.'.format(n, (n*2), (n*3), (n**(1/2))))
print('-'*20)
#Código com várias variáveis
n = int(input('Digite um número:'))
nd = n*2
nt = n*3
nr = n**(1/2)
print('O número {} tem como dobro o número {}, como triplo o número {} e como raiz quadrada o número {:.3f}'.format(n, nd, nt, nr))
print('-'*20)
#Código com função de raiz quadrada
n = int(input('Digite um número:'))
print('O número {} tem como dobro: {}. \nO número {} tem como triplo: {}. \nO número {} tem como raiz quadrada: {:.3f}.'.format(n,(n*2), n, (n*3), n, pow(n, (1/2))))
print ('='*5, 'Fim', '='*5)
