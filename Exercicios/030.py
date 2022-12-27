# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
nun=int(input('Digite um número:'))
par=nun % 2 #Todo número que é par é divisivel por 2, e seu resto é '0' !!!
if par == 0 :
    print('seu número é par!')
else:
    print('seu número é ínpar')
print('fim')
