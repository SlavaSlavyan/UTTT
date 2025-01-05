import json

class Load:

    def read(path):
        with open(f'{path}.json', 'r', encoding='utf-8') as file:
            cofigurations = json.load(file)

        return cofigurations

    def write(data,path):
        with open(f'{path}.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)