from time import perf_counter, sleep
from concurrent.futures import ThreadPoolExecutor

"""THREAD POOL


Cada subproceso del grupo (Pool) se denomina subproceso de trabajo o trabajador. 
Un ThreadPool le permite reutilizar los subprocesos de trabajo una vez que se 
completan las tareas. También protege contra fallas inesperadas, como excepciones.

Un ThreadPool extiende de Executor y retorna un objeto Future. La clase Exceutor
tiene 3 mètodos para controlar el thread pool.
- submit
- map
- shutdown
"""


def task(id: int):
    print(f'starting the task {id}')
    sleep(1)


with ThreadPoolExecutor() as executor:
    f1 = executor.submit(task, 1)
    f2 = executor.submit(task, 1)
    print(f1.result())
    print(f2.result())
