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


def cabecalho(txt):
    print(linha())
    print()
    print(txt.center(40))
    print()
    print(linha())


def menu(lista):
    cabecalho("\033[0;36mCYBERVERIFY\033[0m")
    c = 1
    for item in lista:
        print(f"{c} - {item}")
        c += 1
    while True:
        opc = leiaOpc("\033[0;94mChoose an option:\033[0m ")
        if 1 <= opc <= len(lista):
            return opc
        print("\033[0;31mPlease enter a valid option.\033[0m")

    