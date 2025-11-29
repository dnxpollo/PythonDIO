from datetime import timedelta, datetime, date, time


##############################################################################

tipo_carro = {'p', 'm', 'g'}
tempo_p = 30
tempo_m = 40
tempo_g = 50
data_atual = datetime.now()

if tipo_carro == 'p':
    data_estimada = data_atual + timedelta(minutes=tempo_p)
    print(f'O carro chegou {data_atual} e a previsão para estar pronto é {data_estimada}')
elif tipo_carro == 'p':
    data_estimada = data_atual + timedelta(minutes=tempo_m)
    print(f'O carro chegou {data_atual} e a previsão para estar pronto é {data_estimada}')
else:
    data_estimada = data_atual + timedelta(minutes=tempo_g)
    print(f'O carro chegou {data_atual} e a previsão para estar pronto é {data_estimada}')



# pegando apenas um elemento da hora

print(date.today() - timedelta(days=1))

resultado = datetime(2025, 11, 18, 20, 20, 15) - timedelta(hours=1)
print(resultado.time())