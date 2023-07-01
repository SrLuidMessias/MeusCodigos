# Crie um programa que leia o ano de nascimento de sete pessoas. No final, 
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
ano_atual=date.today().year
contador=0
contador1=0
for c in range(1, 8):
    nascimento=int(input('Digite o ano de nascimento da {}° pessoa :'.format(c)))
    conta=ano_atual - nascimento
    if conta >= 21:
        contador += 1 # se a idade for a cima de 21, é mais uma pessoa MAIOR de idade!
    else:
        contador1 += 1 # se não, é mais uma pesseo MENOR de idade
print('são {} maiores de idade'.format(contador))
print('são {} menores de idade'.format(contador1))