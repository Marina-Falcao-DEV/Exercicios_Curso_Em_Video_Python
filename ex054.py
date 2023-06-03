print('Leitor de maioridade: ')
print('='*35)
from datetime import date
totalmaior = 0
totalmenor = 0
for c in range(1, 8):
    nascimento = int(input('Em que ano a {}a pessoa nasceu?'.format(c)))
    anoatual = date.today().year
    idade = anoatual - nascimento
    if idade >= 21:
        totalmaior = totalmaior + 1
    else:
        totalmenor = totalmenor + 1
print('O total de \033[1;34mMAIORES\033[m (igual ou acima de 21 anos) foi de \033[1;34m{}\033[m pessoas.'.format(totalmaior))
print('O total de \033[1;35mMENORES\033[m (abaixo de 21 anos) foi de \033[1;35m{}\033[m pessoas.'.format(totalmenor))

