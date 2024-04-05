"""MÁS SOBRE ENUMERACIONES

Por definición, los miembros de una enumeración son únicos, sin
embargo puede crear diferetes nombres de miembros con un mismo
valor asignado. Cuando esto ocurre python no crea diferentes miembros
dentro de la enumerasión, solo crea diferentes alias de miembros 
para el mismo valor.

Si dos o más miembros dentro de una enumeración tienen el mismo valor
asignado, el primero será el principal y los demás serán
alias de ese principal.

Si se itera une enumeración con miembros alias, se iteran solo los
miembros principales.

Para obtener todos los miembros dentro de una enumeración incluyendo
los alias, empleamos la propieadad __member__ de dicha clase que
extiende a Enum.

El decorador @enum.unique se emplea para definir una enumerasión
sin alias.
"""
import enum
import json
from enum import Enum, auto


class ResponseStatus(Enum):
    PENDING = 'pending'
    FULFILLED = 'fulfilled'
    REJECTED = 'rejected'


class EstatusRespuesta(Enum):
    # en progreso
    IN_PROGRESS = 1
    REQUESTING = 1
    PENDING = 1

    # completado
    SUCCESS = 2
    OK = 2
    FULFILLED = 2

    # error
    ERROR = 3
    NOT_OK = 3
    REJECTED = 3


class Color(Enum):
    RED = 1
    CRIMSON = 1
    SALMON = 1
    GREEN = 2
    BLUE = 3


@enum.unique
class Day(Enum):
    MON = 'Monday'
    TUE = 'Tuesday'
    WED = 'Wednesday'
    THU = 'Thursday'
    FRI = 'Friday'
    SAT = 'Saturday'
    SUN = 'Sunday'


def showExample01():
    response = '''{
        "status":"fulfilled"   
    }'''

    # obtenemos diccionario con respuesta
    data = json.loads(response)
    status = data['status']

    try:
        if ResponseStatus(status) is ResponseStatus.FULFILLED:
            print('The request completed successfully')
    except ValueError as error:
        print(error)


def showExample02():
    print(f'Color enumeration:')
    print(Color.RED is Color.CRIMSON)
    print(Color.SALMON is Color.SALMON)


def showExample03():
    print('Main Color(1) is: ', Color(2))
    for c in Color:
        print(f'{c}', end=', ')
    print()


def showExample04():
    print(f'Color.__members__ : {Color.__members__}')


def showExample05():
    code = 'OK'
    if EstatusRespuesta[code] is EstatusRespuesta.SUCCESS:
        print('The request completed successfully')


def showExample06():
    for day in Day:
        print(day, end=', ')
    print()


def main():
    showExample01()
    showExample02()
    showExample03()
    showExample04()
    showExample05()
    showExample06()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
