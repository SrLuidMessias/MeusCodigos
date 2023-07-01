# Refaça o DESAFIO 9, mostrando a tabuada de um número que o 
# usuário escolher, só que agora utilizando um laço for.
import emoji
print(emoji.emojize(':star:'*12))
print(emoji.emojize(':drop_of_blood:''TABUADA'':drop_of_blood:'))
print(emoji.emojize(':star:'*12))
nun=int(input('digite o número para a tabuada:')) # se colocar o input dentro do for, vai dar erro
for c in range(0, 11):
    print('{:2} X {:2} = {}'.format(nun, c, nun*c))

print('fim')
