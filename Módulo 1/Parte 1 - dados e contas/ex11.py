""" 
Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e 
a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados. 

Dica: tipos de print usando format
"""

# Variáveis
l = float(input('Largura = '))
a = float(input('Altura = '))

# Info extra
area = a * l
qtde_tinta = area / 2

# Print 1
print(
f'''
Dimensão da parede: {l} m X {a} m 
Área: {area} m² 
Quantidade de tinta: {qtde_tinta} litros
''')

# Print 2
# print('\nDimensão da parede: {} m X {} m \nÁrea: {} m² \nQuantidade de tinta: {} litros'.format(l, a, area, qtde_tinta))