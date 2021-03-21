"""
Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

OBS: Solução utilizando biblioteca math
"""
# Importar bib
import math

# Entrada de dados
n = float(input('Digite um número racional = '))

# Cálculo
p_inteira = math.floor(n)
p_racional = n - p_inteira

# Print
print('\nParte racional = {:.4f} \nParte inteira = {:.0f}'.format(p_racional, p_inteira))