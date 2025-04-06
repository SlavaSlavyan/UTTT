class Timer:

    def __init__(self, m):

        self.timers = {
            "main":{"act":1,"tick":0,"sec":0,"min":0}
        }
    
    def addtimer(self,m,name: str,act: int,time: any):

        if time == 0:
            time = (0,0,0)

        self.timers[name] = {"act":act,"tick":time[0],"sec":time[1],"min":time[2]}
    
    def removetimer(self,m,name:str):

        try:
            del self.timers[name]

        except:
            print(f'Timer {name} not exist')

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