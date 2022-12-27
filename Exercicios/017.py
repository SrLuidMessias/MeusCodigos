# faça um programa que leia o comprimento do cateto oposto
# e do cateto adjecente de um triângulo retângulo, calcule
# e mostre o comprimento da hipotenusa.
import math
co=float(input('comprimento do cateto oposto é:'))
ca=float(input('comprimeto do cateto adjecente é:'))
hi=math.hypot(co,ca)
print('a hipotenusa vai medir {:.2f}'.format(hi))
