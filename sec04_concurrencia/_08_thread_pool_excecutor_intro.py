"""THREAD POOL EXECUTOR

El manejo manual de threads no suele ser eficiente ya que crear y destruir
muchos threads frecuentemente es costoso en términos computacionales.

En lugar de hacerlo, es posible que desee reutilizar threds si espera 
ejecutar muchas tareas ad hoc en el programa. Un thread pool (grupo de
hilos) permite lograr esto.

Un thread pool es un patrón concurrente que permite administrar de forma
automática un grupo de threads de manera eficiente.

Workers
Cada thread dentro de pool se le denomina worker. Un grupo de hilos le permite 
reutilizar los threads de trabajo (workers) una vez que se completan las tareas. 

También protege contra fallas inesperadas, como excepciones.

Normalmente, un thread pool le permite configurar la cantidad de 
subprocesos y proporciona una convención de nomenclatura específica 
para cada subproceso de trabajo.

Para crear un thread pool, utiliza la clase ThreadPoolExecutor del 
módulo concurrent.futures.

Una vez que complete el trabajo con el ejecutor, debe llamar explícitamente 
al método Shutdown() para liberar el recurso retenido por el ejecutor. 

Para evitar llamar explícitamente al método Shutdown(), 
puede utilizar el administrador de contexto.
"""
