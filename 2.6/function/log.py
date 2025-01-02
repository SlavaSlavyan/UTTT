def LOG(FILE,problem):

    import json
    import sys
    from datetime import datetime

    try:
        with open('log.json', 'r', encoding='utf-8') as file:
            log = json.load(file)
            
    except:
        log = []
        with open('log.json', 'w', encoding='utf-8') as file:
            json.dump(log, file, ensure_ascii=False, indent=4)

    now = datetime.now()
    time = now.strftime("%d/%m/%Y %H:%M")
    log.append(f'[{time}][{FILE}]: {problem}')

    with open('log.json', 'w', encoding='utf-8') as file:
        json.dump(log, file, ensure_ascii=False, indent=4)

    sys.exit()


