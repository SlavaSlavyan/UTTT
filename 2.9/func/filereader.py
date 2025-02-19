import json

class File: # этот класс содержит функции для работы с внешними файлами формата json

    def load(path): # для чтения

        try:

            with open(f'{path}.json', 'r', encoding='utf-8') as file:
                data = json.load(file)

            return data
        
        except:

            print(f'[ERROR]: No such file or directory "{path}.json"')

            if path == 'config':

                data = {}
                File.save(path,data)

                print(f'[SOLUTION]: Created new file "{path}.json"')
    
    def save(path,data): # для записи

        with open(f'{path}.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)