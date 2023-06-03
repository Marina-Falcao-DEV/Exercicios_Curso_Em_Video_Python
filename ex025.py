nome = str(input('Qual o seu nome? ')).strip()
print('Seu nome é: {}.'.format(nome.title()))
print('Você tem Silva no nome? {}'.format('Silva' in nome.title()))