"""
Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com X% de desconto.
"""

# Entrada de dados
valor = float(input('Digite o valor do produto R$ = '))
desc = float(input('Digita o percentual do desconto = '))

# Cálculo
valor_descontado = valor * (1 - desc / 100)

# Print
print(f'Valor com desconto = {valor_descontado:.2f}')