class Scenes:

    def __init__(self,mainself):
        pass
    
    def load_scene(self,mainself,id:str):
        
        try:
            exec(f"from scenes.{id}.main import Main as {id}; self.{id} = {id}(mainself)")
            print(f"Успешная загрузка сцены {id}")
        
        except Exception as error:
            print(f"Ошибка загрузки сцены {id}\n{error}")