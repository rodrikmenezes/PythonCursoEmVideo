""" 
Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente 
de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa. 

OBS: Solução usando biblioteca math
"""

# Bibliotecas
from math import hypot, asin, degrees

# Entrada de dados
co = float(input('Inserir Cateto Oposto = '))
ca = float(input('Inserir Cateto Adjacente = '))

# Cálculo
hip = hypot(co, ca)
ang_1 = degrees(asin(co / hip))
ang_2 = degrees(asin(ca / hip))
soma_ang = ang_1 + ang_2

# Print
print('Hipotenusa = {:.2f}'.format(hip))
print('Ângulo 1 = {:.2f} graus'.format(ang_1))
print('Ângulo 2 = {:.2f} graus'.format(ang_2))
print('Soma ângulos = {:.2f}'.format(soma_ang))