from datetime import datetime # импорт библиотеки для отображения текущего времени
from pathlib import Path # работа с директориями

class Log: # этот класс необходим для создания логов. При желайнии его можно отключить в файле data\config.json
    
    def __init__(self,config: dict):
        
        self.config = config
        
        self.log = [f'\n=====[{datetime.now().strftime("%H:%M:%S")}][START]=====\n'] # массив со всеми строками лога
        print(self.log[0])
        
        if self.config['log'] != False:
            self.s("last",False)
    
    def w(self,text: str): # функция для записи новой строки в логи
        
        # принимает text как строчку лога
        
        if self.config['log'] != False: # если логирование разрешено
            
            end = False
            
            if text == '/$end$':
                string = f'\n=====[{datetime.now().strftime("%H:%M:%S")}][END]=====\n'
                end = True
            else:
                string = f"[{datetime.now().strftime("%H:%M:%S")}] {text}" # форматизация новой строки

            print(string)
            self.log.append(f"\n{string}")
            
            if self.config['log'] == "auto":
                self.s("last",False)
                if end:
                    self.endsave()
            elif end:
                self.s("last",True)
                self.endsave()

    def s(self,path: str,full: bool): # функция для сохранения лога в отдельный файл
        
        # Принимает path для пути сохранения файла и full как переключатель записи сохранения (true - весь файл, false - только последняя строчка)
        # [ВНИМАНИЕ!!!] функция не  создаёт директории! Используйте ТОЛЬКО уже существующие
        
        try:
            
            if full: # если надо сохранить весь файл
                
                with open(f"{path}.log", "a", encoding="utf-8") as file:
                    for string in self.log:
                        file.write(string)
                        
            else: # если надо сохранить только последнюю строчку
                
                with open(f"{path}.log", "a", encoding="utf-8") as file:
                    file.write(self.log[-1])
                    
        except: # если директория не найдена
            print(f"[ERROR] Failed to create/open file {path}.log")
    
    def endsave(self):
        
        if not Path("logs").exists():
            Path("logs").mkdir(parents=True)
    
        self.s(f"logs\\{datetime.now().strftime("%Y%m%d%H%M%S")}",True)