import json

def abrirArchivo():
    with open('info.json', encoding="utf-8") as openfile:
        return json.load(openfile)

def guardarArchivo(miData):
    with open("info.json", "w") as outfile:
        json.dump(miData, outfile)

def procesar_inscripcion(inscripciones):
    camper = {}
    camper["id"] = len(inscripciones) + 1
    camper["nombre"] = input("Ingrese los nombres del camper: ")
    camper["apellido"] = input("Ingrese los apellidos del camper: ")
    camper["direccion"] = input("Ingrese la dirección del camper: ")
    camper["acudiente"] = input("Ingrese el nombre del acudiente: ")
    camper["telefono_celular"] = input("Ingrese el número de teléfono celular del camper: ")
    camper["telefono_fijo"] = input("Ingrese el número de teléfono fijo del camper: ")
    camper["estado"] = input("Ingrese el estado del camper (En proceso de ingreso, Inscrito, Aprobado, Cursando, Graduado, Expulsado, Retirado): ")
    camper["riesgo"] = input("Ingrese el nivel de riesgo del camper: ")
    print("Seleccione una ruta de entrenamiento: ")
    print("1. Ruta NodeJS")
    print("2. Ruta Java")
    print("3. Ruta NetCore")
    opcion = int(input("Ingrese el número de la ruta deseada: "))
    if opcion == 1:
        camper["ruta_de_entrenamiento"] = "Ruta NodeJS"
    elif opcion == 2:
        camper["ruta_de_entrenamiento"] = "Ruta Java"
    elif opcion == 3:
        camper["ruta_de_entrenamiento"] = "Ruta NetCore"
    inscripciones.append(camper)
    guardarArchivo({"inscripciones": inscripciones})
    print("Inscripción realizada exitosamente.")

def mostrar_campers(inscripciones):
    for camper in inscripciones:
        print("ID: ", camper["id"])
        print("Nombres: ", camper["nombre"])
        print("Apellidos: ", camper["apellido"])
        print("Direccion: ", camper["direccion"])
        print("Acudiente: ", camper["acudiente"])
        print("Telefono celular: ", camper["telefono_celular"])
        print("Telefono fijo: ", camper["telefono_fijo"])
        print("Estado: ", camper["estado"])
        print("Riesgo: ", camper["riesgo"])
        print("Ruta de entrenamiento: ", camper.get("ruta_de_entrenamiento", "No asignada"))

def registrar_notas(inscripciones):
    id_camper = int(input("Ingrese el ID del camper: "))
    for camper in inscripciones:
        if camper["id"] == id_camper:
            nota_teorica = float(input("Ingrese la nota teórica: "))
            nota_practica = float(input("Ingrese la nota práctica: "))
            promedio = (nota_teorica + nota_practica) / 2
            if promedio >= 60:
                print("El camper ha aprobado la prueba.")
                camper["estado"] = "Aprobado"
            else:
                print("El camper no ha aprobado la prueba.")
            guardarArchivo({"inscripciones": inscripciones})
            break
    else:
        print("No se encontró ningún camper con ese ID.")

def menu():
    miInfo = abrirArchivo()
    inscripciones = miInfo
    print("========Menú========")
    print("1. Procesar inscripción.")
    print("2. Mostrar campers")
    print("3. Registrar notas")
    opcion = int(input("Ingrese la opción deseada: "))
    if opcion == 1:
        procesar_inscripcion(inscripciones)
    elif opcion == 2:
        mostrar_campers(inscripciones)
    elif opcion == 3:
        registrar_notas(inscripciones)

menu()
