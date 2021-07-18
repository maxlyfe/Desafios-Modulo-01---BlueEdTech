# 01 - Conversor de moedas

moeda_destino = str(input('Para qual moeda você deseja converter esse valor? ').capitalize().title().strip().replace(' ',''))
quantidade_moeda = float(input('Qual é o valor em reais que você deseja converter?\n R$ ').replace(',','.'))
dolar = quantidade_moeda/5.05
euro = quantidade_moeda/6.15
libra = quantidade_moeda/7.15
dolar_can = quantidade_moeda/4.18
peso_arg = quantidade_moeda/0.053
peso_chi = quantidade_moeda/0.0070
if moeda_destino == 'Dolar':
    print(f'O valor de R${quantidade_moeda} será de US${dolar:.2f}')
elif moeda_destino == 'Euro':
    print(print(f'O valor de R${quantidade_moeda} será de €{euro:.2f}'))
elif moeda_destino == 'Libra':
    print(print(f'O valor de R${quantidade_moeda} será de £{libra:.2f}'))
elif moeda_destino == 'Dolarcanadiense':
    print((f'O valor de R${quantidade_moeda} será de CAD{dolar_can:.2f}'))
elif moeda_destino ==  'Pesoargentino':
    print((f'O valor de R${quantidade_moeda} será de ${peso_arg:.2f}'))
elif moeda_destino == 'Pesochileno':
    print((f'O valor de R${quantidade_moeda} será de ${peso_chi:.2f}'))
else:
    print('Não esta definido o valor da diviça que você esta solicitando')
