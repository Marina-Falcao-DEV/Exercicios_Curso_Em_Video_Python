frase = str(input('Escreva uma frase: ')).lower().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('a')))
print('Em qual posição ela aparece pela primeira vez? {}'.format(frase.find('a')+1)) # O "+1" indica a posição que nós lemos (començando a contagem do 1) e não a posição que o Python lê (começando a contagem do 0)
print('Em qual posição ela aparece pela última vez? {}'.format(frase.rfind('a')+1))