# Эта игра была создана Святославом Моско как индивидуальный проект.
# Все легальные версии находятся в общем доступе на сайте GitHub https://github.com/SlavaSlavyan/UTTT

# Этот файл является основным фалом программы и отвечает за её запуск.

# Класс для вывода логов. Необходим для выявления ошибок.
class Log:
    
    def __init__(self):
        
        try: # Проверка возможности создания логов
            
            # Эти билиотеки нужны для взаимодействия с системой.
            from pathlib import Path
            import datetime
            
            self.Path = Path
            self.datetime = datetime
            
            self.logging = True # Разрешение на логирование
            
            # удаление последнего лога для создания нового
            if self.Path("Log\\last.log").exists(): 
                Path("Log\\last.log").unlink()
            
        except Exception as err:
            print(f"[WARNING] Не удалось включить логи! Ошибка: {err}.")
            self.logging = False # Запрет на логирование
            
        self.log = [] # Массив со всеми строками лога. После записи сохраняется как отдельынй файл.
    
    def write(self,text: str): # Функция для записи новой строчки лога
        
        # принимает text как строку и форматирует её для строчки лога
        
        try: # Пытаемся применить формат со временем системы
            string = f"[{self.datetime.datetime.now().strftime("%H:%M:%S")}] {text}"
            
        except:
            string = f"[ErrOfDateTime] {text}"
            
        print(string) # вывод чистой строки в терминал (не зависимо от логов, терминал выводит информацию всегда)
        
        # если логирование разрешено
        if self.logging:
            
            self.log.append(f"\n{string}") # добавление строчки в лог с разделяющим отступом
            
            # исключение на случай ошибки связанной с путём к файлу
            try: 
                
                # Если папка Log не существует, она будет создана
                if not self.Path('Logs').exists():
                    self.Path('Logs').mkdir(parents=True)
                
                path = "Logs\\last.log"
            
            except:
                path = "last (err of path).log"

            # авто сохранение логов в последний файл (последняя строчка)
            with open(path, "a", encoding="utf-8") as file:
                file.write(self.log[-1])
    
    def save(self): # функция для сохранения логов в отдельный файл
        
        # Если логирование разрешено
        if self.logging:
            
            try: # Исключение на случай ошибки записи
                
                # Если папка Log не существует, она будет создана
                if not self.Path('Logs').exists():
                    self.Path('Logs').mkdir(parents=True)
                
                # Сохранение целого массива логов в отдельный файл с уникальным именем.
                with open(f"Logs\\{self.datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.log", "w", encoding="utf-8") as file:
                    
                    # Запись построчная
                    for string in self.log:
                        file.write(string)
            
            except Exception as err:
                print(f"[WARNING] Не удалось сохранить логи! Ошибка: {err}.")

# Импортированиe библиотек
import pygame
import sys

# Основной класс программы
class Main:
    
    def __init__(self):
        
        # Создание экземпляра логов
        self.log = Log()
        self.log.write('[DEBUG] Инициализация основного класса и подготовка к запуску...')
        
        # Инициализация графического модуля PyGame
        pygame.init()
        
        # Эта переменная отвечает за инструкции по вводу от пользователя.
        # Проще говоря эта переменная обозначает где сейчас происходят события в игре.
        # Например meny, game, settings и подобное.
        self.status = 'logo'
        
        
    
    def start(self):
        
        self.log.write('[DEBUG] [WARNING] [ERROR] [FATAL] [TRACE] [INFO]')
        self.log.save()
    
    
UTTT = Main()

UTTT.start()