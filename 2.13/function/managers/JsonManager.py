import json
from pathlib import Path

class JsonManager:
    
    def __init__(self,m):

        m.Log.write("Инициализация класса работы с JS.","DEBUG")
        
        m.config = self.load(m,"data\\config",True)

    def load(self, m, path:str, hard_mode:bool=False) -> any:

        m.Log.write(f"Загрузка инофрмации из файла {path}.json...")

        try:

            with open(f'{path}.json', 'r', encoding='utf-8') as file:
                data = json.load(file)

            m.Log.write(f"Загрузка прошла успешно! Полученная информация:\n{data}.")

            return data

        except Exception as err:

            m.Log.write(f'Не удалось загрузить файл {path}.json. Информация: {err}.',"ERROR")
            
            if hard_mode:
                m.Log.write(f'Жесткий режим. Отключение программы',"CRITICAL")
                m.stop()
            
            else:
                return "$err"
    
    def save(self, m, path:str, data:any, hard_mode:bool=False):

        m.Log.write(f"Сохранение информации в файл {path}.json... Информация:\n{data}.")

        try:
            
            if not Path(f'{path}.json').exists():

                m.Log.write(f"Создание нового файла {path}.json")
                Path(f'{path}.json').parent.mkdir(parents=True, exist_ok=True)
            
            with open(f'{path}.json', 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            
            m.Log.write(f"Сохранение прошло успешно!")

        except Exception as err:

            m.Log.write(f'Не удалось сохранить файл {path}.json. Информация: {err}.',"ERROR")
            
            if hard_mode:
                m.Log.write(f'Жесткий режим. Отключение программы',"CRITICAL")
                m.stop()
            
            else:
                return "$err"