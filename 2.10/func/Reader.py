import json

class Reader: # этот класс взаимодействует с json файлами
    
    def __init__(self):
        pass
    
    def load(self,path: str) -> any: # функция получения информации из файла
        
        # принимает path как путь до файла
        # [ВНИМАНИЕ!!!] функция не  создаёт директории! Используйте ТОЛЬКО уже существующие
        
        try:
            
            with open(f'{path}.json', 'r', encoding='utf-8') as file:
                data = json.load(file)

            return data # возврат иформации из файла
        
        except: # если директория не найдена
            print(f"[ERROR] Failed to open file {path}.json")
    
    def save(self,path: str,data: any):
        
        # принимает path как путь до файла куда будет загружена информация и data как загружаемую информацию
        # [ВНИМАНИЕ!!!] функция не  создаёт директории! Используйте ТОЛЬКО уже существующие
        
        try:
            
            with open(f'{path}.json', 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
                
        except: # если директория не найдена
            print(f"[ERROR] Failed to open file {path}.json")