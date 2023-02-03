""" 
Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente 
de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa. 

OBS: Solução sem uso de biblioteca
"""

# Limpar terminal 
import os; os.system('cls')

# Entrada de dados
co = float(input('Inserir Cateto Oposto = '))
ca = float(input('Inserir Cateto Adjacente = '))

# Cálculo
hip = (co ** 2 + ca ** 2) ** (1/2)

# Print
print('Hipotenusa = {:.2f}'.format(hip))