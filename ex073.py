print('-'*60)
print('<'*18, '\033[32mCAMPEONATO BRASILEIRO\033[m', '>'*18)
print('-'*60)
times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Atlético-MG', 'Fluminense', 'Grêmio', 'Atlético-PR', 'São Paulo', 'Cruzeiro', 'Internacional',
         'Fortaleza', 'Bragantino', 'Santos', 'Cuiabá', 'Bahia', 'Corinthians', 'Goiás', 'América-MG', 'Vasco', 'Coritiba')
print(f'\033[33mAnalisando os {len(times)} primeiros times do Campeonato Brasileiro...\033[m')
print(times)
print(f'\n1) Os \033[1;30;46m5 primeiros times\033[m do campeonato por ordem de colocação são: {times[:5]}')
ordem = 0
for c in range(0,5):
    ordem = ordem + 1
    print(ordem, end=' -> ')
    print(times[c])
print(f'\n2) Os \033[1;30;46m4 últimos times\033[m do campeonato brasileiro são: {times[-4:]}')
ordemfim = 16
for c in range(16,20):
    ordemfim = ordemfim + 1
    print(ordemfim, end=' -> ')
    print(times[c])
print(f'\n3) Os nomes dos \033[1;30;46m{len(times)} times por ordem alfabética\033[m são: \n{sorted(times)}')
print(f'\n4) O time Bragantino está na \033[1;30;46m{times.index("Bragantino")+1}a posição\033[m do campeonato.')
print('-'*60)
print('FIM')