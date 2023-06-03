print('='*30)
print(' '*5,'\033[30;44mCalculadora de IMC\033[m',' '*5)
print('='*30)
peso = float(input('Qual o seu peso (Kg)? '))
altura = float(input('Qual a sua altura (metros)? '))
imc = peso/(altura**2)
print('O valor do seu IMC foi {:.1f}.'.format(imc))
if imc < 18.5:
    print('Você está \033[7;31mABAIXO\033[m do peso. Cuidado!!!')
elif imc >= 18.5 and imc < 25:
    print('Você está com o peso \033[7;32mIDEAL\033[m. Parabéns!!! Continue assim.')
elif imc >=25 and imc < 30:
    print('Você está com \033[7;33mSOBREPESO\033[m. Atenção!!!')
elif imc >= 30 and imc < 40:
    print('Você está no nível de \033[7;31mOBESIDADE\033[m. Cuide-se!!!')
elif imc > 40:
    print('Você está no nível de \033[7;31mOBESIDADE MÓRBIDA\033[m. Já deveria estar se cuidando. Alerta máximo!!!')