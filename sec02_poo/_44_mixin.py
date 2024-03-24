"""MIXIN

Un mixin es una clase que proporciona implementaciones de métodos para 
su reutilización por múltiples clases secundarias relacionadas. 
Sin embargo, la herencia no implica una relación es-un.

Un mixin no define un nuevo tipo. Por lo tanto, no está destinado 
a la creación de instancias, es una especie de interfaz.

Un mixin agrupa un conjunto de métodos para su reutilización. 
Cada mixin debe tener un único comportamiento específico, 
implementando métodos estrechamente relacionados.

Normalmente, una clase secundaria utiliza herencia múltiple 
para combinar las clases mixin con una clase principal.

Dado que Python no define una forma formal de definir clases 
mixin, es una buena práctica nombrar las clases mixin 
con el sufijo Mixin.
"""
import json


class Person:

    def __init__(self, name: str) -> None:
        self.name = name


class DictMixin:

    def toDict(self):
        return self._traverseDict(self.__dict__)

    def _traverseDict(self, attributes: dict):
        result = {}
        for k, v in attributes.items():
            result[k] = self._traverse(k, v)
        return result

    def _traverse(self, key, value):
        if isinstance(value, DictMixin):
            return value.toDict()
        elif isinstance(value, dict):
            return self._traverseDict(value)
        elif isinstance(value, list):
            return [self._traverse(key, v) for v in value]
        elif hasattr(value, '__dict__'):
            return self._traverseDict(value.__dict__)
        else:
            return value


class JSONMixin:

    def toJson(self) -> str:
        return json.dumps(self.toDict())


class Employee(DictMixin, JSONMixin, Person):
    def __init__(self, name: str, skills: list, dependents: dict) -> None:
        super().__init__(name)
        self.skills = skills
        self.dependents = dependents


def showExample01():
    from pprint import pprint
    e = Employee(
        name='John Wick',
        skills=['Karate', 'Guns', 'Kick Ass'],
        dependents={'wife': 'Mary Jane', 'children': ['Dog', 'Cat']}
    )
    print(e.toDict())
    print(e.toJson())


if __name__ == '__main__':
    showExample01()
    input('\nPress any key to continue . . .')
