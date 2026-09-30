#funciones programa aqui
import json
from pathlib import Path
carpeta_src = Path(__file__).parent
localizacion_json = carpeta_src / ".." / "datos" / "archivo.json"

def mostrar_tareas(lista_tareas):
    lista_tareas = []
    with open(localizacion_json,"r", encoding="utf-8") as archivo:
        lista_tareas = json.load(archivo)

    if len(lista_tareas) <= 0:
        print("No tienes ninguna tarea creada, crea una para mostrarla en pantalla")
    else:
        print (lista_tareas)
    
    

def tarea_nueva(lista_tareas,diccionario_tareas):
    with open(localizacion_json, "r", encoding="utf-8") as archivo:
        lista_tareas = json.load(archivo)
        
    añadir_tareas = True
    while añadir_tareas:
        diccionario_tareas = {}
        diccionario_tareas["nombre_tarea"] = input("Nombre de la tarea\n")
        lista_tareas.append(diccionario_tareas)
        continuar_añadiendo = input("¿Quieres seguir añadiendo tareas?(s/n)")
        if continuar_añadiendo == "s":
            print("Añade otra tarea")
        elif continuar_añadiendo == "n":
            with open(localizacion_json, "w") as archivo:
                json.dump(lista_tareas, archivo, indent=4)
            añadir_tareas = False


def eliminar_tarea(lista_tareas):
    tarea_eliminar = {}
    with open(localizacion_json, "r", encoding="utf-8") as archivo:
        lista_tareas = json.load(archivo)
    print(f"Esta es tu lista de tareas\n{lista_tareas}")
    tarea_eliminar["nombre_tarea"] = input("Escribe el nombre de la tarea\n")
    for tarea in lista_tareas:
        tarea["nombre_tarea"] == tarea_eliminar["nombre_tarea"]
        if tarea_eliminar in lista_tareas:
            print(f"Se eliminara la tarea {tarea_eliminar['nombre_tarea']}")
            lista_tareas.remove(tarea)
            with open(localizacion_json,"w") as archivo:
                json.dump(lista_tareas, archivo, indent=4)
        else:
            print("No se ha encontrado ese archivo")
    
        
