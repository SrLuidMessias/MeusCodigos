num = (int(input('Digite um valor:')),
       int(input('Digite outro valor:')),
       int(input('Digite mais um valor:')),
       int(input('Digite o último valor:')))
print(f'você digitou os valores {num}')
print(f'o valor 9 apareceu {num.count(3)} vezes')
if 3 in num:
    print(f'valor 3 está na {num.index(3)+1}ª posição')
else:
    print('número 3 não encontrado')
print('os valores pares foram ', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')