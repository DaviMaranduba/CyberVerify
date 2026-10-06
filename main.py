import menu
import analysis
from time import sleep
from rich.panel import Panel
from rich.table import Table


while True:
    option = menu.menu(["[bold white]Analyze a message[/]", "[bold dim]Exit[/]"])
    if option == 1:
        with menu.console.status("[bold bright_cyan]CYBERVERIFY[/bold bright_cyan]", spinner="dots", ):
            sleep(1)
        message = menu.console.input("[bright_white]>Type the message to analyze<:[bright_white] ")
        analyzer = analysis.MessageAnalyzer(message)
        with menu.console.status("[bold bright_green]Scanning Risk", spinner="dots", ):
            result = analyzer.get_risk_level()
            sleep(3)
        menu.console.print(result)
        sleep(1)
        table = Table()
        table.add_column(":warning: Detected suspicious word", style="bold green on black", header_style="bold bright_red")
        for word in analyzer.found_words:
            table.add_row(word)
        menu.console.print(Panel(table, title="[bold bright_cyan]Suspicious words:[/bold bright_cyan]", border_style="cyan"))
        sleep(1.5)
    elif option == 2:
        with menu.console.status("[orange1]Exiting the program...[/orange1]", spinner="dots", ):
            sleep(2)
        menu.console.print("[bold orange1]🛡️ Stay safe! Goodbye.🛡️[/bold orange1]")
        break
