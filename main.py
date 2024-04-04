import csv
import json
import os

class Estudiante:
    def __init__(self, id, nombre, apellido):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido

def leer_csv(nombre_archivo):
    estudiantes = []
    try:
        with open(nombre_archivo, newline='', encoding='utf-8') as archivo_csv:
            lector = csv.reader(archivo_csv)
            for row in lector:
                estudiante = Estudiante(row[0], row[1], row[2])
                estudiantes.append(estudiante)
    except FileNotFoundError:
        print("Error: El archivo no se encontró.")
    return estudiantes

def escribir_json(estudiantes, nombre_archivo):
    datos_json = []
    for estudiante in estudiantes:
        datos_json.append({
            "id": estudiante.id.strip(),
            "nombre": estudiante.nombre.strip(),
            "apellido": estudiante.apellido.strip()
        })
    
    nombre_archivo_json = os.path.splitext(nombre_archivo)[0] + ".json"
    with open(nombre_archivo_json, 'w', encoding='utf-8') as archivo_json:
        json.dump(datos_json, archivo_json, indent=4)
    
    print(f"El archivo JSON '{nombre_archivo_json}' se ha creado correctamente.")

def main():
    ruta_archivo_csv = input("Ingrese la ruta del archivo CSV: ")
    estudiantes = leer_csv(ruta_archivo_csv)
    if estudiantes:
        escribir_json(estudiantes, ruta_archivo_csv)

if __name__ == "__main__":
    main()
