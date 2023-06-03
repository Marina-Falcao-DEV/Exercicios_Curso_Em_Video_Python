print('*'*30)
print('{:^30}'.format('Validação de Dados'))
print('*'*30)
sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Erro!!! Digite M para masculino ou F para feminino: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
print('FIM')
