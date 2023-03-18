import glob
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import os

direc = 'E:\Рабочий стол\Учеба\Лазерная фотоника\L33182 18.10\L33182 18.10\\'
L = [13, 40, 60, 80, 100]
patterns = ['clean_x*.csv', 'clean_y*.csv']
#

for pattern in patterns:
    d = []
    for filepath in glob.glob(direc + 'clean_data\\' + pattern):
        data = pd.read_csv(filepath,
                           index_col=0)
        high_values = data.loc[data['0'] >= 0.135335283236612691]
        d.append(
                high_values.iloc[-1].name - high_values.iloc[0].name
                )
        
        
    # d(L)
    d = np.array(d).reshape(-1, 1)
    L = np.array(L).reshape(-1, 1)
    reg = LinearRegression().fit(L, d)
    d_new = reg.predict(L)
    #print(reg.predict(np.array(0).reshape(-1,1)))
    
    # Создание директории и составление пути
    graphpath = direc + 'Графики\\d_and_teta'
    graphname = 'd_' + pattern[6].upper() + '.png'
    if not os.path.exists(graphpath):
        os.makedirs(graphpath)
    graphpath = os.path.join(graphpath, graphname)
    # Построение графика
    abscissa = pattern[6].upper()
    plt.xlabel('L, см')
    plt.ylabel('$d_{}(L), мкм$'.format(abscissa))
    plt.plot(L, d_new)
    plt.scatter(L, d)
    plt.show()
    #plt.savefig(graphpath)
    plt.clf()    