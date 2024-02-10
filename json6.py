import json 

def agregar_alumno(alumnos, nombre, apellido, dni, fecha_nacimiento, tutor):
    alumno = {
        "Nombre": nombre,
        "Apellido": apellido,
        "DNI": dni,
        "Fecha de nacimiento": fecha_nacimiento,
        "Tutor": tutor,
        "Notas": [],
        "Faltas": 0,
        "amonestaciones": 0
    }
    alumnos.append(alumno)
    return alumnos

def iniciales(alumno, notas, faltas, amonestaciones):
    alumno["Notas"] = notas
    alumno["Faltas"] = faltas
    alumno["amonestaciones"] = amonestaciones

def mostrar_alumno(alumno):
    print("Datos del alumno:")
    for key, value in alumno.items():
        print(f"{key}: {value}")

def mostrar_alumnos(alumnos):
    for i in range(len(alumnos)):
        print(f"Alumno {i + 1}:")
        mostrar_alumno(alumnos[i])

def modificar_datos(alumno, notas=None, faltas=None, amonestaciones=None):
    if notas:
        alumno["Notas"] = notas
    if faltas:
        alumno["Faltas"] = faltas
    if amonestaciones:
        alumno["amonestaciones"] = amonestaciones
        
def expulsar_alumno(alumnos, alumno):
    alumnos.remove(alumno)
    print(f"Alumno {alumno['Nombre']} expulsado.")

def guardar(alumnos):
    with open("alumnos.json" , 'w') as archivoalumnos:
        json.dump(alumnos, archivoalumnos)

def cargar():
    try:
        with open("alumnos.json" , "r") as archivoalumnos:
            return json.load(archivoalumnos)
    except FileNotFoundError:
        return []

alumnos = cargar()

if not alumnos:
    alumnos = agregar_alumno(alumnos, "Estefania", "Guzman", "46532123", "19/11/1990", "Yolanda Jaime")
    alumnos = agregar_alumno(alumnos, "Carolina", "Reynaga", "25571412", "27/09/1985", "Cristina Lopez")

iniciales(alumnos[0], [4, 7, 6], 6, 2)
iniciales(alumnos[1], [9, 7, 6], 1, 0)

guardar(alumnos)

mostrar_alumnos(alumnos)

modificar_datos(alumnos[0], notas=[6, 8, 7], faltas=9, amonestaciones=4)

modificar_datos(alumnos[1], notas=[10, 5, 9], faltas=3, amonestaciones=1)

mostrar_alumnos(alumnos)

expulsar_alumno(alumnos, alumnos[0])

mostrar_alumnos(alumnos)
