class Scenes:

    def __init__(self,mainself):
        self.load_all(mainself)

    def load_all(self,mainself):

        _list = ["logo"]

        for class_id in _list:
            try: exec(f"from scenes.{class_id}.main import Main as Class{class_id}; self.{class_id} = Class{class_id}(mainself)")
            except Exception as error: print(f"Ошибка загрузки сцены при аргументе {class_id}: {error}")