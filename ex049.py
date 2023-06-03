n = int(input('\033[31mDigite um número para ver a sua tabuada: \033[m'))
print('\033[1;36m=-'*10)
print('{:^20}'.format('TABUADA'))
print('=-'*10, '\033[m')
multiplicador = 0 # MANEIRA MAIS COMPLICADA
for c in range (1,11):
    multiplicador = multiplicador+1
    resultado = n * multiplicador
    print('{} X {:2} = {}'.format(n, c, resultado))
print('FIM')
n = int(input('\033[31mDigite um número para ver a sua tabuada: \033[m')) # MANEIRA MAIS SIMPLES
for c in range (1,11):
    print('{} X {:2} = {}'. format(n, c, n*c))