import pandas as pd
import os
import glob

def averager(rootdir, pattern):
    '''
    Усредняет все значения для каждой координаты для файлов
    '''
    # Открываем файлы по паттерну, добавляем каждый датафрейм в список.
    files = []
    for filepath in glob.glob(os.path.join(rootdir, pattern)):
        data = pd.read_csv(filepath,
                           sep='\s+',
                           header=None,
                           index_col=0)
        files.append(data)
    # Соединяем файлы в один датафрейм
    result_data = pd.concat(files, axis=1, ignore_index=True)
    result_data = pd.DataFrame(result_data.mean(axis=1))
    result_data.columns = [1]
    return result_data