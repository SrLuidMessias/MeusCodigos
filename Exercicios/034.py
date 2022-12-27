#  Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para
#  salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento 
#  é de 15%.

salario=float(input('qual o seu salário? R$'))
persu=10/100.0
au= persu * salario
novosala= salario + au
persui= 15 / 100.0
auin= persui * salario
novosalain= salario + auin
if salario > 1250.00:
    print('seu salário aumentará R${}'.format(novosala))
if salario <= 1250.00:
    print('seu salário aumentará R${}'.format(novosalain))
print('fim')
