"""GENERATORS

Normalmente, Python ejecuta una función normal de arriba a abajo según el modelo 
de ejecución hasta su finalización.

"""


class Util:

    @staticmethod
    def endApplication():
        input('\nPress any key to continue . . . ')


class Lesson:

    @staticmethod
    def showExample01():

        # ejemplo ejecución secuencial
        lambda _: (print('Hi!'))

    @staticmethod
    def main():
        Lesson.showExample01()


if __name__ == '__main__':
    Lesson.main()
    Util.endApplication()
