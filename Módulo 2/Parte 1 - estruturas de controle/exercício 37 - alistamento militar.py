"""
Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem 
e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço 
militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

import datetime as dtm

print('Informe sua data de nascimento: ')

# Entrada de dados
dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))

# Exemplo para testes
# dia = 14 ; mes = 9 ; ano = 1986

# Variaveis
data_nasc = dtm.datetime(ano, mes, dia)
data_atual = dtm.datetime.today()
diff = data_atual - data_nasc
diff = diff.days
idade_alist = 18*365
idade_info = diff // 365
criterio = diff - idade_alist

print('\nData de nascimento: ' + data_nasc.strftime('%d/%m/%Y'))

# Condicional
if criterio > 0:
    n_anos = criterio // 365
    n_meses = round((criterio / 365 - n_anos) * 12)
    print('\nMensagem: \nVocê já passou do tempo de se alistar!')
    print('\nIdade: {} anos. \nTempo passado: {} anos e {} meses'.format(idade_info, n_anos, n_meses))
else:
    criterio = abs(criterio)
    n_anos = criterio // 365
    n_meses = round((criterio / 365 - n_anos) * 12)
    print('\nMensagem: \nVocê deve se alistar no futuro!')
    print('\nIdade: {} anos \nFaltam {} anos e {} meses para data do alistamento'.format(idade_info, n_anos, n_meses))
