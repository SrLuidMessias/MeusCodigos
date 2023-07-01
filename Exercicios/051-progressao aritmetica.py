#  Desenvolva um programa que leia o primeiro termo e a razão de uma PA(Progressão aritmética).
#  No final, mostre os 10 primeiros termos dessa progressão.
t=int(input('Primeiro Termo:'))
r=int(input('Razão:'))
decimo= t + (10 - 1) * r
for c in range(t, decimo + r, r):
    print('{}'.format(c), end=' ⇀  ')
print('fim')
