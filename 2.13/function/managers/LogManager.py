import logging
import datetime
from pathlib import Path

class LogManager:
    
    def __init__(self):
    
        if not Path('data\\logs').exists():
            Path('data\\logs').mkdir(parents=True, exist_ok=True)
            
            if Path('data\\logs\\last.log').exists():
                Path('data\\logs\\last.log').unlink()
        
        logging.basicConfig(filename='data\\logs\\last.log',level=logging.DEBUG,format='[%(asctime)s][%(levelname)s] %(message)s',datefmt='%H:%M:%S',encoding='utf-8')
        
        self.logs = []
        
    def write(self, text:str|list, str_type:str="INFO"):
        
        if not isinstance(text,list):
            text = [text]
        
        for line in text:
            
            self.logs.append({"text":line,"type":str_type})
            
            if str_type == "DEBUG":
                logging.debug(line)
                
            elif str_type == "WARNING":
                logging.warning(line)
                
            elif str_type == "ERROR":
                logging.error(line)
                
            elif str_type == "CRITICAL":
                logging.critical(line)
                
            else:
                logging.info(line)
                str_type = "INFO"
                
            print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}][{str_type}] {line}")

    def save(self):
        
        if not Path('data\\logs').exists():
            Path('data\\logs').mkdir(parents=True, exist_ok=True)
        
        logging.basicConfig(filename=f'data\\logs\\{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.log')
        
        for line in self.logs:
            self.write(line['text'],line['type'])