# Faça um programa que calcule a soma entre todos os números que são 
# múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1 # vai contar todos os números divisiveis por 3 
        soma += c # vai somar todos os valores multiplos de 3
print('a soma de todos os {} valores solicitados é {}'.format(cont, soma))