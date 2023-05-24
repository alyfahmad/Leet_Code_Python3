from datetime import datetime

cur= datetime.strptime('24-5-2023', '%d-%m-%Y').date().strftime('%d-%m-%Y')

cur_2= datetime(2022, 12, 28).date()

print(type(cur))
print(type(cur_2))
print(cur_2)
