"""MONKEY PATCHING

Técnica que permite modificar o extender el comportamiento de las
clases, métodos o funciones en tiempo de ejecución.

Básicamente consiste en cambiar o extender el comportamiento de una
clase sin necesidad de modificar directamente el código fuente.

Esto puede ser útil cuando requiera corregir un error en una biblioteca
externa, agregar funcionalidad adicional a una clase existente o
incluso realizar pruebas unitarias.

La función a emplear para modificar comportamiento 
"""


def showExample01():

    class Robot:
        def __init__(self, name: str) -> None:
            self.name = name

    def addSpeech(cls):
        cls.speak = lambda self, message: print(message)
        return cls

    # modificamos clase
    Robot = addSpeech(Robot)
    robot = Robot(name='Optimus Prime')
    robot.speak('Hi!')


def showExample02():

    def addSpeach(cls):
        cls.speak = lambda self, message: print(message)
        return cls

    @addSpeach
    class Robot:
        def __init__(self, name: str) -> None:
            self.name = name

    # creamos instancia
    bubblebe = Robot(name='Bubbleblee')
    bubblebe.speak('H!, soy amarillo!')


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
