"""PARÁMETROS

Las funciones en python pueden recibir diversos parámetros.

1. defaut parameters
Son parámetros con valor default asignado.

2. keyword paramters
Permitenn pasar valores a los argumentos empleando su nombre.
Esto permite cambiar el orden en el que se pasan al invicar.

3. Requeridos
Son los que obligatoriamente deben recibir un valor en el
parámetro.
"""


def agradecer(name: str, message: str = 'Hi'):
    """Retorna mensaje de agradecimiento.

    Args:
        name (str): nombre del destinatario
        message (str, optional): Mensaje a concatenar.

    Returns:
        str: String del agradecimiento completo.
    """
    return f'{message} {name}'


if __name__ == '__main__':

    # default
    agradecer('Rodrigo')

    # position parameters
    agradecer('Rodrigo', 'Hola')

    # keywords parametsrs
    agradecer(message='Bienvenido', name='Rodrigo')

    # end application
    input('\nPress any key to continue . . . ')
