"""PARÁMETROS

Las funciones en python pueden recibir diversos parámetros.

1. defaut parameters
Son parámetros con valor default asignado.

2. keyword paramters
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


def main():
    # ejemplo 1, uso de valor default default
    mensaje = agradecer('Rodrigo')
    print(mensaje)

    # ejemplo 2, parametros posiciobales requeridos
    mensaje = agradecer('Rodrigo', 'Hola')
    print(mensaje)

    # ejemplo 3, parametros con nombre
    mensaje = agradecer(mensaje='Bienvenido', nombre='Rodrigo')
    print(mensaje)


if __name__ == '__main__':

    # run application
    main()

    # end message
    input('\nPress any key to continue . . . ')
