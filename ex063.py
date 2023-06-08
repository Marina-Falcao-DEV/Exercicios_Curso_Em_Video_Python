print('=-='*20)
print('{:^60}'.format('SEQUÊNCIA DE FIBONACCI V1.0'))
print('=-='*20)
termos = int(input('Quantos termos você quer mostrar? '))
ninicial = 0
nintermediario = 1
c = 0
print('{} -> {} -> '.format(ninicial, nintermediario), end=' ')
while c < (termos-2):
    c = c + 1
    nfinal = ninicial + nintermediario
    ninicial = nintermediario
    nintermediario = nfinal
    print('{}'.format(nfinal), end=' -> ')
print('FIM')