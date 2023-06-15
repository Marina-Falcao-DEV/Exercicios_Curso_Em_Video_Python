print('^'*60)
print('{:^60}'.format('TABUADA'))
print('^'*60)
cont = 0
multiplicacao = 1
while True:
    n = int(input('Você quer ver o valor da tabuada de qual número? '))
    if n < 0:
        break
    for cont in range(0, 10):
        cont = cont + 1
        multiplicacao = cont * n
        print(f'{n} x {cont:^2} = {multiplicacao}')
print('FIM... O programa acabou!!!')
