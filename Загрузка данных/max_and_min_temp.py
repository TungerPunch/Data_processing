import pandas as pd
import matplotlib.pyplot as plt
# Код работает для архива погоды с https://rp5.ru/
# Например new_data.csv

# Загрузка файла
filename = 'Загрузка данных\\Погода в Екатеринбурге 07.07.21-07.07.22.csv'
data = pd.read_csv(filename, sep=';', index_col=False, encoding='utf-16', engine='python')


# Правильный вывод даты, добавление даты без времени
data['Местное время'] = pd.to_datetime(data['Местное время'], format='%d.%m.%Y %H:%M')
data['Дата'] = data['Местное время'].dt.date

# Группировка по дате без времени
day_max_temperature = data.groupby(['Дата']).agg(temp_max=('T', 'max'))
day_min_temperature = data.groupby(['Дата']).agg(temp_max=('T', 'min'))
dates = day_max_temperature.index

# Нанесение данных на диаграмму
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, day_max_temperature, c='red', alpha=0.5)
plt.plot(dates, day_min_temperature, c='blue', alpha=0.5)
plt.fill_between(dates, day_max_temperature['temp_max'], day_min_temperature['temp_max'], facecolor='blue', alpha=0.3)

# Форматирование диаграммы
plt.title("Максимальная и минимальная дневные температуры в Екатеринбурге", fontsize=16)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Температура С$^\\circ$", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=12)

# Вывод диаграммы и сохранениe

#plt.show()
plt.savefig('Загрузка данных\\max_and_min_temp.png')
