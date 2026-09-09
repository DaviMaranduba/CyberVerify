import menu
import analysis
from time import sleep

option = menu.menu(["\033[0;37mAnalyze message\033[0m", "\033[0;37mExit\033[0m"])
if option == 1:
    menu.cabecalho("\033[0;36mMESSAGE ANALYSIS\033[0m")
    print("...")
    sleep(1)
    result = analysis.analyze()
    print("Scanning message...")
    sleep(1)
    print(result)