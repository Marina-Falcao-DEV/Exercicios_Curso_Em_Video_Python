print('!'*60)
print('{:^60}'.format('ANALISADOR DE VALORES'))
print('!'*60)
n = int(input('Digite um número: '))
continua = str(input('Quer continuar [S/N]')).strip().upper()
cont = 1
soma = n
media = 0
maior = n
menor = n
while continua == "S":
    n = int(input('Digite um número: '))
    continua = str(input('Quer continuar [S/N]')).strip()[0].upper()
    cont = cont + 1
    soma = soma + n
    media = soma/cont
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
print('!'*60)
print('FIM...\n\033[33mVocê digitou {} números e a média entre eles foi {:.2f}.'.format(cont, media))
print ('O maior valor foi {} e o menor foi {}.\033[m'.format(maior, menor))
print('!'*60)