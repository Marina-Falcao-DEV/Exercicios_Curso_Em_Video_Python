print('+=+'*20)
print('{:^60}'.format('MAIOR E MENOR PESO DA LISTA'))
print('+=+'*20)
maiorpeso = 0
menorpeso = 0
for c in range(1, 6):
    peso = float(input('Qual o seu peso da {}a pessoa (Kg)? '.format(c)))
    if c == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
        if peso == menorpeso == maiorpeso:
            menorpeso = maiorpeso
print('O maior peso é: {} Kg.'.format(maiorpeso))
print('O menor peso é: {} Kg.'.format(menorpeso))
print('Os pesos de todas as pessoas são iguas com valores de {} Kg.'.format(peso))


