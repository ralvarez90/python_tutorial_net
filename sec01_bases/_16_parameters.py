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


def agradecer(nombre: str, mensaje: str = 'Hi'):
    """Retorna mensaje de agradecimiento.

    Args:
        nombre (str): nombre del destinatario
        mensaje (str, optional): Mensaje a concatenar.

    Returns:
        str: String del agradecimiento completo.
    """
    return f'{mensaje} {nombre}'


def show_example_01():
    # ejemplo 1, uso de valor default default
    mensaje = agradecer('Rodrigo')
    print(mensaje)

    # ejemplo 2, parámetros posicionales requeridos
    mensaje = agradecer('Rodrigo', 'Hola')
    print(mensaje)

    # ejemplo 3, parámetros con nombre
    mensaje = agradecer(mensaje='Bienvenido', nombre='Rodrigo')
    print(mensaje)


def main():
    show_example_01()


if __name__ == '__main__':
    # run application
    main()

    # end message
    input('\nPress any key to continue . . . ')
