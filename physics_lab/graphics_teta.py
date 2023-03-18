import glob
import pandas as pd
import matplotlib.pyplot as plt
import os
from math import atan

direc = 'E:\Рабочий стол\Учеба\Лазерная фотоника\L33182 18.10\L33182 18.10\\'
L = [13, 40, 60, 80, 100]
d_0 = 300
patterns = ['clean_x*.csv', 'clean_y*.csv']


for pattern in patterns:
    
    d = []
    d.append(d_0)
    
    for filepath in glob.glob(direc + 'clean_data\\' + pattern):
        data = pd.read_csv(filepath,
                           index_col=0)
        high_values = data.loc[data['0'] >= 0.135335283236612691]
        d.append(
                high_values.iloc[-1].name - high_values.iloc[0].name
                )
    # Рассчет тета
    teta = []
    L.insert(0, 0)
    for i in range(len(L)-1):
        value = 2 * atan(10**(-6)*(d[i+1] - d[i]) / (2*10**(-2)*(L[i+1] - L[i])))
        teta.append(value)
    L.remove(0)
    # Приближение
    teta_aver = sum(teta) / len(teta)
    teta_new = [teta_aver] * len(teta)
    # Создание директории и составление пути
    graphpath = direc + 'Графики\\d_and_teta'
    graphname = 'teta_' + pattern[6].upper() + '.png'
    if not os.path.exists(graphpath):
        os.makedirs(graphpath)
    graphpath = os.path.join(graphpath, graphname)
    # Построение графика
    abscissa = pattern[6].upper()
    plt.xlabel('L, см')
    plt.ylim(0, max(teta)*1.2)
    plt.ylabel('$\Theta_{}(L), рад$'.format(abscissa))
    plt.scatter(L, teta)
    plt.plot(L, teta_new)
    plt.savefig(graphpath, bbox_inches='tight')
    plt.clf()