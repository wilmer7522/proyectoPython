import json
database = "python/info.json"

def abrirArchivo():
    with open('info.json', encoding="utf-8") as openfile:
        return json.load(openfile)

def guardarArchivo(miData):
    with open("info.json", "w") as outfile:
        json.dump(miData, outfile)

camper=[]

#def procesar_inscripcion(inscripciones):
    #campers = {}
    

    #camper.append(campers) # Agrega el nuevo estudiante a la lista de estudiantes
    # guardarArchivo(inscripciones)
    # print("Inscripción realizada exitosamente.")

def rutasEntrenamiento(camper):
    print("Rutas de entrenamiento")
    id_camper = input("Ingrese el ID del camper: ")
    camper_encontrado = None
    
    # Buscar el camper con el ID proporcionado dentro de las inscripciones
    for inscripcion in camper[0]["inscripciones"]:
        if str(inscripcion.get('id')) == id_camper:  # Convertir a cadena para comparar con entrada de usuario
            camper_encontrado = inscripcion
            break
    
    if camper_encontrado:
        print(f"ID: {camper_encontrado.get('id')}")
        print("1. Ruta NodeJS")
        print("2. Ruta Java")
        print("3. Ruta NetCore")
        ruta = input("Seleccione la ruta para este camper: ")
        if ruta == "1":
            camper_encontrado["rutaEntrenamiento"] = "Ruta NodeJS"
        elif ruta == "2":
            camper_encontrado["rutaEntrenamiento"] = "Ruta Java"
        elif ruta == "3":
            camper_encontrado["rutaEntrenamiento"] = "Ruta NetCore"
        else:
            print("Opción no válida, se asignará la Ruta NodeJS por defecto.")
            camper_encontrado["rutaEntrenamiento"] = "Ruta NodeJS"
        print("Asignación de ruta completada.")
        
        guardarArchivo(camper)  # Guardar cambios en el archivo JSON
    else:
        print("No se encontró ningún camper con el ID proporcionado.")

def registrarNotas(camper):
    print("Registro de notas")
    id_camper = input("Ingrese el ID del camper: ")
    inscripcion_encontrada = None
    
    # Buscar la inscripción con el ID proporcionado
    for inscripcion in camper[0]["inscripciones"]:
        if str(inscripcion.get('id')) == id_camper:  # Convertir a cadena para comparar con entrada de usuario
            inscripcion_encontrada = inscripcion
            break
    if inscripcion_encontrada:
        print(f"Inscripción encontrada para el ID: {id_camper}")
        nota_teorica = float(input("Ingrese la nota teórica del camper: "))
        nota_practica = float(input("Ingrese la nota práctica del camper: "))
        promedio = (nota_teorica + nota_practica) / 2
        inscripcion_encontrada["Promedio"] = promedio
        inscripcion_encontrada["Estado"] = "Aprobado" if promedio >= 60 else "Desaprobado"
        print("Notas registradas y estados actualizados.")
    else:
        print("No se encontró ninguna inscripción para el ID proporcionado.")


def areasEntrenamiento(camper):
    print("Areas de entrenamiento")
    for camper in camper:
        print(f"ID: {camper['# de identificación']}")
        print("1. NodeJS")
        print("2. Java")
        print("3. NetCore")
        area = input("Seleccione el área de entrenamiento para este camper: ")
        if area == "1":
            camper["Area de entrenamiento"] = "Sputnik"
        elif area == "2":
            camper["Area de entrenamiento"] = "Atermis"
        elif area == "3":
            camper["Area de entrenamiento"] = "Apolo"
        else:
            print("Opción no válida, se asignará el área Sputnik por defecto.")
            camper["Area de entrenamiento"] = "Sputnik"
        print()

inscripciones ={}
camper = abrirArchivo()
def menu():
    print("=====Menú=====")
print("1. Inscripciones")
print("2. Rutas de entrenamiento")
print("3. Registrar notas")
print("4. Áreas de entrenamiento")
opcion = int(input("Ingresa una opción: "))
if opcion == 1:
    camper = abrirArchivo()
    
    # Obtener el último ID asignado
    ultimo_id = 0
    for inscripcion in camper[0]["inscripciones"]:
        if 'id' in inscripcion and inscripcion["id"] > ultimo_id:
            ultimo_id = inscripcion["id"]

    
    campers = ultimo_id + 1
    
    nombre= input("Ingrese los nombres del camper: ")
    apellido = input("Ingrese los apellidos del camper: ")
    identificacion = input("Ingrese el número de identificación del camper: ")
    direccion = input("Ingrese la dirección del camper: ")
    acudiente = input("Ingrese el nombre del acudiente: ")
    telefonoCelular= input("Ingrese el número del camper: ")
    telefonoFijo= input("Ingrese un teléfono fijo del camper: ")
    ingreso= input("Ingrese el estado del camper (En proceso de ingreso, Inscrito, Aprobado, Cursando, Graduado, Expulsado, Retirado): ")
    
    # Agregar nueva inscripción con el nuevo ID
    camper[0]["inscripciones"].append(  
        {
            "id": campers,                    
            "nombre": nombre,
            "apellido": apellido,
            "identificacion": identificacion,
            "direccion": direccion,
            "acudiente": acudiente,
            "telefono_celular": telefonoCelular,
            "telefono_fijo": telefonoFijo,
            "estado": [
                {
                    "ingreso": ingreso
                    
                }]
        }
    )
    guardarArchivo(camper)
    print("guardado con exito")

    
if opcion == 2:
    rutasEntrenamiento(camper)
if opcion == 3:
    registrarNotas(camper)
if opcion == 4:
    areasEntrenamiento(camper)

menu()


