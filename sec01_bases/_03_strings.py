"""STRINGS

Instancias de la clase str, son secuencias de caracteres 
bajo el estandard utf8. Son indexables, iterables e inmutables.
"""


def getLast(content: str) -> str:
    assert content != '', 'content string can not be empty'
    return content[-1]


def getHead(content: str) -> str:
    assert content != '', 'content string can not be empty'
    return content[0]


def getTail(content: str) -> str:
    assert content != '', 'content string can not be empty'
    return content[1:]


def stringExample():
    msg1 = 'message1'
    msg2 = r'message2,\t esto es un "raw" string'
    msg3 = '''Esto es un texto multilínea:
    \rPermite escribir mucho texto...
    \rAdios!'''
    print(msg1)
    print(msg2)
    print(msg3)


def concatenacionEjemplo():
    # forma 1
    print('Hello' ' World!')

    # forma 2
    print('Hello ' + 'World!')


def accessingExample():
    message = 'hello_world'
    for i in range(len(message)):
        print(f'message[{i}] -> {message[i]}')


def substringsExample():
    str1 = 'Welcome to the Jungle'
    print(f'head: {getHead(str1)}')
    print(f'tail: {getTail(str1)}')
    print(f'last: {getLast(str1)}')


if __name__ == '__main__':

    # str
    stringExample()

    # concat
    concatenacionEjemplo()

    # accessing
    accessingExample()

    # substrings
    substringsExample()

    # end application
    input('\nPress any key to continue. . . ')
