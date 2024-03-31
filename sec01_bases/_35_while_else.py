"""WHILE ELSE

El bucle while puede tener al igual que un for una sentencia 
else que se ejecuta cuando la condición del while es falso.
"""


def show_example_01():
    basket = [
        {'fruit': 'apple', 'qty': 20},
        {'fruit': 'banana', 'qty': 30},
        {'fruit': 'orange', 'qty': 10}
    ]

    fruit = input('fruit: ')
    index = 0
    while index < len(basket):
        item = basket[index]
        if item['fruit'] == fruit:
            print(f'The basket has {item["qty"]} {item["fruit"]}(s)')
            break

        index += 1
    else:
        qty = int(input('Enter the qty for {fruit}'))
        basket.append({'fruit': fruit, 'qty': qty})
        print(basket)


def main():
    show_example_01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')
