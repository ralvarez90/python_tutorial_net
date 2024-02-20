"""STRINGS

Instancias de la clase str, son secuencias de caracteres 
bajo el estandard utf8. Son indexables, iterables e inmutables.
"""


def getLastChr(content: str) -> str:
    assert content != '' and content is not None, 'content string can not be empty or None'
    return content[-1]


def getHead(content: str) -> str:
    assert content != '' and content is not None, 'content string can not be empty or None'
    return content[0]


def getTail(content: str) -> str:
    assert content != '' and content is not None, 'content string can not be empty or None'
    return content[1:]


def stringExampl1():
    msg1 = 'message1'
    msg2 = r'message2,\t esto es un "raw" string'
    msg3 = '''Esto es un texto multilínea:
    \rPermite escribir mucho texto...
    \rAdios!'''
    print(msg1)
    print(msg2)
    print(msg3)


def stringConcatExample():
    print('Hello' ' World!')
    print('Hello ' + 'World!')
    print(f'{"Hello"} {"World!"}')
    print('%s %s' % ('Hello', 'World!'))
    print('{} {}'.format('Hello', 'World!'))


def stringIndicesExample():
    message = 'hello_world'
    for i in range(len(message)):
        print(f'message[{i}] -> {message[i]}')


def stringSubstringsExample():
    str1 = 'Welcome to the Jungle'
    print(f'head: {getHead(str1)}')
    print(f'tail: {getTail(str1)}')
    print(f'last: {getLastChr(str1)}')


def main():
    # se ejecutan los ejemplos
    stringExampl1()
    stringConcatExample()
    stringIndicesExample()
    stringSubstringsExample()


if __name__ == '__main__':

    # run application
    main()

    # end message
    input('\nPress any key to continue. . . ')
