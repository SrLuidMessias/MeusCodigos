# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
nun1=int(input('digite o primeiro número:'))
nun2=int(input('digite o segundo número:'))
nun3=int(input('digite o terçeiro número:'))

if nun1<nun2 and nun1<nun3:
    print('o {} é o menor número!'.format(nun1))
if nun2<nun1 and nun2<nun3:
    print('o {} é o menor número!'.format(nun2))
if nun3<nun2 and nun3<nun1:
    print('o {} é o menor número!'.format(nun3))
if nun1>nun2 and nun1>nun3:
    print('o {} é o maior número!'.format(nun1))
if nun2>nun1 and nun2>nun3:
    print('o {} é o maior número!'.format(nun2))
if nun3>nun2 and nun3>nun1:
    print('o {} é o maior número!'.format(nun3))
print('fim')