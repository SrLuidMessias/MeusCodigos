'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
import emoji
print('\033[32m-=\033[m'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('\033[32m-=\033[m'*20)
v1 = p2 = 0
while True:
    n = int(input('Diga um valor :'))
    pari = str(input('Par ou ímpar? [P|I] :')).upper()
    print('\033[35m-\033[m' * 20)
    pc = randint(0, 11)
    soma = n + pc

    if soma % 2 == 0 :
        print(f'Você jogou {n} e o pc jogou {pc} total de {soma} deu PAR')
        if pari == 'P' and soma % 2 == 0:
            print('você VENCEU!')
            v1 += 1
        elif pari == 'I' and soma % 2 == 0:
            print(emoji.emojize('você PERDEU!:rolling_on_the_floor_laughing:'))
            p2+=1
    else:
        print(f'Você jogou {n} e o pc jogou {pc} total de {soma} deu ÍMPAR')
        if pari == 'I' and soma % 2 != 0:
            print('você VENCEU!')
            v1 += 1
        elif pari == 'P' and soma % 2 != 0:
            print(emoji.emojize('você PERDEU!:rolling_on_the_floor_laughing:  '))
            p2 += 1
    print('\033[35m-\033[m'*20)
    stop = str(input('Quer Continuar [S|N]? :')).upper()
    if stop == 'N':
        break
print(f'total de vitórias foi {v1} e derrotas {p2}')
print('Obrigado por jogar, e nunca mais volte!!!')




