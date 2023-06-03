#Fórmula matemática
co = float(input('Qual o tamanho do cateto oposto em cm?'))
ca = float(input('Qual o tamanho do cateto adjacente em cm?'))
h = (co**2+ca**2)**(1/2)
print('A hipotenusa deste triângulo retângulo é: {:.2f} cm.'.format(h))
print('-'*30)
#Importação de biblioteca Math
import math
co = float(input('Qual o tamanho do cateto oposto em cm?'))
ca = float(input('Qual o tamanho do cateto adjacente em cm?'))
h = math.hypot(co, ca)
print('A hipotenusa deste triângulo retângulo é: {:.2f} cm.'.format(h))
print('-'*30)
#Importação das funções da biblioteca Math
from math import hypot
co = float(input('Qual o tamanho do cateto oposto em cm?'))
ca = float(input('Qual o tamanho do cateto adjacente em cm?'))
h = hypot(co, ca)
print('A hipotenusa deste triângulo retângulo é: {:.2f} cm.'.format(h))
