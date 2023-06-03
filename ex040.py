print('\033[1;36mSituação escolar do aluno:')
print('-'*30,'\033[m')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1+nota2)/2
print('A sua média foi {:.2f}.'.format(media))
if media < 5:
    print('\033[31mVocê está \033[4mREPROVADO\033[m\033[31m!!!\033[m')
elif media >= 5 and media <= 6.9:
    print('\033[33mVocê está em \033[4mRECUPERAÇÃO\033[m\033[m. Estude mais!!!\033[m')
else:
    print('\033[32mVocê está \033[4mAPROVADO\033[m\033[32m. Parabéns!!!\033[m')
