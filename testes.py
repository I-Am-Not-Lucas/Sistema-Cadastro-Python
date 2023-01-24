from datetime import date

data_pc = date.today()
data_inscricao = f'{data_pc.day} / {data_pc.month} / {data_pc.year}'
print(data_inscricao)