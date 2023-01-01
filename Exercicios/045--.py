# Crie um programa que faça o computador jogar Jokenpô com você.
# o melhor!!!!
from random import randint
import emoji
from time import sleep 
itens = ('pedra', 'papel', 'tesoura')
computador= randint(1,2)  ### !!!!sempre começe com zero nesse caso !!!!senão vai ter erro de falta de caracteres
print(emoji.emojize('''escolha
[0] pedra :curling_stone:
[1] papel :roll_of_paper:
[2] tesoura :scissors:'''))
jogador = int(input('Qual a sua jogada??'))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ')
print('=-'*20)
print('o computador escolheu {}'.format(itens [computador]))
print('E você escolheu {}'.format(itens[jogador]))
print('=-'*20)
if computador == 0:
    if jogador == 0:
        print(emoji.emojize('empate:face_exhaling:'))
    elif jogador == 1:
        print(emoji.emojize('você venceu:partying_face:'))
    elif jogador == 2:
        print(emoji.emojize('você perdeu:sad_but_relieved_face:'))
if computador == 1:
    if jogador == 1:
        print(emoji.emojize('empate:face_exhaling:'))
    elif jogador == 0:
        print(emoji.emojize('você perdeu:sad_but_relieved_face:'))
    elif jogador == 2:
        print(emoji.emojize('você venceu:partying_face:'))
if computador == 2:
    if jogador == 0: 
        print(emoji.emojize('você venceu:partying_face:'))
    elif jogador == 1:
        print(emoji.emojize('você perdeu:sad_but_relieved_face:'))
    elif jogador == 2:
        print(emoji.emojize('empate:face_exhaling:'))


