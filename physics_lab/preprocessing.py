import pandas as pd
import os
from averager import averager
from sklearn.preprocessing import MaxAbsScaler

rootdir = 'E:\Рабочий стол\Учеба\Лазерная фотоника\L33182 18.10\L33182 18.10\data'
# Вносим возможные паттерны
x_patterns = []
y_patterns = []
for i in range(1, 6):
    x_patterns.append('x.' + str(i) + '*')
    y_patterns.append('y' + str(i) + '*')
# Определяем шумы
shum_x = pd.read_csv(os.path.join(rootdir, '\data\shum x.dat'),
                     sep='\s+',
                     header=None,
                     index_col=0)

shum_y = pd.read_csv(os.path.join(rootdir, 'data\shum y.dat'),
                     sep='\s+',
                     header=None,
                     index_col=0)


for pattern in y_patterns:
    data = averager(rootdir, pattern).sub(shum_y)
    data['index'] = data.index * 8.9
    data = data.set_index('index')
    transformer = MaxAbsScaler().fit(data)
    data = pd.DataFrame(transformer.transform(data))
    data['index'] = data.index * 8.9
    data = data.set_index('index')
    data.to_csv(os.path.join(rootdir[:-5] + '\clean_data', 'clean_' + pattern[:-1] + '.csv'))
for pattern in x_patterns:
    data = averager(rootdir, pattern).sub(shum_x)
    data['index'] = data.index * 8.9
    data = data.set_index('index')
    transformer = MaxAbsScaler().fit(data)
    data = pd.DataFrame(transformer.transform(data))
    data['index'] = data.index * 8.9
    data = data.set_index('index')
    data.to_csv(os.path.join(rootdir[:-5] + '\clean_data', 'clean_' + pattern[:-1] + '.csv'))    
