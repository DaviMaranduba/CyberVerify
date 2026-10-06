import menu
import analysis
from time import sleep
from rich.panel import Panel
from rich.table import Table


while True:
    option = menu.menu(["[bold white]Analyze a message[/]", "[bold dim]Exit[/]"])
    if option == 1:
        print("...")
        sleep(1)
        message = input("\033[0;36mType the message to analyze:\033[0m ")
        analyzer = analysis.MessageAnalyzer(message)
        result = analyzer.get_risk_level()
        menu.console.print("[white]>Scanning Risk...<[/white]")
        sleep(3)
        print(result)
        sleep(1)
        table = Table()
        table.add_column(":warning: Detected suspicious word", style="bold green on black", header_style="bold bright_red")
        for word in analyzer.found_words:
            table.add_row(word)
        menu.console.print(Panel(table, title="[bold bright_cyan]Suspicious words:[/bold bright_cyan]", border_style="cyan"))
        sleep(1.5)
    elif option == 2:
        print("...")
        sleep(2)
        menu.console.print("[orange1]Exiting the program...[/orange1]")
        sleep(2)
        menu.console.print("[bold orange1]🛡️ Stay safe! Goodbye.🛡️[/bold orange1]")
        break
