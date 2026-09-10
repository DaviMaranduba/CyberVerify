import menu
import analysis
from time import sleep

while True:
    option = menu.menu(["\033[0;37mAnalyze message\033[0m", "\033[0;37mExit\033[0m"])
    if option == 1:
        menu.cabecalho("\033[0;36mMESSAGE ANALYSIS\033[0m")
        print("...")
        sleep(1)
        result = analysis.analyze()
        print(">Scanning Risk...<")
        sleep(3)
        print(result)
        sleep(1.5)
    elif option == 2:
        print("...")
        sleep(2)
        print("\033[0;33mExiting the program...\033[m")
        sleep(2)
        print("\033[0;33m🛡️ Stay safe! Goodbye.🛡️")
        break
