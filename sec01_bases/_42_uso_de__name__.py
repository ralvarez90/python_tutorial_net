"""USO DEL __name__

El __name__ es una variable especial en Python. Es especial porque 
Python le asigna un valor diferente dependiendo de cómo se ejecuta 
el script que lo contiene.

Cuando importa un módulo, Python ejecuta el archivo asociado con 
el módulo.

A menudo, desea escribir un script que pueda ejecutarse directamente 
o importarse como un módulo. La variable __name__ te permite hacer eso.

Cuando ejecuta el script directamente, Python establece la variable __name__ 
en '__main__', win embargo, si importa un archivo como módulo, Python establece el 
nombre del módulo en la variable __name__.
"""


def calculate_tax(price: float, tax: float) -> float:
    return price*tax


def print_billing_doc():
    taxrate = 0.1

    products = [
        {'name': 'Book', 'price': 39},
        {'name': 'Pen', 'price': 5},
    ]

    print(f'Name\tPrice\tTax')
    for p in products:
        tax = calculate_tax(p['price'], taxrate)
        print(f'{p["name"]}\t{p["price"]}\t{tax}')


def show_example():
    print_billing_doc()


def main():
    show_example()


# uso de __name__
if __name__ == '__main__':
    # run application
    main()

    # end message
    input('\nPress any key to continue. . .')
