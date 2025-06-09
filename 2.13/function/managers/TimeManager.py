class TimeManager:
    
    def __init__(self,m):
        
        m.Log.write("Инициализация класса работы со временем.","DEBUG")
        
        self.timers = {}
    
    def main(self,m):
        
        for timer in self.timers.values():
            
            if m.Disp.fps != 0:
                timer['tick'] += 100/m.Disp.fps*timer['mod']
            
            if timer['mod'] > 0:
                
                if timer['tick'] >= 100:
                    timer['tick'] -= 100
                    timer['sec'] += 1
                
                if timer['sec'] >= 60:
                    timer['sec'] -= 60
                    timer['min'] += 1
            
            if timer['mod'] < 0:
                
                if timer['tick'] <= -100:
                    timer['tick'] += 100
                    timer['sec'] -= 1
                
                if timer['sec'] <= -1:
                    timer['sec'] += 60
                    timer['min'] -= 1 
    
    def start(self,m, name:str, start_value:tuple=(0,0,0), mod:int|float=1):
        
        m.Log.write(f"Задача таймера {name}...")
        
        if name in self.timers:
            m.Log.write(f"Не удалось создать таймер {name}. Таймер уже существует.","ERROR")
        else:
            self.timers[name] = {"min":start_value[0],"sec":start_value[1],"tick":start_value[2],"mod":mod}
            m.Log.write(f"Создан новый таймер {name}.")
    
    def stop(self,m, name:str):
        
        m.Log.write(f"Остановка таймера {name}...")
        
        if name in self.timers:
            del self.timers[name]
            m.Log.write(f"Таймер {name} остановлен.")
        
        else:
            m.Log.write(f"Не удалось остановить таймер {name}. Таймера не существует.","ERROR")