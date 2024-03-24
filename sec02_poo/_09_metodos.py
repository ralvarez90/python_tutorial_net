"""MÉTODOS

Son funciones asociadas a cada una de las instancias, las 
funciones normales son instancias de la clase function, mientras
que los métodos son diferentes.

Si un método de instancia se invoca desde la clase es tipo
function y si se invoca desde la intancia es un método.

Los métodos instancia se pueden invocar como métodos de clase,
pasando como argumento una instancia de dicha clase.

El primer argumento de un método de instancia es la referencia
al propio objeto que invoca, por convensión se suele nombrar
como self.
"""


def runtimeType(obj: object) -> str:
    return str(type(obj))[8:-2]


class Request:

    def send(*args):
        primero, *otros = args
        print(f'primero: {primero}')
        print(f'otros: {otros}')

    def enviar(self):
        pass


def showExample01():
    # generamos instancia
    req = Request()

    # mostramos tipos
    print(f'type(Request.enviar): {runtimeType(Request.enviar)}')
    print(f'type(Request.send)  : {runtimeType(Request.send)}')
    print(f'type(Request)       : {runtimeType(Request)}')

    # invocamos método
    req.send()
    Request.send(req)


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
