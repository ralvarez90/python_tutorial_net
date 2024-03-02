"""CONJUNTOS

Son colecciones de datos únicos y sin orden. Donde cada elemento
es único. Los elementos dentro de un set deben ser inmutables, por
lo que no puede tener como elementos de un set diccionarios o listas.

Existencia (in, not in)
Empleamos el operador in para verificar la existencia o contención
de un elemento dentro de un set. 

Los sets al ser objetos tienen sus propios métodos y propiedades 
implementados.
- add
    Agrega un elemento al conjunto
    
- remove
    Elimina elemento lanzando excepción en caso de que el objeto a
    eliminar no exista dentro del conjunto.
    
- discard
    Elimina elemento si existe, no lanza excepción

- pop
    Elimina y retorna el último elemento dentro del diccionario.

- clear
    Elimina todos los elementos de un set.
    
- copy
    Obtiene una copia del conjunto.
    
Conjuntos congelados
Los frozenset son conjuntos inmutables a partir de otros conjuntos.

Los sets son iterables por lo que se puede obtener cada uno de sus
objetos mediante un ciclo for.
"""
import types


def runtime_type(obj: object) -> str:
    return str(type(obj))[8:-2]


def show_example_1():
    skills = {
        'Python Programming',
        'Databases',
        'Software Design',
    }

    print(f'skills: {skills}')
    print(runtime_type(skills))


def show_example_2():
    emptySet = set()
    emptyDict = {}
    print(f'emptySet : {emptySet}')
    print(f'emptyDict: {emptyDict}')


def show_example_3():
    caracteres = set('letter')
    print(f'caracteres: {caracteres}')


def show_example_4():
    rating = 1
    ratings = {1, 2, 3, 4, 5}
    print(f'1     in {ratings} ? {rating in ratings}')
    print(f'1 not in {ratings} ? {rating not in ratings}')


def show_example_5():
    skills = {'Python', 'Java', 'Perl'}
    skills.add('Go')
    skills.add('Rust')
    print(f'skills: {skills}')
    try:
        skills.remove('Rust')
    except KeyError:
        print('Elemento fuera de conjunto')

    if 'Java' in skills:
        skills.remove('Java')

    print(f'final skills: {skills}')
    skills.discard('Cobol')


def show_example_6():
    skills = {'Problem Solving', 'Algorithms', 'Python Programming'}
    while len(skills) != 0:
        removed = skills.pop()
        print(f'Eliminado: "{removed}", restantes -> {skills}')


def show_example_7():
    languages = {
        'python',
        'haskell',
        'java',
        'go',
        'rust',
    }
    print(f'languages: {languages}')
    languages.clear()
    print(f'languages: {languages}')


def show_example_8():
    skills = {'Python programming', 'Problem solving', 'Design patterns'}
    skills.add('Django')
    skills = frozenset(skills)
    print(f'type of {skills} -> {runtime_type(skills)} ')
    # skills.add('REST Framework') lana error


def show_example_9():
    languages = {
        'python',
        'haskell',
        'java',
        'go',
        'rust',
    }

    for lang in languages:
        print(f'- {lang}')

    for index, value in enumerate(languages, start=1):
        print(index, value)


def main():
    show_example_1()
    show_example_2()
    show_example_3()
    show_example_4()
    show_example_5()
    show_example_6()
    show_example_7()
    show_example_8()
    show_example_9()


if __name__ == '__main__':
    # run application
    main()

    # end message
    input('\nPress any key to continue . . .')
