print('='*21, 'Pintando Paredes', '='*21)
print('-'*60)
largura = float(input('Qual a largura da parede em metros? '))
altura = float(input('Qual a altura da parede em metros?'))
area = largura*altura
tinta = area/2
print('A área da parede é de {} m2. \nA quantidade de tinta necessária para a pintura é {} litros.'.format(area, tinta))
print('='*60)
