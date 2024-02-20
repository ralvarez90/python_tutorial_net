"""FUNCIONES PRIVADAS

Empleamdo _ o __ antes del nombre de una función, esta se 
marca como privada, es decir solo se usa en su módulo contenedor.

Otra forma de hacer que una función u objeto se privadao dentro de
un módulo es usar la variable __all__. De esta manera, no es necesario 
anteponer el nombre de la función con un guión bajo (_) para que 
sea privada.
"""

__all__ = [
    'funcionPublica'
]


def funcionPublica(email: str, message: str):
    print(f'Sending "{message}" to email "{email}"')


def funcionPrivada(filename: str):
    print(f'Attach {filename} to the message')
