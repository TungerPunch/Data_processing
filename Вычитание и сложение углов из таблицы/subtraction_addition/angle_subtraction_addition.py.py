import pandas as pd
import re
# Скрипт для рассчета разницы углов из таблицы


def totalseconds(minutes, seconds):
    return minutes * 60 + seconds

def subtr_angles(angle1: list, angle2: list):
    minutes1, seconds1 = map(int, angle1)
    minutes2, seconds2 = map(int, angle2)
    
    if totalseconds(minutes1, seconds1) >= totalseconds(minutes2, seconds2):
        if seconds1 >= seconds2:
            result = [str(minutes1 - minutes2),
                      str(seconds1- seconds2)]
        else:
            result = [str(minutes1 - minutes2 - 1),
                      str(60 + seconds1- seconds2)]
    else:
        if seconds2 >= seconds1:
            result = ['-' + str(minutes2 - minutes1),
                      str(seconds2- seconds1)]
        else:
            result = [str(minutes2 - minutes1 - 1),
                      str(60 + seconds2- seconds1)]
    return result


def add_angles(angle1: list, angle2: list):
    minutes1, seconds1 = map(int, angle1)
    minutes2, seconds2 = map(int, angle2)
    
    return [minutes1 + minutes2 + (seconds1 + seconds2) // 60,
              (seconds1 + seconds2) % 60]
    
    

def angle_subtraction(file_name):
    # Вспомогательные переменные
    angles1 = []
    angles2 = []
    col_name_1 = 'Угол отклонения пучка\n в прямом ходе'
    col_name_2 = 'Угол отклонения пучка\n в обратном ходе'
    data = pd.read_excel(r"table.xlsx",
                         index_col='Обороты',
                         )
    
    # Вытаскиваем нужные цифры из строк и записываем их в angle1, angle2
    for i in data.index:
       angle = re.findall(r'\d+', str(data[col_name_1][i]))
       angle = list(map(int, angle))
       angles1.append(angle)
       angle = re.findall(r'\d+', str(data[col_name_2][i]))
       angle = list(map(int, angle))
       angles2.append(angle)
       
    
    difference = []
    # Рассчитываем разницу между углами
    for i in data.index:
        i = int(i)
        difference.append(subtr_angles(angles1[i], angles2[i]))
        difference[i] = '''{}' {}"'''.format(*difference[i])
    
    # Записываем значения разниц в таблицу
    
    data['Разница'] = difference
    
    return pd.DataFrame(data)


def angle_addition(file_name):
    # Вспомогательные переменные
    angles1 = []
    angles2 = []
    col_name_1 = 'Угол отклонения пучка\n в прямом ходе'
    col_name_2 = 'Угол отклонения пучка\n в обратном ходе'
    data = pd.read_excel(r"table.xlsx",
                         index_col='Обороты',
                         )
    
    # Вытаскиваем нужные цифры из строк и записываем их в angle1, angle2
    for i in data.index:
       angle = re.findall(r'\d+', str(data[col_name_1][i]))
       angle = list(map(int, angle))
       angles1.append(angle)
       angle = re.findall(r'\d+', str(data[col_name_2][i]))
       angle = list(map(int, angle))
       angles2.append(angle)
       
    
    difference = []
    # Рассчитываем разницу между углами
    for i in data.index:
        i = int(i)
        difference.append(add_angles(angles1[i], angles2[i]))
        difference[i] = '''{}' {}"'''.format(*difference[i])
    
    # Записываем значения разниц в таблицу
    
    data['Разница'] = difference
    
    return pd.DataFrame(data)


angle_subtraction(r'table.xlsx').to_excel(r'sub_new_table.xlsx')
angle_addition(r'table.xlsx').to_excel(r'add_new_table.xlsx')

