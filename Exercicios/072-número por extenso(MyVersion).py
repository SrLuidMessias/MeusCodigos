'''Crie um programa que tenha uma dupla totalmente preenchida
com uma contagempor extenso, de zero até vinte. Seu programa
deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

numbers = ('zero', 'one', 'two', 'three', 'four', 'five', 'six'
, 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen'
, 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')
while True:
    numberchoice = int(input('Type a number between 0 and 20:'))#<-- você na verdade está digitando a posição
    if 0 <= numberchoice <= 20:
        print(f'{numbers[numberchoice]}')
    elif numberchoice != numbers:
        numberchoice = int(input('Something was wrong, type again :'))
        print(f'{numbers[numberchoice]}')
    finish = str(input('Do you want continue? S or N? :')).upper().strip()[0]
    if finish == 'N':
        break
print('thank you !!!')