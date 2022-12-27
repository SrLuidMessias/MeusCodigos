# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('\033[1;31;45m qual o valor da casa \033[m ? :'))
salario_comprador = float(input('\033[1;31;45m qual o seu salário \033[m ? :'))
anos_pagar = int(input('\033[1;31;45m Quantos anos deseja pagar \033[m ? :'))
prestação = valor_casa / (anos_pagar * 12)
calculo = salario_comprador / 100

print('Uma casa no valor de R${:.2f} em {} anos '.format(valor_casa, anos_pagar,),end='')
print('Será necessário pagar {:.2f} mensais'.format(prestação))
print(calculo)
if calculo >= 30.0:
    print('Aprovado!')
else:
    print('Recusado!')
print('fim')








