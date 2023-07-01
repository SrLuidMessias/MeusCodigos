'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
print('=-'*20)
print('Vamos Jogar')
print('=-'*20)
while True:

    jogador = int(input('Diga o valor:'))
    pari = str(input('Par ou Ímpar [P|I] :')).upper()
    print('-' * 20)
    pc = randint(1, 10)
    soma = jogador + pc
    print(f'O computador jogou {pc} e o jogador {jogador}')
    print('Deu Par'if soma % 2 == 0  else 'deu ímpar' )
    print('-' * 20)
    if pari == 'P':
        if soma % 2 == 0:
            print('VOCÊ VECEU')
        else:
            break
    elif pari == 'I':
        if soma % 2 == 1:
            print('VOCÊ VENCEU')
        else :
            break
    print('-' * 20)
    print('vamos jogar novamente...')
print('Sem sorte! PERDEU')




