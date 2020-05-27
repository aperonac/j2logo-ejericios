def menu():
    print("Menu: ")
    print("[1] - Importar palabras clave.")
    print("[2] - Mostrar palabras clave.")
    print("[0] - Salir")


def elegirOpcion():
    opcion = 0
    while True:
        try:
            opcion = int(input("Opcion: "))
            if opcion in [0, 1, 2]:
                break
        except ValueError:
            print('ERROR: Introduzca un numero')
    return opcion


def carga_keywords():
    claves = []
    with open('keywords.txt') as f:
        for linea in f:
            claves += linea.split()
    return claves


def muestraKeywords(claves):
    vuelta = 1
    for contador, clave in enumerate(claves):
        if contador < 20 * vuelta:
            print(clave)
        else:
            input('Mostrar mas...')
            print(clave)
            vuelta += 1


def flujo():
    while True:
        menu()
        opcion = elegirOpcion()

        if opcion == 0:
            break
        elif opcion == 1:
            keywords = carga_keywords()
        elif opcion == 2:
            muestraKeywords(keywords)


if __name__ == '__main__':
    flujo()
