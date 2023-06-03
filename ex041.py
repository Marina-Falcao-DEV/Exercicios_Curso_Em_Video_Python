print('+='*20)
print('Categorias dos atletas da natação:')
print('+='*20)
from datetime import date
ano_atual = date.today().year
ano_nascimento = int(input('Qual o ano do seu nascimento? '))
idade = ano_atual - ano_nascimento
print('Você tem {} anos e está ... '.format(idade), end='')
if idade <= 9:
    print('na categoria \033[3;31mMIRIM\033[m.')
elif idade > 9 and idade <= 14:
    print('na categoria \033[3;31mINFANTIL\033[m.')
elif idade > 14 and idade <= 19:
    print('na categoria \033[3;31mJÚNIOR\033[m.')
elif idade > 19 and idade <= 25:
    print ('na categoria \033[3;31mSÊNIOR\033[m.')
elif idade > 25:
    print('na categoria \033[3;31mMASTER\033[m.')