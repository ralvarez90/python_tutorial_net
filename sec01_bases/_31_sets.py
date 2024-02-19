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


def ejemplo_set_definicion():
    skills = {
        'Python Programming',
        'Databases',
        'Software Design',
    }

    print(f'skills: {skills}')
    print(runtime_type(skills))


def ejemplo_empty_set():
    empty_set = set()
    empty_dict = {}
    print(f'empty_set : {empty_set}')
    print(f'empty_dict: {empty_dict}')


def ejemplo_char_set():
    caracteres = set('letter')
    print(f'caracteres: {caracteres}')


def ejemplo_contension():
    rating = 1
    ratings = {1, 2, 3, 4, 5}
    print(f'1     in {ratings} ? {rating in ratings}')
    print(f'1 not in {ratings} ? {rating not in ratings}')


def ejemplo_agregar_remover_descartar():
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


def ejemplo_metodo_pop():
    skills = {'Problem Solving', 'Algorithms', 'Python Programming'}
    while len(skills) != 0:
        removed = skills.pop()
        print(f'Eliminado: "{removed}", restantes -> {skills}')


def ejemplo_metodo_clear():
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


def ejemplo_frozenset():
    skills = {'Python programming', 'Problem solving', 'Design patterns'}
    skills.add('Django')
    skills = frozenset(skills)
    print(f'type of {skills} -> {runtime_type(skills)} ')
    # skills.add('REST Framework') lana error


def ejemplo_for():
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
    ejemplo_set_definicion()
    ejemplo_empty_set()
    ejemplo_char_set()
    ejemplo_contension()
    ejemplo_agregar_remover_descartar()
    ejemplo_metodo_pop()
    ejemplo_metodo_clear()
    ejemplo_frozenset()
    ejemplo_for()


if __name__ == '__main__':

    # run application
    main()

    # end message
    input('\nPress any key to continue . . .')
