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
            if self.Path("Logs\\last.log").exists(): 
                self.Path("Logs\\last.log").unlink()
            
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
    
    def err(text: str): # Экстренный вывод логов при фатальной ошибке
        
        # принимает text как строку и форматирует её для строчки лога 
            
        print(text) # вывод чистой строки в терминал (не зависимо от логов, терминал выводит информацию всегда)

        # авто сохранение логов в последний файл (последняя строчка)
        with open("err.log", "a", encoding="utf-8") as file:
            file.write(f"\n{text}")
 
try: # Исключение на случай ошибки импортирования
    
    # Импортированиe библиотек
    import pygame
    import sys
    
    # импортирование модулей 
    from func.JsonManager import JsonManager
    from display.main import Display
    from func.PlayerInput import PlayerInput
    
    run = True

except Exception as err:
    
    Log.err(f'[FATAL] Не удалось импортировать библиотеки! Ошибка:{err}')
    import traceback
    traceback.print_exc()
    run = False

# Основной класс программы
class Main:
    
    def __init__(self):
        
        # если в инициализации основного файла произойдёт ошибка, программа не запуститься и выдаст лог с причиной
        
        try:
            
            self.run = True # разрешение на запуск
        
            # Создание экземпляра логов
            self.log = Log()
            self.log.write('=====[START]=====\n')
            self.log.write('[DEBUG] Инициализация основного класса и подготовка к запуску...')
            
            # Инициализация модуля взаимодействия с файлами json и импортирование базовых настроек
            self.Manager = JsonManager(self)
            self.reloadconfig(True)
            
            # Эта переменная отвечает за инструкции по вводу от пользователя.
            # Проще говоря эта переменная обозначает где сейчас происходят события в игре.
            # Например meny, game, settings и подобное.
            self.status = 'logo'
            
            # Инициализация графического модуля PyGame
            pygame.init()
            
            self.Disp = Display(self)
            self.PI = PlayerInput(self)
            
            # базовые настройки
            pygame.display.set_caption(f"Ultimate Tic Tac Toe {self.config['vers']}")
            pygame.mouse.set_visible(True)
            
            self.log.write('[DEBUG] Инициализация основного класса прошла успешно.\n')
        
        except Exception as err:
            
            Log.err(f'[FATAL] Не удалось иициализировать основной класс программы! Ошибка: {err}')
            import traceback
            traceback.print_exc()
            self.run = False
        
    def start(self): # функция для старта программы
        
        self.log.write('[DEBUG] Запуск игры.')
        
        # Запуск основного цикла если есть разрешение
        while self.run:
            
            self.Disp.main(self) # отрисовка кадра
            
            self.PI.main(self) # обработка ввода
            
            pygame.display.flip() # обновление кадра (вывод)
            self.Disp.fps = self.Disp.clock.get_fps() # получение фпс
            self.Disp.clock.tick(self.config['max-fps']) # ограничение кадров в секунду соответствующее максимальному значению в cofig
            
        self.end()
    
    def reloadconfig(self,stop: bool) -> bool: # Загрузка информации из файла конфигурации
        
        # Принимает stop как указатель строгости. Если True, при ошибке программа будет остановленна.
        # Возвращает статус загрузки успешно/провально
        
        info = self.Manager.load(self,"data\\config")
        
        if not info[1]:
            
            self.log.write('[ERROR] Не удалось загрузить конфигурацию.')
            
            if stop:
                self.log.write('[WARNING] Высокая строгость загрузки. Запуск функции отключения игры.')
                self.end()
            else:
                self.log.write('[WARNING] Низкая строгость загрузки. Игнорирование проблемы может привести к экстренному отключению программы!')
                
        else:
            self.log.write('[INFO] Загружена конфигурация игры.')
            self.config = info[0]
        
        return info[1]
    
    def saveconfig(self,stop: bool) -> bool: # Сохранение определённых настроек
        
        # Принимает stop как указатель строгости. Если True, при ошибке программа будет остановленна.
        # Возвращает статус сохранения успешно/провально
        
        info = self.Manager.save(self,"data\\config",self.config)
        
        if not info:
            
            self.log.write('[ERROR] Не удалось сохранить конфигурацию.')
            
            if stop:
                self.log.write('[WARNING] Высокая строгость сохранения. Запуск функции отключения игры.')
                self.end()
            else:
                self.log.write('[WARNING] Низкая строгость сохранения. Игнорирование проблемы может привести к экстренному отключению программы!')
                
        else:
            self.log.write('[INFO] Сохранена конфигурация игры.')
        
        return info
    
    def end(self): # Функция для отключения программы
        
        self.log.write('[DEBUG] Отключение игры.\n')
        
        try:
            self.Manager.save(self,"data\\config",self.config)
            self.log.write('[INFO] Конфигурация успешно сохранена.')
        except:
            self.log.write('[ERROR] Не удалось сохранить конфиг при выключении.')
        
        self.log.write('=====[END]=====')
        self.log.save()
        
        pygame.quit()
        sys.exit()
    
# если запуск разрешен
if run:
    
    # Создание экзмпляра основного класса и запуск
    UTTT = Main()
    UTTT.start()