import json

class File:

    def load(path):

        with open(f'{path}.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        return data
    
    def save(path,data):

        with open(f'{path}.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)