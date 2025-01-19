import json

class File:

    def load(path):
        ЦФ

    def save(path,data):

        with open(f'{path}.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)