print('='*40)
print('{:^40}'.format('DETECTOR DE PALÍNDROMO'))
print('='*40)
frase = str(input('Digite uma frase: ')).strip().upper()# PRREPARO PARA LER A STRING INVERTIDA (FASE 1)
frasesplit = frase.split()# PRREPARO PARA LER A STRING INVERTIDA (FASE 2)
frasejunta = ''.join(frasesplit)# PRREPARO PARA LER A STRING INVERTIDA (FASE 3)
palindromo = frasejunta[::-1]# PRREPARO PARA LER A STRING INVERTIDA (FASE 4)
if frasejunta == palindromo: # PRIMEIRA RESOLUÇÃO
    print('A frase {} é um PALÍNDROMO da frase {}.'.format(palindromo, frasejunta))
else:
    print('A frase {} NÃO é um palíndromo da frase {}.'.format(palindromo, frasejunta))
print('*'*20, 'Modo extra', '*'*20)
print('A frase {} é palíndromo de {}? {}'.format(palindromo, frasejunta , palindromo in frasejunta)) # SEGUNDA RESOLUÇÃO

