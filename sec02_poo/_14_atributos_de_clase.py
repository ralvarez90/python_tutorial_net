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

    def get_netprice(self) -> float:
        return self.price * (1-self.discount)


class Circle:
    # atributos de clase
    PI = 3.14159
    circles = []

    def __init__(self, radius: float = 0) -> None:
        assert radius >= 0, 'radius value cannot be a negative number'
        # atributos de instancia
        self.radius = radius

        # add the instance to the circle lsit
        self.circles.append(self)

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


def showExample01():
    c = Circle(radius=10)
    print(f'Circle area     : {c.area():.2f} u^2')
    print(f'Circle perimeter: {c.perimeter():.2f} u')

    # create some circles
    for r in range(1, 11):
        Circle(radius=10*r)

    # show all circles
    for c in Circle.circles:
        print(c)


def showExample02():
    print(f'PI -> {Circle.PI}')


def showExample03():
    test = Test()
    print(f'test.x = {test.x}')
    print(f'Test.x = {Test.x}')


def showExample04():
    p1 = Product(2000)
    print(f'p1.netprice() -> ${p1.get_netprice():,.2f}')
    p2 = Product(2000)
    p2.set_discount(0.05)
    print(f'p2.netprice() -> ${p2.get_netprice():,.2f}')


def main():
    # run examples
    showExample01()
    showExample02()
    showExample03()
    showExample04()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
