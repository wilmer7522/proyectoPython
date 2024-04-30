import json
database = "python/info.json"

def abrirArchivo():
    with open('info.json', encoding="utf-8") as openfile:
        return json.load(openfile)

def guardarArchivo(miData):
    with open("info.json", "w") as outfile:
        json.dump(miData, outfile)

camper=[]

def procesar_inscripcion(camper):
    ultimo_id = 0
    # Obtener el último ID asignado
    for inscripcion in camper[0]["inscripciones"]:
        if 'id' in inscripcion and inscripcion["id"] > ultimo_id:
            ultimo_id = inscripcion["id"]

    
    campers = ultimo_id + 1
    
    nombre= input("Ingrese los nombres del camper: ")
    apellido = input("Ingrese los apellidos del camper: ")
    identificacion = int(input("Ingrese el número de identificación del camper: "))
    direccion = input("Ingrese la dirección del camper: ")
    acudiente = input("Ingrese el nombre del acudiente: ")
    telefonoCelular= int(input("Ingrese el numero de celular del camper: "))
    telefonoFijo= int(input("Ingrese un teléfono fijo del camper: "))
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
   
def rutasEntrenamiento(camper):
    horarios = {
        "Ruta NodeJS": ["6:00 - 10:00", "10:00 - 14:00", "14:00 - 18:00"],
        "Ruta Java":["6:00 - 10:00", "10:00 - 14:00", "14:00 - 18:00"],
        "Ruta NetCore":["6:00 - 10:00", "10:00 - 14:00", "14:00 - 18:00"]
    }
    print("Rutas de entrenamiento")
    id_camper = input("Ingrese el ID del camper: ")
    camper_encontrado = None
    
    # Buscar el camper con el ID proporcionado dentro de las inscripciones
    for inscripcion in camper[0]["inscripciones"]:
        if str(inscripcion.get('id')) == id_camper:  # Convertir a cadena para comparar con entrada de usuario
            camper_encontrado = inscripcion
            #print(f"camper {camper_encontrado}Nombre {"nombre"}")
            break
    
    if camper_encontrado:
        print(f"ID: {camper_encontrado.get('id')}")
        print("####################")
        print(f"ID: {id_camper}")
        print(f"Nombre: {inscripcion["nombre"]}")
        print(f"Apellido: {inscripcion["apellido"]}")
        print(f"Estado: {inscripcion["estado"][0]["ingreso"]}")
        #print(f"Ruta de entrenamiento: {inscripcion["rutaEntrenamiento"]}")
        print("#####################")
        print("")
        print("1. Ruta NodeJS")
        print("2. Ruta Java")
        print("3. Ruta NetCore")
        print("")
        ruta = input("Seleccione la ruta para este camper: ")
        if ruta == "1":
            if len([c for c in camper[0]["inscripciones"] if c.get("rutaEntrenamiento")=="Ruta NodeJS"]) >=33:
                print("Lo siento, la ruta de entrenamiento NodeJS esta llena.")
                return
            camper_encontrado["rutaEntrenamiento"] = "ruta NodeJS"
        elif ruta == "2":
            if len([c for c in camper[0]["inscripciones"] if c.get("rutaEntrenamiento")=="Ruta Java"]) >=33:
                print("Lo siento, la ruta de entrenamiento Java esta llena.")
                return
            camper_encontrado["rutaEntrenamiento"] = "ruta Java"
        elif ruta == "3":
            if len([c for c in camper[0]["inscripciones"] if c.get("rutaEntrenamiento")=="Ruta NetCore"]) >=33:
                print("Lo siento, la ruta de entrenamiento NetCore esta llena.")
                return
            camper_encontrado["rutaEntrenamiento"] = "ruta NetCore"
        else:
            print("Opción no válida, se asignará la Ruta NodeJS por defecto.")
            camper_encontrado["rutaEntrenamiento"] = "Ruta NodeJS"
        print("Asignación de ruta completada.")
        print("Horarios de clases para esta ruta: ")#, horarios[camper_encontrado["rutaEntrenamiento"]]
        
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
        print("####################")
        print(f"ID: {id_camper}")
        print(f"Nombre: {inscripcion["nombre"]}")
        print(f"Apellido: {inscripcion["apellido"]}")
        print(f"Estado: {inscripcion["estado"][0]["ingreso"]}")
        print(f"Ruta de entrenamiento: {inscripcion["rutaEntrenamiento"]}")
        print("#####################")
        nota_teorica = float(input("Ingrese la nota teórica del camper: "))
        nota_practica = float(input("Ingrese la nota práctica del camper: "))
        promedio = (nota_teorica + nota_practica) / 2
        inscripcion_encontrada["Promedio"] = promedio
        inscripcion_encontrada["Estado"] = "Aprobado" if promedio >= 60 else "Reprobado"
        print("Notas registradas y estados actualizados.")
        guardarArchivo(camper)  # Guardar cambios en el archivo JSON
    else:
        print("No se encontró ninguna inscripción para el ID proporcionado.")

