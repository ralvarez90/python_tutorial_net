"""SENTENCIAS IF, ELIF, ELSE

Permite la toma de desiciones durante la ejecución
de un programa. Recibe una expresión booleana y
se puede anidar con elif y else.

El orden de andamiento es if, seguido por elif que es
una mezcla entre if-else y por último el else.
"""


def exampleIf():
    age = int(input('Enter your age: '))
    if age >= 18:
        print('You are elegible to vote.')


def exampleIfElse():
    age = int(input('Enter your age: '))
    if age >= 18:
        print('You are elegible to vote.')
    else:
        print('You are not elegible to vote.')


def exampleIfElifElse():
    age = int(input('Enter your age: '))
    if age < 5:
        ticketPrice = 5
    elif age < 16:
        ticketPrice = 10
    else:
        ticketPrice = 18
    print(f'You will pay ${ticketPrice} for the ticket')


def main():
    # ejemplo 1, if
    exampleIf()

    # ejemplo 2, if-else
    exampleIfElse()

    # ejemplo 3, if-elif-else
    exampleIfElifElse()


if __name__ == '__main__':

    # run app
    main()

    # end message
    input('\nPress any key to continue. . . ')
