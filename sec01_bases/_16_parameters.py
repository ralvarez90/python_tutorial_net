"""PARÁMETROS

Las funciones en python pueden recibir diversos parámetros.

1. default parameters
Son parámetros con valor default asignado.

2. keyword parameters
Permiten pasar valores a los argumentos empleando su nombre.
Esto permite cambiar el orden en el que se pasan al invocar.

3. Requeridos
Son los que obligatoriamente deben recibir un valor en el
parámetro.
"""


def greeting(nombre: str, mensaje: str = 'Hi'):
    """Retorna mensaje de agradecimiento.

    Args:
        nombre (str): nombre del destinatario
        mensaje (str, optional): Mensaje a concatenar.

    Returns:
        str: String del agradecimiento completo.
    """
    return f'{mensaje} {nombre}'


def showExample01():
    # ejemplo 1, uso de valor default default
    mensaje = greeting('Rodrigo')
    print(mensaje)

    # ejemplo 2, parámetros posicionales requeridos
    mensaje = greeting('Rodrigo', 'Hola')
    print(mensaje)

    # ejemplo 3, parámetros con nombre
    mensaje = greeting(mensaje='Bienvenido', nombre='Rodrigo')
    print(mensaje)


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
