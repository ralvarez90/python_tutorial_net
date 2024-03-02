"""STRINGS

Instancias de la clase str, son secuencias de caracteres 
bajo el estandard utf8. Son indexables, iterables e inmutables.
"""


def get_last_char(content: str) -> str:
    assert content != '' and content is not None, 'content string can not be empty or None'
    return content[-1]


def get_head(content: str) -> str:
    assert content != '' and content is not None, 'content string can not be empty or None'
    return content[0]


def get_tail(content: str) -> str:
    assert content != '' and content is not None, 'content string can not be empty or None'
    return content[1:]


def show_example_1():
    msg1 = 'message1'
    msg2 = r'message2,\t esto es un "raw" string'
    msg3 = '''Esto es un texto multilínea:
    \rPermite escribir mucho texto...
    \rAdios!'''
    print(msg1)
    print(msg2)
    print(msg3)


def show_example_2():
    print('Hello' ' World!')
    print('Hello ' + 'World!')
    print(f'{"Hello"} {"World!"}')
    print('%s %s' % ('Hello', 'World!'))
    print('{} {}'.format('Hello', 'World!'))


def show_example_3():
    message = 'hello_world'
    for i in range(len(message)):
        print(f'message[{i}] -> {message[i]}')


def show_example_4():
    str1 = 'Welcome to the Jungle'
    print(f'head: {get_head(str1)}')
    print(f'tail: {get_tail(str1)}')
    print(f'last: {get_last_char(str1)}')


def main():
    show_example_1()
    show_example_2()
    show_example_3()
    show_example_4()


if __name__ == '__main__':
    # run application
    main()

    # end message
    input('\nPress any key to continue. . . ')