def areasEntrenamiento(camper):
    print("Areas de entrenamiento")
    id_camper = input("Ingrese el ID del camper: ")
    inscripcion_encontrada = None
    
    # Buscar la inscripción con el ID proporcionado
    for inscripcion in camper[0]["inscripciones"]:
        if str(inscripcion.get('id')) == id_camper:  # Convertir a cadena para comparar con entrada de usuario
            inscripcion_encontrada = inscripcion
            break
    
    if inscripcion_encontrada:
        print(f"ID: {id_camper}")
        print(f"Nombre: {inscripcion["nombre"]}")
        print(f"Apellido: {inscripcion["apellido"]}")
        print(f"Estado: {inscripcion["estado"][0]["ingreso"]}")
        print(f"Ruta de entrenamiento: {inscripcion["rutaEntrenamiento"]}")
        print("#####################")
        print("1. Sputnik")
        print("2. Artemis")
        print("3. Apolo")
        area = input("Seleccione el área de entrenamiento para este camper: ")
        if area == "1":
            inscripcion_encontrada["Area de entrenamiento"] = "Sputnik"
        elif area == "2":
            inscripcion_encontrada["Area de entrenamiento"] = "Artemis"
        elif area == "3":
            inscripcion_encontrada["Area de entrenamiento"] = "Apolo"
        else:
            print("Opción no válida, se asignará el área Sputnik por defecto.")
            inscripcion_encontrada["Area de entrenamiento"] = "Sputnik"
            guardarArchivo(camper)  # Guardar cambios en el archivo JSON
        print("Asignación de área de entrenamiento completada.")
        
    else:
        print("No se encontró ninguna inscripción para el ID proporcionado.")

def crearRutaEntrenamiento(camper):
    # Solicitar los datos para la nueva ruta de entrenamiento
    print("Creación de nueva ruta de entrenamiento")
    nombre_ruta = input("Ingrese el nombre de la nueva ruta de entrenamiento: ")
    modulo_fundamentos = input("Ingrese el módulo de Fundamentos de Programación (Introducción a la algoritmia, PSeInt y Python): ")
    modulo_web = input("Ingrese el módulo de Programación Web (HTML, CSS y Bootstrap): ")
    modulo_formal = input("Ingrese el módulo de Programación formal (Java, JavaScript, C#): ")
    sgdb_principal = input("Ingrese el SGDB principal de la ruta de entrenamiento: ")
    sgdb_alternativo = input("Ingrese el SGDB alternativo de la ruta de entrenamiento: ")
    horario = input("Ingrese el horario de clases para esta ruta: ")
    limite_estudiantes = int(input("Ingrese el límite de estudiantes para esta ruta: "))

    # Verificar que la ruta no exista previamente
    rutas_existente = [ruta.get("nombre") for ruta in camper]
    if nombre_ruta in rutas_existente:
        print("Lo siento, la ruta de entrenamiento ya existe.")
        return

    # Agregar la nueva ruta de entrenamiento al archivo JSON
    nueva_ruta = {
        "nombre": nombre_ruta,
        "modulos": {
            "Fundamentos de programación": modulo_fundamentos,
            "Programación Web": modulo_web,
            "Programación formal": modulo_formal,
            "Bases de datos": {
                "SGDB principal": sgdb_principal,
                "SGDB alternativo": sgdb_alternativo
            },
            "Backend": {
                "Horario": horario,
                "Límite de estudiantes": limite_estudiantes
            }
        }
    }
    camper.append(nueva_ruta)
    guardarArchivo(camper)
    print("Nueva ruta de entrenamiento creada con éxito.")


inscripciones ={}
camper = abrirArchivo()
def menu():
    print("=====Menú=====")
print("1. Inscripciones")
print("2. Rutas de entrenamiento")
print("3. Registrar notas")
print("4. Áreas de entrenamiento")
print("5. Crear nuevas rutas")
opcion = int(input("Ingresa una opción: "))
if opcion == 1:
    procesar_inscripcion(camper)
if opcion == 2:
    rutasEntrenamiento(camper)
if opcion == 3:
    registrarNotas(camper)
if opcion == 4:
    areasEntrenamiento(camper)
if opcion == 5:
    crearRutaEntrenamiento(camper)

menu()


