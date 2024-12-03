import json

def convert_colors_to_tuples(color_dict):
    # Создаем новый словарь для хранения результатов
    result = {}
    
    for color_name, rgb_string in color_dict.items():
        # Преобразуем строку в кортеж, разделяя по запятой и преобразуя в целые числа
        rgb_tuple = tuple(map(int, rgb_string.split(',')))
        result[color_name] = rgb_tuple
    
    return result

# Пример использования
json_data = '''
{
    "gray":"40, 44, 52",
    "darkgray":"51,56,66",
    "lightgray":"171,178,191",
    "secondlightgray":"92, 99, 112",
    "yellow":"229, 192, 123",
    "green":"152, 195, 121",
    "blue":"97, 175, 239",
    "orange":"198, 107, 60",
    "red":"194, 64, 52"
}
'''

# Загружаем JSON данные в словарь
color_dict = json.loads(json_data)

# Преобразуем цвета в кортежи
converted_colors = convert_colors_to_tuples(color_dict)

# Выводим результат
print(converted_colors)