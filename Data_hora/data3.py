from datetime import datetime

d = datetime.now()

# formatando data e hora
# strftime e strptime

data_hora_atual = datetime.now()
data_hora_str = '2025-11-18 10:20'
mascara_ptbr = '%d/%m/%y'
mascara_en = '%Y-%m-%d %H:%M' # usar Y para ano com 4 digitos e y para anos com 2 digitos

print(data_hora_atual.strftime(mascara_ptbr))


# uso do strptime
# converte uma data string em um objeto datetime

data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)