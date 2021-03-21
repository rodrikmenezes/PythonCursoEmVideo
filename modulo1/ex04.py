""" 
Exercício Python 4: Faça um programa que leia algo pelo teclado e 
mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele. 
"""
# Entrada de dados
n = input('Digite algo: ')

# Tipo
print('\nTipo primitivo: ', type(n))

# É número?
print('É número? ', n.isnumeric())

# É texto?
print('É texto? ', n.isalpha())

# É alfanumérico?
print('É alfanumérico? ', n.isalnum())

# Está em maiúsculo?
print('Está em maiúsculo? ', n.isupper())

# Está em minúsculo?
print('Está em minúsculo? ', n.islower())

# Capitalizado?
print('Capitalizado? ', n.istitle())