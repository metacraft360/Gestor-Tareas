from src.gestor import tarea_nueva, mostrar_tareas, eliminar_tarea

#interfaz programa aqui
def interfaz():
    lista_tareas = []
    diccionario_tareas = {}
    print("***BIENVENIDO AL GESTOR***\n")
    print("En este programa podras gestionar las distintas tareas que quieras realizar")
    elegir_accion = True
    while elegir_accion:
        try:
            accion = int(input("Estas son tus opciones dentro del menu\n(1)Mostrar tareas pendientes/(2)Añadir tareas/(3)Eliminar tareas/(4)Salir del gestor\n"))
            if accion == 1:
                mostrar_tareas(lista_tareas)
            elif accion == 2:
                tarea_nueva(lista_tareas,diccionario_tareas)
            elif accion == 3:
                 eliminar_tarea(lista_tareas)
            elif accion == 4:
                 elegir_accion = False
            else:
                print("Elige un número entre 1-5")
            pass            
        except ValueError:
            print("Elige un número entre 1-5")
