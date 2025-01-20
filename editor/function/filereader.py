import json

class File:

    def load(path):

        with open(f'{path}.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    def save(path,data):

        pass