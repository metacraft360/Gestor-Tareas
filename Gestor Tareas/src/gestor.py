#funciones programa aqui
import json
from pathlib import Path

def mostrar_tareas(diccionario_tareas):
    carpeta_src = Path(__file__).parent
    localizacion_json = carpeta_src / ".." / "datos" / "archivo.json"
    
    with open(localizacion_json,"r", encoding="utf-8") as archivo:
        diccionario_tareas = json.load(archivo)
    print (diccionario_tareas)
    
    

def tarea_nueva(diccionario_tareas):
    diccionario_tareas = {}

    diccionario_tareas["nombre"] = input("¿Cual será el nombre de la tarea?\n")

    print (f"El nombre de la tarea será {diccionario_tareas["nombre"]}")

    return diccionario_tareas #variable comun para el diccionario con las tareas


