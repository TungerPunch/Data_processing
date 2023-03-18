import pygal

from die import Die

#Создание кубиков
die1 = Die(6)
die2 = Die(10)
#Моделируем броски с сохранение результата в списке
results = []
for roll_num in range(5000000):
    result = die1.roll() + die2.roll()
    results.append(result)

#Анализ результатов
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result +1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Визуализация результатов
hist = pygal.Bar()
hist.title = "Результаты 1000 бросков D " + str(die1.num_sides) +\
             " и D" + str(die2.num_sides) + " 50000 раз."
hist.x_labels = [str(x) for x in list(set(results))]
hist.x_title = "Результаты"
hist.y_title = "Частота результатов"

hist.add("D " + str(die1.num_sides) +" и D " + str(die2.num_sides), frequencies)
hist.render_to_file('Броски кубиков\die_visual.svg')

