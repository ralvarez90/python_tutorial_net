"""GENERATORS

Normalmente, Python ejecuta una función normal de arriba a abajo según el modelo 
de ejecución hasta su finalización. Ver ejemplo 01.

Para pausar una función a mitad de camino y reanudarla desde donde se pausó, 
se utiliza la declaración yield (producir).

Cuando una función contiene una sentencia yield, decimos que dicha función
o método es un generador.

Por definición, un generador es una función que contiene al menos una 
declaración yield y cuando llamas a una función generadora, devuelve 
un nuevo objeto generador. Sin embargo, no inicia la función.

Los objetos generadores (o generadores) implementan el protocolo iterador. 
De hecho, los generadores son iteradores perezosos. Por lo tanto, para 
ejecutar una función generadora, se llama a la función incorporada next() 
en ella.
"""


class Util:

    @staticmethod
    def endApplication():
        input('\nPress any key to continue . . . ')


class Lesson:

    @staticmethod
    def showExample01():
        print("EXAMPLE 01. Use normal function")

        # ejemplo ejecución secuencial
        def greeting():
            print('Hi')
            print('How are you?')
            print('Are you there?')

        # invocación
        greeting()
        print()

    @staticmethod
    def showExample02():
        print('EXAMPLE 02. Use generator function')

        # create a generetor funcion
        def greeting():
            print('Hi!')
            yield 1
            print('How are you?')
            yield 2
            print('Are you there?')
            yield 3

        # obtenemos generador
        messenger = greeting()
        for _ in range(3):
            element = next(messenger)
            print(element)
        print()

    @staticmethod
    def showExample03():
        print('EXAMPLE 03. Using generators to create iterators')

        def squares(length: int):
            for n in range(length):
                yield n**2

        length = 5
        square = squares(length)
        for s in square:
            print(s)
        print()

    @staticmethod
    def main():
        Lesson.showExample01()
        Lesson.showExample02()
        Lesson.showExample03()


if __name__ == '__main__':
    Lesson.main()
    Util.endApplication()
