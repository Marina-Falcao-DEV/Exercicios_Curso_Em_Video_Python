print('Custo da Viagem')
print('-'*25)
distancia = float(input('QUal a distância da viagem em Km? '))
if distancia <= 200:
    precoa = distancia * 0.5
    print('A passagem para uma viagem de {} Km custará R$ {:.2f}'.format(distancia, precoa))
else:
    precob = distancia * 0.45
    print('A passagem para uma viagem de {} Km custará R$ {:.2f}'.format(distancia, precob))
