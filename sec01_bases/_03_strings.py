"""STRINGS

Instancias de la clase str, son secuencias de caracteres utf8. Cada
elemento se puede obtener mediante índices. Otra característica es
que son inmutables e iterables.
"""


def getLastChar(content: str) -> str:
    assert content != '' and content is not None, 'content string can not be empty or None'
    return content[-1]


def getHead(content: str) -> str:
    assert content != '' and content is not None, 'content string can not be empty or None'
    return content[0]


def getTail(content: str) -> str:
    assert content != '' and content is not None, 'content string can not be empty or None'
    return content[1:]


def showExample01():
    msg1 = 'message1'
    msg2 = r'message2,\t esto es un "raw" string'
    msg3 = '''Esto es un texto multilínea:
    \rPermite escribir mucho texto...
    \rAdios!'''
    print(msg1)
    print(msg2)
    print(msg3)


def showExample02():
    print('Hello' ' World!')
    print('Hello ' + 'World!')
    print(f'{"Hello"} {"World!"}')
    print('%s %s' % ('Hello', 'World!'))
    print('{} {}'.format('Hello', 'World!'))


def showExample03():
    message = 'hello_world'
    for i in range(len(message)):
        print(f'message[{i}] -> {message[i]}')


def showExample04():
    str1 = 'Welcome to the Jungle'
    print(f'head: {getHead(str1)}')
    print(f'tail: {getTail(str1)}')
    print(f'last: {getLastChar(str1)}')


def main():
    showExample01()
    showExample02()
    showExample03()
    showExample04()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue. . . ')
