#  Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um
#  número entre 0 e 10. Só que agora o jogador vai tentar adivinhar
#  até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random
print('''Sou o *%¨$¨$## Acabei de pensar em um número entre 1 e 10
         Tente adivinhar!!!''')
nun=int(input('Digite um número'))
adi=random.randint(1, 10)
contador = 0
contador += 1 # <---- contar com o nun fora do while
while nun != adi:
    nun=int(input('Errou! Digite outro número!'))
    contador += 1 # <------ contar com o nun dentro do while
    if nun < adi:
        print('Suba mais o valor, tente novamente!')
    elif nun > adi:
        print('Deça mais esse valor aí!!')
print('acertou!!! foram {} palpites, até o acerto, Parabéns!'.format(contador))



