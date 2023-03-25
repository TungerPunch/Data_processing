import pandas as pd
import re
import numpy as np

data = pd.read_excel('table.xlsx', skiprows=[0,], index_col='Номер моды',)
data = data[[r'Jm', r'\theta_c', r'Jm.1', r'\theta c', ]]

for column in data.columns:
    column_data = pd.DataFrame(data[[column]])
    column_data[['grad', 'min']] = \
        column_data.iloc[:, 0].str.split('grad', expand=True)
    column_data['min'] = column_data['min'].str.rstrip('min').str.lstrip()
    column_data[['grad', 'min']] = column_data[['grad', 'min']].astype(float) 
    column_data['result'] = column_data['grad'] + column_data['min'] / 60
    data[column] = column_data['result']
    
data.to_excel('new_table.xlsx')