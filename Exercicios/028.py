#Escreva um programa que faça o computador “pensar” em um número inteiro entre 1 e 5 e peça para o usuário 
# tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
import emoji

print(emoji.emojize(':crossed_swords:'*20))
print('JOGO DA ADIVINHAÇÃO')
print(emoji.emojize(':crossed_swords:'*20))
import random
from time import sleep
num=int(input('digite um número de 1 a 5!:'))
adi=random.randint(1, 5)
print(emoji.emojize(':stopwatch: processando...'))
sleep(2)
if num == adi :
    print(emoji.emojize(':partying_face:...acertou!! O número escolhido é:{}'.format(adi)))
else:
    print(emoji.emojize(':sad_but_relieved_face: errou!! Meu número era:{}!'.format(adi)))
print('...tente denovo! press "ENTER"')
 

