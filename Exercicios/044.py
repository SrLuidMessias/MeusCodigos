# Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:

#   – à vista dinheiro/cheque: 10% de desconto
#   – à vista no cartão: 5% de desconto
#   – em até 2x no cartão: preço formal 
#   – 3x ou mais no cartão: 20% de juros
print('='*20,('LOJA MAGNO'),'='*20)
preço = int(input('Preço das compras: R$')) 
print(''' ESCOLHA
[1] à vista dinheiro/cheque:
[2] à vista no cartão:
[3] em até 2x no cartão:
[4] 3x ou mais no cartão: 
''')
esco = int(input('Digite:'))
if esco == 1 :
    total = preço - (preço *10 / 100)
    print('sua compra de {}, vai custar {} no final'.format(preço, total))
elif esco == 2 :
    total = preço - (preço * 5 / 100) 
    print('sua compra de {}, vai custar {}'.format(preço, total))
elif esco == 3 :
    total = preço
    parc3 = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parc3))
elif esco == 4 :
    total = preço + (preço * 20 / 100)
    conta = total 
    parc4 = int(input('Em quantas parcelas?'))
    totalparc = total / parc4
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parc4, totalparc ))

else:
    total = preço
    print('Opção invalida!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, total))
