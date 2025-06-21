import subprocess
import traceback

VERS = "2.13.17 DEV"

try:
    loading = subprocess.Popen(['python', 'function\\loading.py'])
    loading_screen = True
except:
    print("$НЕТ ЭКРАНА ЗАГРУЗКИ!")
    loading_screen = False

try:

    from function.Main import Main

    UTTT = Main(VERS)

    if loading_screen:
        loading.terminate()

    while True:
        
        UTTT.main()

except Exception as err:

    try:
        UTTT.Log.write(f"Ошибка в основном цикле!\n\n{traceback.format_exc()}.","WARNING")
        UTTT.stop()
    except:
        print(f"Не удалось вывести ошибку в логи!\n\n{traceback.format_exc()}.")

    if loading_screen:
        loading.terminate()

    from function.Error import Error

    err_screen = Error()
    err_screen.main(traceback.format_exc())
