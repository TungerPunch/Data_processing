import matplotlib.pyplot as plt

from random_walk import RandomWalk
"""Программа визуализирует случайное блуждание"""

#Новые блуждания строяться пока программа остается активной
while True:
    #Построение случайного блуждания и нанесение точек на диаграмму
    rw = RandomWalk(1000)
    rw.fill_walk()
    #Назначаем размер области просмотра
    plt.figure(figsize=(10, 6))
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=15)
    #Выделение первой и последней точки
    plt.scatter(0, 0, c='green', edgecolors='none', s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)
    #Удаление осей
    plt.axis('off')
    #plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
plt.savefig('random_walk.png')
