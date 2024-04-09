"""SCOPE

Cuando asigna un objeto a una variable, la variable hara referencia
a ese objeto en memoria. Se dice que la variable está vinculada al
objeto.

Las variables almacenan referencias de objetos en memoria. Luego de
que una varible está vinculada a un objeto podemos acceder al objeto
en memorio usando el nombre de variable a lo largo de partes de
nuestro código.

La parte del código, en donde se está definido el nombre de variable
y la vinculación de dicha variable a un objeto se denomina scope
léxico.

Python almacena la vinculación entre variables/objetos en espacios
de nombres. Todo scope o alcance está dentro de un respectivo
espacio de nombres.

En Python la jearquía de scopes es de la forma:
built-in scope
    module scope
        nonlocal scope
            local scope
"""
