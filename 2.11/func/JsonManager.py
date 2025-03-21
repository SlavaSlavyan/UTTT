import json
from pathlib import Path

# Класс для взаимодействия с json файлами
class JsonManager:
    
    def __init__(self,m):
        m.log.write('[DEBUG] Инициализация класса JsonManager')
    
    # функция для загрузки файла
    def load(self, m, path: str) -> list:
        
        # Принимает path как путь до файла
        # Возвращает list [информация полученная из файла (any), статус загрузки успешно/провально (bool)]
        
        m.log.write(f'[DEBUG] Импорт иформации из файла {path}.json')
        
        try:
            
            with open(f'{path}.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            m.log.write(f'[INFO] Файл {path}.json успешно загружен.')
            
            return [data,True]
        
        except Exception as err: # если не удалось загрузить файл
            
            m.log.write(f"[ERROR] Не удалось открыть файл {path}.json. Ошибка: {err}")
            return [None,False]

    # функция для сохранения файла
    def save(self, m, path: str, data: any) -> bool:
        
        # Принимает path как путь до файла и data как информацию, которую нужно сохранить
        # Возвращает boolean как статус загрузки успешно/провально
        
        m.log.write(f'[DEBUG] Сохранение информации в файл {path}.json')
        
        try:
            
            # если файла не существует
            if not Path(f'{path}.json').exists():
                
                m.log.write(f'[INFO] Файла {path}.json не существует, создаю новый.')
                
                Path(f'{path}.json').parent.mkdir(parents=True, exist_ok=True) # создание папки
                Path(f'{path}.json').touch() # создание самого файла
            
            with open(f'{path}.json', 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
                
            m.log.write(f'[INFO] Файл {path}.json успешно сохранён.')
                
            return True
                
        except Exception as err: # если не удалось сохранить файл
            
            m.log.write(f"[ERROR] Не удалось сохранить файл {path}.json. Ошибка: {err}")
            return False