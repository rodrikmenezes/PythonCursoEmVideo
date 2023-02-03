"""
Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

OBS: Solução simples (sem uso de biblioteca)
"""

# Limpar terminal 
import os; os.system('cls')

# Entrada de dados
n = float(input('Digite um número racional = '))

# Cálculo
p_racional = n % 1
p_inteira = n // 1

# Print
print('\nParte racional = {:.4f} \nParte inteira = {:.0f}'.format(p_racional, p_inteira))