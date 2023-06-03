print('Aumento de Salários')
print('-+-'*10)
salario = float(input('Qual o seu salário? R$ '))
if salario > 1250:
    aumento = salario*1.1
else:
    aumento = salario*1.15
print('O salário de R$ {:.2f} passará a ser {:.2f} após o aumento.'.format(salario, aumento))
