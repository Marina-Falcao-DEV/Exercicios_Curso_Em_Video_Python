print('\033[32m=+=\033[m'*10)
print(' '*5,'\033[4;42mALISTAMENTO MILITAR\033[m',' '*5)
print('\033[32m=+=\033[m'*10)
sexo = int(input(""" Escolha uma das opções: 
[ 1 ] Feminino \n[ 2 ] Masculino\n Qual o seu sexo?"""))
if sexo == 1:
    print('Você NÃO precisa de alistamento no Brasil.')
elif sexo == 2:
    print('O seu alistamento é obrigatório no Brasil!!!')
    print(' ')
    ano_nascimento = int(input('Em que ano você nasceu? '))
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual-ano_nascimento
    if idade == 18:
        print('\033[33mVocê tem 18 anos. Alistamento imediato!!!\033[m')
    elif idade < 18:
        tempo_menor = 18 - idade
        print('\033[32mSeu alistamento ainda não chegou, faltam {} anos.'.format(tempo_menor))
        ano_menor = ano_atual + tempo_menor
        print('Seu alistamento será em {}.\033[m'.format(ano_menor))
    else:
        tempo_maior = idade - 18
        print('\033[31mSeu alistamento já passou fazem {} anos.'.format(tempo_maior))
        ano_maior = ano_atual - tempo_maior
        print('Seu alistamento deveria ter sido em {}.\033[m'.format(ano_maior))

