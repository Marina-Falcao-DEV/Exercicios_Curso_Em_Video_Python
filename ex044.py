#Resolução - opção 1
print('='*9,'GERENCIADOR DE PAGAMENTOS','='*9)
print('-'*15,'\033[7;34mLojão Digital\033[m','-'*15)
print('='*45)
preco_normal = float(input('Digite o valor do produto: R$ '))
opcao_pagamento = int(input("""Escolha uma das formas de pagamento:
[ 1 ] À vista (dinheiro/cheque)
[ 2 ] À vista (cartão)
[ 3 ] 2X (cartão)
[ 4 ] 3x ou mais (cartão)
Opção: """))
if opcao_pagamento == 1:
    print('O seu pagamento será realizado à vista em dinheiro/cheque e terá um desconto de 10%.')
    preco_dinheiro = preco_normal - preco_normal*0.1
    print('A sua compra de R$ {} custará R$ {} após o desconto.'.format(preco_normal, preco_dinheiro))
elif opcao_pagamento == 2:
    print('O seu pagamento será realizado à vista em cartão e terá um desconto de 5%.')
    preco_cartao = preco_normal - preco_normal*0.05
    print('A sua compra de R$ {} custará R$ {} após o desconto.'.format(preco_normal, preco_cartao))
elif opcao_pagamento == 3:
    print('O seu pagamento será realizado em 2X no cartão e terá o preço normal.')
    preco_2X = preco_normal
    print('A sua compra custará R$ {} e não terá desconto.'.format(preco_2X))
elif opcao_pagamento == 4:
    print('O seu pagamento será realizado em 3X ou mais no cartão e terá um acréscimo de 20%.')
    preco_3X = preco_normal + preco_normal * 0.20
    print('A sua compra de R$ {} custará R$ {} após os juros.'.format(preco_normal, preco_3X))
print('\033[2;36mAproveite suas compras. Volte sempre!!!\033[m')
print(' ')
#Resolução - opção 2
print('='*9,'GERENCIADOR DE PAGAMENTOS','='*9)
print('-'*15,'\033[7;34mLojão Digital\033[m','-'*15)
print('='*45)
preco_normal = float(input('Digite o valor do produto: R$ '))
opcao_pagamento = int(input("""Escolha uma das formas de pagamento:
[ 1 ] Dinheiro/cheque
[ 2 ] Cartão de crédito
Opção de pagamento: """))
if opcao_pagamento == 1:
    print('O seu pagamento será realizado à vista em dinheiro/cheque e terá um desconto de 10%.')
    preco_dinheiro = preco_normal - preco_normal*0.1
    print('A sua compra de R$ {} custará R$ {} após o desconto.'.format(preco_normal, preco_dinheiro))
elif opcao_pagamento == 2:
    n_parcelas = int(input('Em quantas parcelas você quer pagar? '))
    if n_parcelas == 1:
        print('O seu pagamento será realizado à vista em cartão e terá um desconto de 5%.')
        preco_cartao = preco_normal - preco_normal*0.05
        print('A sua compra de R$ {} custará R$ {} após o desconto.'.format(preco_normal, preco_cartao))
    elif n_parcelas == 2:
        print("O seu pagamento será realizado em 2X no cartão e terá o preço normal.")
        preco_2X = preco_normal
        print('A sua compra custará R$ {} e não terá desconto.'.format(preco_2X))
    elif n_parcelas >= 3:
        print('O seu pagamento será realizado em 3X ou mais no cartão e terá um acréscimo de 20%.')
        preco_3X = preco_normal + preco_normal * 0.20
        print('A sua compra de R$ {} custará R$ {} após os juros.'.format(preco_normal, preco_3X))
print('\033[2;36mAproveite suas compras. Volte sempre!!!\033[m')
