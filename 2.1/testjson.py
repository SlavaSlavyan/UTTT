import json

# Открываем файл и читаем данные
with open('data\\settings.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Выводим массив на экран
print(data)
input()