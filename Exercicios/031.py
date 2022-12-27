# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.


from datetime import date # Pega a data atual 
ano=int(input('Digite um ano qualquer, ou coloque "0" para analizar o ano atual:'))
if ano == 0:
    ano=date.today().year 
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 : # Espressão completo para saber se o ano é bissexto
    print('o ano {} é bissexto'.format(ano))
else:
    print('o ano {} não é bissexto'.format(ano))
print('fim')