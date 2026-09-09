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




def linha(tam = 40):
    return "=" * tam


def cabecalho(txt):
    print(linha())
    print()
    print(txt.rjust(24))
    print()
    print(linha())


def menu(lista):
    cabecalho("CYBERVERIFY")
    c = 1
    for item in lista:
        print(f"{c} - {item}")
        c += 1
    while True:
        opc = leiaOpc("Choose an option: ")
        if 1 <= opc <= len(lista):
            return opc
        print("\033[0;31mPlease enter a valid option.\033[0;31m")

    