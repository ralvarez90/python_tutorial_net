"""ATRIBUTOS DE CLASE

Recordemos que un atributo puede ser cualquier objeto incluyendo
funciones.

Una atributo de clase es accesible de forma directa desde la clase
sin necesidad de generar instancias. Aunque si existen instancia
de dicha clase también se pueden acceder a todos las variables
de clase desde las instancias.

Recordemos que puede acceder a las variables de clase desde la clase
y desde las instancias de la forma:
objet_name.class_attribute
clase_name.class_attribute

Cuando accede a un atributo através de una instancia, python busca el
atributo en su diccionario de atributis __dict__, si no lo encuentra lo
busca en el diccionario de atributos de su respectiva clase.
"""


class Product:
    default_discount = 0

    def __init__(self, price: float) -> None:
        self.price = price
        self.discount = Product.default_discount

    def set_discount(self, discount: float):
        self.discount = discount

    def netprice(self) -> float:
        return self.price * (1-self.discount)


class Circle:
    # atributos de clase
    PI = 3.14159
    circles_list = []

    def __init__(self, radius: float = 0) -> None:
        assert radius >= 0, 'radius value cannot be a negative number'
        # atributos de instancia
        self.radius = radius

        # add the instance to the circle lsit
        self.circles_list.append(self)

    def area(self) -> float:
        return self.PI * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * self.PI * self.radius

    def __str__(self) -> str:
        return f'Circle{str(self.__dict__)}'


class Test:
    x = 10

    def __init__(self) -> None:
        self.x = 20


def show_example_1():
    c = Circle(radius=10)
    print(f'Circle area     : {c.area():.2f} u^2')
    print(f'Circle perimeter: {c.perimeter():.2f} u')

    # create some circles
    for r in range(1, 11):
        Circle(radius=10*r)

    # show all circles
    for c in Circle.circles_list:
        print(c)


def show_example_2():
    print(f'PI -> {Circle.PI}')


def show_example_3():
    test = Test()
    print(f'test.x = {test.x}')
    print(f'Test.x = {Test.x}')


def show_example_4():
    p1 = Product(2000)
    print(f'p1.netprice() -> ${p1.netprice():,.2f}')
    p2 = Product(2000)
    p2.set_discount(0.05)
    print(f'p2.netprice() -> ${p2.netprice():,.2f}')


def main():
    # run examples
    show_example_1()
    show_example_2()
    show_example_3()
    show_example_4()


if __name__ == '__main__':
    # run application
    main()

    # end message
    input('\nPress any key to continue . . .')
