import logging
import datetime
from pathlib import Path

class LogManager:
    
    def __init__(self):
    
        if not Path('data\\logs').exists():
            Path('data\\logs').mkdir(parents=True, exist_ok=True)
            
        if Path('data\\logs\\_last.log').exists():
            Path('data\\logs\\_last.log').unlink()
        
        logging.basicConfig(filename='data\\logs\\_last.log',level=logging.DEBUG,format='[%(asctime)s][%(levelname)s] %(message)s',datefmt='%H:%M:%S',encoding='utf-8')
        
        self.logs = []
        
    def write(self, text:str|list, str_type:str="INFO"):

        if not isinstance(text,list):
            text = [text]
            
        for line in text:

            line = str(line)
            
            if str_type == "DEBUG":
                logging.debug(line)
                
            elif str_type == "WARNING":
                logging.warning(line)
                
            elif str_type == "ERROR":
                logging.error(line)
                
            elif str_type == "CRITICAL":
                logging.critical(line)
                
            else:
                str_type = "INFO"
                logging.info(line)
            
            formated_line = f"[{datetime.datetime.now().strftime('%H:%M:%S')}][{str_type}] {line}"
            print(formated_line)

            self.logs.append(formated_line)

    def save(self):

        save_file = f'data\\logs\\{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.log'
        
        if not Path('data\\logs').exists():
            Path('data\\logs').mkdir(parents=True, exist_ok=True)

            if Path(save_file).exists():
                Path(save_file).unlink()
        
        with open(save_file,"a",encoding='utf-8') as file:
            for line in self.logs:
                file.write(f"{line}\n")