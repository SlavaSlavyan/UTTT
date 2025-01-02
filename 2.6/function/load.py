import json

class Config:

    def read():
        with open('function\\config.json', 'r', encoding='utf-8') as file:
            cofigurations = json.load(file)

        return cofigurations

    def write(data):
        with open('function\\config.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)