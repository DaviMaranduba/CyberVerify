import menu
import analysis
from time import sleep


while True:
    option = menu.menu(["[bold white]Analyze a message[/]", "[bold dim]Exit[/]"])
    if option == 1:
        print("...")
        sleep(1)
        message = input("\033[0;36mType the message to analyze:\033[0m ")
        result = analysis.get_risk_level(message)
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
