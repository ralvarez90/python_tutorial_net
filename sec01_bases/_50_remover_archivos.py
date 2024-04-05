"""REMOVER ARCHIVOS

Empleamos la funcion os.remove para eliminar un archivo
desde python. Si no existe el archivo entnces lanza una
excepción FileNotFoundError por lo que se suele primero
verificar la existencia con os.exists.
"""
import os


def deleteFile(filename: str) -> bool:
    try:
        os.remove(filename)
    except Exception as error:
        print(error)
    else:
        return True
    return False


def showExample01():
    print(deleteFile('asdasd'))


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
