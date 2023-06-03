print('=-='*20)
print('\033[7;40m{:^60}\033[m'.format('ANALISADOR COMPLETO'))
print('=-='*20)
somaidade = 0
maioridade = 0
totalm = 0
homemvelho = ' '
for n in range(1, 5):
    print('{:^60}'.format('{}a pessoa'.format(n)))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade (anos): '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade = somaidade + idade
    mediaidade = somaidade/n
    if sexo == 'M':
        if n == 1:
            maioridade = idade
            homemvelho = nome
        else:
            if idade > maioridade:
                maioridade = idade
                homemvelho = nome
    if sexo == 'F':
        if idade < 20:
            totalm = totalm + 1
print('-'*60)
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} e se chama {}.'.format(maioridade, homemvelho))
print('O total de mulheres abaixo de 20 anos é igual a {}.'.format(totalm))
print('\033[7;40m{:^60}\033[m'.format('FIM'))