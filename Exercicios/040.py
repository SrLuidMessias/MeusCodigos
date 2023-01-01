# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma 
# mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO
import emoji
import time
n1 = float(input('Primeira nota : '))
n2 = float(input('Segunda nota : '))
media = (n1+n2)/ 2
print(emoji.emojize('processando...:eight-thirty:'))
time.sleep(2)
print('tirando {} e {}, a média é {}'.format(n1, n2, media))
if media < 5.0 :
    print(emoji.emojize('o aluno está \033[1;31mreprovado\033[m:sad_but_relieved_face:'))
elif 7.0 > media >= 5.0 : # o python lê assim <-----o------>
    print(emoji.emojize('O aluno está em recuperação:expressionless_face:'))
elif media >= 7.0:
    print('O aluno está aprovado')
    print(emoji.emojize(' \033[1;35m  VIVAAAAAA :partying_face: \033[m '))