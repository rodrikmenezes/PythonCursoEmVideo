"""
Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""

# Biblioteca
from math import sin, cos, tan, radians

# Entrada de dados
ang_graus = float(input('Inserir ângulo = '))

# Converter radiandos
ang_rad = radians(ang_graus)

# Cálculos
seno = sin(ang_rad)
cosseno = cos(ang_rad)
tangente = tan(ang_rad)

# Prints
print('SENO = {:.2f}'.format(seno))
print('COSSENO = {:.2f}'.format(cosseno))
print('TANGENTE = {:.2f}'.format(tangente))
