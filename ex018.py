print('>'*10, 'Seno - Coseno -Tangente','<'*10)
print('-'*45)
import math
a = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(a))
cosseno = math.cos(math.radians(a))
tangente = math.tan(math.radians(a))
print('O seno do ângulo {} é: {:.2}'.format(a,seno))
print('O cosseno do ângulo {} é: {:.2f}'.format(a,cosseno))
print('A tangente do ãngulo {} é: {:.2f}'.format(a,tangente))
print('-'*45)
from math import sin,cos,tan,radians
a = float(input('Digite um ângulo: '))
seno = sin(radians(a))
cosseno = cos(radians(a))
tangente = tan(radians(a))
print('O seno do ângulo {} é: {:.2f}'.format(a,seno))
print('O cosseno do ângulo {} é: {:.2f}'.format(a,cosseno))
print('A tangente do ângulo {} é: {:.2f}'.format(a,tangente))



