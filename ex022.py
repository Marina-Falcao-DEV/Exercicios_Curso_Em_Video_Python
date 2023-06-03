nome = str(input('Qual o seu nome?')).strip()
print('Seu nome é: {}'.format(nome))
print('Seu nome em maiúsculo é: {}'.format(nome.upper()))
print('Seu nome em minúsculo é: {}'.format(nome.lower()))
print('Seu nome tem {} letras com espaços.'.format(len(nome)))
print('Seu nome tem {} letras sem espaços.'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
separa = nome.split()
print(separa)
print('Seu primeiro nome tem {} letras.'.format(len(separa[0])))



