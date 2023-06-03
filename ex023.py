print('Resolução com strings e sem usar as estruturas de repetição:')
print('-'*70)
n = str(input('Digite um número entre 0 e 9999: '))
print('Analisando o número {} ... Ele contém:'.format(n))
print('{} unidades'.format(n[3]))
print('{} dezenas'.format(n[2]))
print('{} centenas'.format(n[1]))
print('{} unidades de milhar'.format(n[0]))
print('-'*70)
print('Resolução com inteiro:')
print('-'*70)
n1 = int(input('Digite um número entre 0 e 9999: '))
print('Analisando o número {} ... Ele contém:'.format(n1))
u = n1//1%10
d = n1//10%10
c = n1//100%10
m = n1//1000%10
print('{} unidades'.format(u))
print('{} dezena'.format(d))
print('{} centena'.format(c))
print('{} unidades de milhar'.format(m))