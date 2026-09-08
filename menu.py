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
    