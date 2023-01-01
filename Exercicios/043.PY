#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice 
# de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#  – IMC abaixo de 18,5: Abaixo do Peso
#  – Entre 18,5 e 25: Peso Ideal               
#  – 25 até 30: Sobrepeso                       # divide o peso (em KG) pela altura (em metros) ao quadrado
#  – 30 até 40: Obesidade
#  – Acima de 40: Obesidade Mórbida
peso = float(input('Digite seu peso (KG) :'))
altura = float(input('Digite sua altura (M):'))
imc = peso / (altura * altura) # caso inverta para primeiro a multiplicação e depois a divisão, vai dar errado!!!
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc <= 25:
    print('peso ideal') 
elif 25 <= imc <=30:
    print('sobrepeso')
elif 30 <= imc <= 40:
    print('Obesidade')
else: 
    print('Obsidade mórbida')