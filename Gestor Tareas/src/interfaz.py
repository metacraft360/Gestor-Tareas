from src.gestor import tarea_nueva, mostrar_tareas

#interfaz programa aqui
def interfaz():
    diccionario_tareas = {}
    print("***BIENVENIDO AL GESTOR***\n")
    print("En este programa podras gestionar las distintas tareas que quieras realizar")
    elegir_accion = True
    while elegir_accion:
        try:
            accion = int(input("Estas son tus opciones dentro del menu\n(1)Mostrar tareas pendientes/(2)Mostrar tareas completadas/(3)Añadir tareas/(4)Eliminar tareas/(5)Salir del gestor\n"))
            if accion == 1:
                tarea_nueva(diccionario_tareas)
            elif accion == 2:
                mostrar_tareas(d)
            #elif accion == 3:
                #tarea_nueva(diccionario_tareas)
            #elif accion == 4:
            #elif accion == 5:
            #else:
                print("Elige un número entre 1-5")
        except ValueError:
            print("Elige un número entre 1-5")