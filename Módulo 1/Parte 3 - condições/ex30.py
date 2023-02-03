"""
Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""

# Limpar terminal 
import os; os.system('cls')

# Entrada
n = int(input('Digite um número inteiro qualquer: '))
# n = 11

# Cálculo/Saída
if n % 2 == 0:
    print(f'\033[1;34m{n} é PAR \033[0;0m')
else:
    print(f'\033[1;31m{n} é IMPAR \033[0;0m')