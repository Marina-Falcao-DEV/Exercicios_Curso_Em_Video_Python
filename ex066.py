print('+=+'*15)
print('{:^45}'.format('SOMADOR DE NÚMEROS'))
print('+=+'*15)
cont = soma = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    cont = cont + 1
    soma = soma + n
print(f'A soma dos {cont} números foi igual a {soma}.')
