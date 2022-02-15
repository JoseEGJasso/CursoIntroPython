def main():
    try:
        cont = open('config.txt')
    except FileNotFoundError:
        print("No se encontró el archivo")
    except IsADirectoryError:
        print("config.txt es un directorio, no un archivo")
    except PermissionError:
        print("No tienes permisos para abrir este archivo")


if __name__ == '__main__':
    main()