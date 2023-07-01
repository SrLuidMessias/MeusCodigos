''' Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
print('=-'*10)
pv=int(input('Primeiro valor:'))
sv=int(input('Segundo valor:'))
soma = pv + sv
multi = pv * sv
opcao = 0
while opcao != 5:
    soma = pv + sv
    multi = pv * sv
    opcao = 0
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')

    opcao=int(input('>>> Qual a sua opção? :'))
    print('=-'*10)
    if opcao == 1:
        print('a soma do valor {} e {} é {}'.format(pv,sv,soma))
    elif opcao == 2:
        print('{} x {} = {}'.format(pv ,sv ,multi ))
    elif opcao == 3:
        if pv > sv:
            print('O {} é maior'.format(pv))
        else:
            print('O {} é maior'.format(sv))
    elif opcao == 4:
        pv = int(input('>>> Primeiro valor:'))
        sv = int(input('>>> Segundo valor:'))
    elif opcao == 5:
        print('Processando...')
        sleep(2)
    else:
        print('dado incorreto')
        print('Tente novamente!!')
    print('=-'*10)
print('Você saiu do programa! Obrigado e volte sempre!')





