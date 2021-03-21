"""
Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

Dica: formatar casas decimais
"""

# Entrada de dados
real = float(input('Valor em R$ = '))
dolar = real * 5.7687

# Cálculo e print
print('\nO valor de R$ {} em dólar é U$ {:.2f}'.format(real, dolar))