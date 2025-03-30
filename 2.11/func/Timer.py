# класс для создания всех таймеров в игре
class Timer:

    def __init__(self, m):

        m.log.write('[DEBUG] Инициализация класса Func.Timer')
        m.log.write('[INFO] Запуск основного таймера')
        
        self.timers = {
            "main":{"act":1,"tick":0,"sec":0,"min":0}
        }
    
    def addtimer(self,m,name: str,act: int,time: any):

        if time == 0:
            time = (0,0,0)

        m.log.write(f'[INFO] Запуск таймера {name} с на нальным временем {time[2]}:{time[1]}:{time[0]} с условием {act}')

        self.timers[name] = {"act":act,"tick":time[0],"sec":time[1],"min":time[2]}
    
    def removetimer(self,m,name:str):

        try:

            m.log.write(f'[INFO] Остановка таймера {name} с конечным временем {self.timers[name]['min']}:{self.timers[name]['sec']}:{self.timers[name]['tick']}')

            del self.timers[name]

        except Exception as err:

            m.log.write(f'[ERROR] При отключении таймера {name} возникла ошибка, возможно таймера с таким id не существует')
    
    def main(self,m):

        for timer in self.timers.values():

            if m.Disp.fps == 0:
                sm = 100
            else:
                sm = m.Disp.fps
            timer['tick'] += timer['act']*100/sm
            
            if timer['tick'] >= 100:
                timer['tick'] -= 100
                timer['sec'] += 1
            
            if timer['tick'] <= -100:
                timer['tick'] += 100
                timer['sec'] -= 1
            
            if timer['sec'] >= 60:
                timer['sec'] = 0
                timer['min'] += 1
            
            if timer['sec'] <= -1:
                timer['sec'] = 59
                timer['min'] -= 1