'''
Чертит графики для файлов из директории
'''

import glob
import pandas as pd
import matplotlib.pyplot as plt
import os

direc = 'E:\Рабочий стол\Учеба\Лазерная фотоника\L33182 18.10\L33182 18.10\\'
L = [13, 40, 60, 80, 100]

for index, filepath in enumerate(glob.glob(direc + 'clean_data\clean_y*.csv')):
    data = pd.read_csv(filepath,
                       index_col=0)
    graphname = filepath.replace(direc, '')
    graphname = graphname.replace('.csv', '_with_line.png')
    graphpath = direc + 'Графики'
    if not os.path.exists(graphpath):
        os.makedirs(graphpath)
    graphpath = os.path.join(graphpath, graphname)
    
    plt.plot(data, label='L = {} см'.format(L[index]))
    plt.xlabel('Y, мкм')
    plt.ylabel('I(Y)')
    plt.ylim(0, 1)
    #plt.savefig(graphpath)
    
y = [0.135335283236612691, 0.135335283236612691]
x = [0, 2127]
plt.plot(x, y, label = '$e^{-2}$')
plt.legend()
plt.savefig(direc + 'Графики\\Y.png')
plt.clf()


for index, filepath in enumerate(glob.glob(direc + 'clean_data\clean_x*.csv')):
    data = pd.read_csv(filepath,
                       index_col=0)
    graphname = filepath.replace(direc, '')
    graphname = graphname.replace('.csv', '_with_line.png')
    graphpath = direc + 'Графики'
    if not os.path.exists(graphpath):
        os.makedirs(graphpath)
    graphpath = os.path.join(graphpath, graphname)
    plt.plot(data, label='L = {} см'.format(L[index]))
    plt.xlabel('X, мкм')
    plt.ylabel('I(X)')
    plt.ylim(0, 1)
    #plt.savefig(graphpath)
    
y = [0.135335283236612691, 0.135335283236612691]
x = [0, data.index[-1]]
plt.plot(x, y, label = '$e^{-2}$')
plt.legend()
plt.savefig(direc + 'Графики\\X.png')
plt.clf()
