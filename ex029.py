print('-=-'*20)
print(' '*15,'Radar Eletrônico', ' '*15)
print('-=-'*20)
velocidade = float(input('Qual a velocidade do carro em Km/h?'))
multa = float(7*(velocidade-80))
if velocidade > 80:
    print('MULTADO!!! Você excedeu o limite de velocidade permitido, que é de 80 Km/h.\nO valor da multa será de R${:.2f}.'.format(multa))
print('Tenha um bom dia!!! Dirija com segurança.')
