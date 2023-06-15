print('*'*30)
print('{:^30}'.format('CAIXA ELETRÔNICO'))
print('*'*30)
saque = int(input('Qual o valor do saque? R$ '))
valorrestante = saque
cedula = 50
while True:
    if valorrestante >= cedula:
        totcedulas = valorrestante // cedula
        valorrestante = valorrestante % cedula
    else:
        if cedula > 0:
            print(f'No total foram {totcedulas} de R$ {cedula}.')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        if valorrestante == 0:
            break
print('Obrigado pela preferência. Volte sempre!!!')