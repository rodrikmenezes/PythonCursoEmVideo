"""
Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, 
mostrando em seguida o primeiro e o último nome separadamente.
"""

# Limpar terminal 
import os; os.system('cls')

# Entrada
nome = input('Digite seu nome completo: ').strip().split()

# Saída
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome) - 1]))



