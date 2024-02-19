"""SENTENCIAS IF, ELIF, ELSE

Permite la toma de desiciones durante la ejecución
de un programa. Recibe una expresión booleana y
se puede anidar con elif y else.

El orden de andamiento es if, seguido por elif que es
una mezcla entre if-else y por último el else.
"""


def example_if_simple():
    age = int(input('Enter your age: '))
    if age >= 18:
        print('You are elegible to vote.')


def example_if_else():
    age = int(input('Enter your age: '))
    if age >= 18:
        print('You are elegible to vote.')
    else:
        print('You are not elegible to vote.')


def example_if_elif_else():
    age = int(input('Enter your age: '))
    if age < 5:
        ticket_price = 5
    elif age < 16:
        ticket_price = 10
    else:
        ticket_price = 18
    print(f'You will pay ${ticket_price} for the ticket')


def main():
    # ejemplo 1, if
    example_if_simple()

    # ejemplo 2, if-else
    example_if_else()

    # ejemplo 3, if-elif-else
    example_if_elif_else()


if __name__ == '__main__':

    # run app
    main()

    # end message
    input('\nPress any key to continue. . . ')
