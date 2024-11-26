import json

# Открываем файл и читаем данные
with open('data\\settings.json', 'r') as file:
    data = json.load(file)

# Выводим массив на экран
print(data)
input()