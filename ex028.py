print('--='*20)
print('Vou pensar em número entre 0 e 5. Tente adivinhar...')
print('--='*20)
import random
computador = random.randint(0,5)
usuario = int(input('Em qual número eu pensei? '))
from time import sleep
print('PROCESSANDO...')
sleep(3)
if computador == usuario:
    print('PARABÉNS!!! Você ganhou, pois pensou no mesmo número que eu, {}.'.format(computador))
else:
    print('GANHEI!!! Eu pensei no número {} e você pensou no {}.'.format(computador, usuario))

