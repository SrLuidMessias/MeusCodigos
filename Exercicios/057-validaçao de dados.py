# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo=str(input('Digite seu sexo [M/F] :')).strip().upper()[0]
while sexo not in 'MmFf':  #< ---- enquanto sexo não tiver 'MmFf' .
    sexo=str(input('dado errado, digite seu sexo:')).strip().upper()[0]
print('sexo {} registrado com sucesso!! '.format(sexo))