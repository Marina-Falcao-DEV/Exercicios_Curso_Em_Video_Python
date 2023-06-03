print('\033[31m=\033[m'*30)
print('\033[1;34mCalculadora de Empréstimos\033[m')
print('\033[31m=\033[m'*30)
casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário? R$ ' ))
anos = int(input('Em quanto anos você quer pagar a casa? '))
prestacao = casa/(anos * 12)
print('Para pagar uma casa no valor de \033[42m{:.2f}\033[m em \033[41m{}\033[m anos, \na prestação será de R$ \033[43m{:.2f}\033[m.'.format(casa,anos,prestacao))
if prestacao <= salario*0.3:
    print('\033[32mParabéns!!! O seu empréstimo foi aprovado.\033[m')
else:
    print('\033[31mInfelizmente o seu empréstimo foi negado.\033[m')