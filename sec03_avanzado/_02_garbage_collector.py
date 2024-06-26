"""RECOLECTOR DE BASURA

Python gestiona la memoria de forma automática. Una vez que un objeto
deja de ser referenciado, sin embargo el conteo de referencias no 
siempre funciona de forma apropiada.

Por ejemplo, cuando tienes un objeto que hace referencia a sí mismo 
o dos objetos se hacen referencia entre sí. Esto crea algo llamado 
referencias circulares.

Cuando el Memory Manager no puede eliminar objetos con referencias 
circulares, provoca una pérdida de memoria.

Python permite interactuar de forma directa con el garbage collector
empleando el módulo gc.
"""
import gc
import ctypes


def refCount(idObj: int) -> int:
    return ctypes.c_long.from_address(idObj).value


def existsObject(idObj: int) -> bool:
    for object in gc.get_objects():
        if id(object) == idObj:
            return True
    return False


def showExample01():
    # primer clase
    class A:
        def __init__(self) -> None:
            self.b = B(self)
            print(f'A: {hex(id(self))}, B: {hex(id(self.b))}')

    # segunda clase
    class B:
        def __init__(self, a: A) -> None:
            self.a = a
            print(f'B: {hex(id(self))}, A: {hex(id(self.a))}')

    # deshabilitamos garbage collector
    gc.disable()

    # creamos instancia de clase A
    a = A()
    aId = id(a)
    bId = id(a.b)

    # mostramos contadores
    print(f'refCount(a): {refCount(aId)}')
    print(f'refCount(b): {refCount(bId)}')

    # chequeo de existencia de referencias
    print(f'objectExists(a): {existsObject(aId)}')
    print(f'objectExists(b): {existsObject(bId)}')

    # separador
    print('-'*50)

    # eliminamos objetos
    a = None
    print(f'refCount(a): {refCount(aId)}')
    print(f'refCount(b): {refCount(bId)}')

    # chequeo de existencia de referencias
    print(f'objectExists(a): {existsObject(aId)}')
    print(f'objectExists(b): {existsObject(bId)}')

    # ejecturamos recolector
    gc.collect()
    print('-'*50)

    # mostramos contadores
    print(f'refCount(a): {refCount(aId)}')
    print(f'refCount(b): {refCount(bId)}')

    # chequeo de existencia de referencias
    print(f'objectExists(a): {existsObject(aId)}')
    print(f'objectExists(b): {existsObject(bId)}')


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')
