'''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
print('='*20)
print('{:^20}'.format('CAIXA'))
print('='*20)
valor = int(input('Que valor você quer sacar? :'))
monte = valor
ced = 50
totced = 0#<-- para contar o total de cedulas que tem que dar
while True:
    if monte >= ced:
        monte -= ced#<-aqui vai tirar 50 do valor
        totced += 1 #<-contar quantas vezes vai tirar 50 do valor
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R${ced}')
        if ced == 50:#<-se eu não conseguir tirar mais cedulas de 50
            ced = 20 #vai tirar com as de vinte e etc...
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if monte == 0:
            break
print('='*20)
print('fim')

