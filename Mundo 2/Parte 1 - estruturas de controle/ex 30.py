"""
Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""

# Início
print('Informe: \n1) Valor da casa;\n2) Salário do comprador;\n3) Quantos anos para o pagamento.\n')

# Entrada de dados
valorCasa = float(input('Valor da casa: R$ '))
salario = float(input('Salário: R$ '))
tempo = int(input('Quantos anos para pagar: '))

# Teste
# valorCasa = 80000
# salario = 10000
# tempo = 7

# Cálculo
prestacao = valorCasa / (12 * tempo)
perc = prestacao / salario * 100

# Saída
print('\nPara pagar os R$ {:.2f} em {} anos, a prestação é de R$ {:.2f} (isso compromete {:.2f} % de sua renda)\n'.format(valorCasa, tempo, prestacao, perc))
if perc > 30:
    print('EMPRÉSTIMO NEGADO!')
else:
    print('EMPRÉSTIMO APROVADO!')

