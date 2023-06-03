n = str(input('Qual o seu nome completo?')).strip().title()
nome = n.split()
print('Seja bem vindo(a) {}!!!'.format(n))
print('Seu primeiro nome é: {}.'.format(nome[0]))
print('Seu último nome é: {}.'.format(nome[len(nome)-1]))


