from datetime import datetime
import pytz # biblioteca de fusos do mundo

# Usando a biblioteca
data_oslo = datetime.now(pytz.timezone('Europe/Oslo'))
print(data_oslo)

# Modo sem biblioteca(não recomendado)
# O uso de bibliotecas para simplificar códigos
#  é incentivado pelas boas práticas

# from datetime import datetime, timezone, timedelta

# data = datetime.now(timezone(timedelta(hours=2)))
# data_sp = datetime.now(timezone(timedelta(hours=3)))
# print(data_oslo)
# print(data_sp)