''' Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)'''
c = soma = 0
n = int(input('Digite um número, [999] para parar:')) #<- ''ponto de partida'' sem esse comando o programa não funciona! (Name 'n' is nor defined)
while n != 999:
    c += 1
    soma += n
    n = int(input('Digite um número, [999] para parar:')) #<- com o comando aqui em baixo o prograva não poderá somar
print('Você digitou {} vezes e a soma deles é {}'.format(c, soma))# o 999 pois o programa acaba!
