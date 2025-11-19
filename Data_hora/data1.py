from datetime import date, datetime, time

data = date(2025, 11, 10) # data definida 
print(data)

print(date.today()) # data atual

# datetime
# objeto = date + time
# hora/minuto/segundo - diferença para o date
# muito importante em sites de compras ou eventos muito importantes.

data_hora = datetime(2025, 12, 1) # hora, minuto e segundo virá zerado pois as informações são opcionais
print(data_hora)

data_hora = datetime.today() # data e hora atual
print(data_hora)


hora = time(10, 20, 0) # hora definida
print(hora)

hora = time() # hora zerada
print(hora)
# criando data e hora

d = datetime(2025, 7, 19, 13, 45) # primeiro chama a biblioteca datetime e depois a classe
print(d) 