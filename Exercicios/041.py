# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento 
# de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER
from datetime import date
ano_nasc = int(input('Digite seu ano de nascimento:'))
ano_atual = date.today().year
idade =ano_atual - ano_nasc
print('O atleta tem {} anos'.format(idade)) 
if idade <= 9 :
    print('classificação: mirim')
elif 14 >= idade > 9 :
    print('classificação: infantil')
elif 19 >= idade > 14 :
    print('classificação: Júnior')
elif 25 == idade :
    print('classificação: sênior')
elif idade > 25 :
    print('classificação: master')
