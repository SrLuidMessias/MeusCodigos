# um professor quer sortear um dos seus quatro alunos para apagar o quadro,
# faça um programa que ajude ele, dando o nome deles e escrevendo o nome do ecolhido.
import random
n1=str(input('digite o nome do primeiro aluno:'))
n2=str(input('digite o nome do segundo aluno:'))
n3=str(input('digite o nome do terçeiro aluno:'))
n4=str(input('digite o nome do quarto aluno:'))
alunos=[n1, n2, n3, n4]
print('o aluno escolhido é {}'.format(random.choice(alunos)))
