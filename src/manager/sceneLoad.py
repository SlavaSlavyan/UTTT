class Scenes:

    def __init__(self,mainself):
        self.load(mainself,'logo')
        self.load(mainself,'menu')
    
    def load(self,mainself,class_id):

        try: 
            exec(f"from scenes.{class_id}.main import Main as Class{class_id}; self.{class_id} = Class{class_id}(mainself)")
            print(f'Загружена сцена {class_id}')
        except Exception as error: print(f"Ошибка загрузки сцены при аргументе {class_id}: {error}")