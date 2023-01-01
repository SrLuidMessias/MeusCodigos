# Crie um programa que faça o computador jogar Jokenpô com você.
# primeira versão
import random
import time
print('''escolha um número
[1] pedra
[2] papel
[3] tesoura
''')

pedra=1
papel=2
tesoura=3
jogador=int(input('Qual a sua escolha?'))
itens=[pedra,papel,tesoura]
escolha_pc= random.choice(itens)

print('jo')
time.sleep(0.5)
print('ken')
time.sleep(0.5)
print('po')
time.sleep(0.5)


if escolha_pc == tesoura and jogador == 3:
    print('o pc jogou tesoura e o jogador tesoura ')
    print('empate')
elif escolha_pc == tesoura and jogador == 2:
    print('o pc jogou tesoura e o jogador papel ')
    print('vc perdeu')
elif escolha_pc == tesoura and jogador == 1:
    print('o pc jogou tesoura e o jogador pedra')
    print('vc venceu')
elif escolha_pc == pedra and jogador == 3:
    print('o pc jogou pedra e o jogador tesoura')
    print('vc perdeu')
elif escolha_pc == pedra and jogador == 2:
    print('o pc jogou pedra e o jogador papel')
    print('vc venceu')
elif escolha_pc == pedra and jogador == 1:
    print('o pc jogou pedra e o jogador pedra')
    print('empate')
elif escolha_pc == papel and jogador == 3:
    print('o pc jogou papel e o jogador tesoura')
    print('vc venceu')
elif escolha_pc == papel and jogador == 2:
    print('o pc jogou papel e o jogador papel')
    print('empate')
elif escolha_pc == papel and jogador == 1:
    print('o pc jogou papel e o jogador pedra')
    print('vc perdeu')