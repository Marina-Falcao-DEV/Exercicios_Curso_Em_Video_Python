print('\033[32m+'*60)
print(' '*15,'ANALISANDO TRIÂNGULOS V.2.0',' '*15)
print('+'*60,'\033[m')
lado1 = float(input('Qual o comprimento do primeiro lado do triângulo? '))
lado2 = float(input('Qual o comprimento do segundo lado do triângulo? '))
lado3 = float(input('Qual o comprimento do terceiro lado do triângulo? '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Estes lados podem formar um triângulo.', end = ' ')
    if lado1 == lado2 == lado3:
        print('Ele será do tipo \033[4;34mEQUILÁTERO\033[m.')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Ele será do tipo \033[4;35mISÓSCELES\033[m.')
    elif lado1 != lado2 or lado1 != lado3 or lado2 != lado3:
        print('Ele será do tipo \033[4;36mESCALENO\033[m.')
else:
    print('Estes lados \033[31mNÃO\033[m podem formar um triângulo.')