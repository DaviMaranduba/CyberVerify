import menu
from analysis import analyze

option = menu.menu(["Analyze message", "Exit"])
if option == 1:
    menu.cabecalho("MESSAGE ANALYSIS")
    analyze()