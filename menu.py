from rich.console import Group
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.console import Console

console = Console()
titulo = Text("CYBERVERIFY", style="bold bright_cyan")
subtitulo = Text("Suspicious Message Analyzer", style="dim")

conteudo = Group(
    Align.center(titulo),
    Align.center(subtitulo),
)

console.print(Panel(conteudo, border_style="cyan", padding=(1,4),))
def leiaOpc(msg):
    while True:
        try:
            n = int(input(msg))
        except TypeError:
            print("\033[0;31mInvalid data type. Please enter the correct type.\033[m")
        except ValueError:
            print("\033[0;31mInvalid value. Please enter a valid option.\033[m")
        except KeyboardInterrupt:
            print("\033[0;31mOperation cancelled by user.\033[m")
            return 0
        else:
            return n




def linha(tam = 32):
    return "\033[0;34m=\033[0m" * tam

def menu(lista):
    for c, item in enumerate(lista, start=1):
        console.print(f"[cyan]{c}[/cyan] - {item}")
    while True:
        opc = leiaOpc("\033[0;94mChoose an option:\033[0m ")
        if 1 <= opc <= len(lista):
            return opc
        print("\033[0;31mPlease enter a valid option.\033[0m")

    