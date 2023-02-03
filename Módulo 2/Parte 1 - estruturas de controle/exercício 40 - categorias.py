"""
Exercício Python 041: A Confederação Nacional de Natação precisa de um programa 
que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
"""

import datetime as dtm

nasc = int(input('Em que ano você nasceu? '))
atual = dtm.date.today().year
idade = atual - nasc

if idade <= 9:
    categoria = 'MIRIM'
elif idade > 9 and idade <= 14:
    categoria = 'INFANTIL'
elif idade > 14 and idade <= 19:
    categoria = 'JÚNIOR'
elif idade > 19 and idade <= 25:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'
    
print('\nIdade: {} \nCategoria do atleta: {}'.format(idade, categoria))


