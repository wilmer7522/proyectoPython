import json

database = "python/info.json"

def abrirArchivo():
    with open('info.json', encoding="utf-8") as openfile:
        return json.load(openfile)

def guardarArchivo(miData):
    with open("info.json", "w") as outfile:
        json.dump(miData, outfile)

camper = []

def procesar_inscripcion(camper):
    # Función para procesar la inscripción de un nuevo camper
    ultimo_id = 0
    for inscripcion in camper[0]["inscripciones"]:
        if 'id' in inscripcion and inscripcion["id"] > ultimo_id:
            ultimo_id = inscripcion["id"]

    campers = ultimo_id + 1
    
    nombre = input("Ingrese los nombres del camper: ")
    apellido = input("Ingrese los apellidos del camper: ")
    identificacion = int(input("Ingrese el número de identificación del camper: "))
    direccion = input("Ingrese la dirección del camper: ")
    acudiente = input("Ingrese el nombre del acudiente: ")
    telefonoCelular = int(input("Ingrese el número de celular del camper: "))
    telefonoFijo = int(input("Ingrese un teléfono fijo del camper: "))
    ingreso = "Proceso de Inscripcion"#input("Ingrese el estado del camper (En proceso de ingreso, Inscrito, Aprobado, Cursando, Graduado, Expulsado, Retirado): ")
    
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
    print("Guardado con éxito.")

def vercampers(camper):
    print("Buscar Camper")
    id_camper = input("Ingrese el ID del camper a verificar: ")
    camper_encontrado = None
    
    for inscripcion in camper[0]["inscripciones"]:
        if str(inscripcion.get('id')) == id_camper:
            camper_encontrado = inscripcion
            break
    
    if camper_encontrado:
        print(f"ID: {camper_encontrado.get('id')}")
        print("####################")
        print(f"ID: {id_camper}")
        print(f"Nombre: {inscripcion['nombre']}")
        print(f"Apellido: {inscripcion['apellido']}")
        print(f"Estado: {inscripcion['estado'][0]['ingreso']}")
        print("#####################")
    else:
        print("No se encontró ningún camper con el ID proporcionado.")

def rutasEntrenamiento(camper):
    print("Rutas de entrenamiento")
    id_camper = input("Ingrese el ID del camper: ")
    camper_encontrado = None
    
    for inscripcion in camper[0]["inscripciones"]:
        if str(inscripcion.get('id')) == id_camper:
            camper_encontrado = inscripcion
            break
    
    if camper_encontrado:
        print(f"ID: {camper_encontrado.get('id')}")
        print("####################")
        print(f"ID: {id_camper}")
        print(f"Nombre: {inscripcion['nombre']}")
        print(f"Apellido: {inscripcion['apellido']}")
        print(f"Estado: {inscripcion['estado'][0]['ingreso']}")
        print("#####################")
        print("")
        print("1. Ruta NodeJS")
        print("2. Ruta Java")
        print("3. Ruta NetCore")
        print("")
        ruta = input("Seleccione la ruta para este camper: ")
        if ruta == "1":
            if len([c for c in camper[0]["inscripciones"] if c.get("rutaEntrenamiento")=="Ruta NodeJS"]) >=33:
                print("Lo siento, la ruta de entrenamiento NodeJS está llena.")
                return
            camper_encontrado["rutaEntrenamiento"] = "ruta NodeJS"
            guardarArchivo(camper)
        elif ruta == "2":
            if len([c for c in camper[0]["inscripciones"] if c.get("rutaEntrenamiento")=="Ruta Java"]) >=33:
                print("Lo siento, la ruta de entrenamiento Java está llena.")
                return
            camper_encontrado["rutaEntrenamiento"] = "ruta Java"
            guardarArchivo(camper)
        elif ruta == "3":
            if len([c for c in camper[0]["inscripciones"] if c.get("rutaEntrenamiento")=="Ruta NetCore"]) >=33:
                print("Lo siento, la ruta de entrenamiento NetCore está llena.")
                return
            camper_encontrado["rutaEntrenamiento"] = "ruta NetCore"
            guardarArchivo(camper)
        else:
            print("Opción no válida, se asignará la Ruta NodeJS por defecto.")
            camper_encontrado["rutaEntrenamiento"] = "Ruta NodeJS"
        print("Asignación de ruta completada.")
        guardarArchivo(camper)
    else:
        print("No se encontró ningún camper con el ID proporcionado.")

def registrarNotas(camper):
    print("Registro de notas")
    id_camper = input("Ingrese el ID del camper: ")
    inscripcion_encontrada = None
    
    for inscripcion in camper[0]["inscripciones"]:
        if str(inscripcion.get('id')) == id_camper:
            inscripcion_encontrada = inscripcion
            break
    
    if inscripcion_encontrada:
        print("####################")
        print(f"ID: {id_camper}")
        print(f"Nombre: {inscripcion['nombre']}")
        print(f"Apellido: {inscripcion['apellido']}")
        print(f"Estado: {inscripcion['estado'][0]['ingreso']}")
        print(f"Ruta de entrenamiento: {inscripcion.get('rutaEntrenamiento', 'No asignada')}")
        print("#####################")
        nota_teorica = float(input("Ingrese la nota teórica del camper: "))
        nota_practica = float(input("Ingrese la nota práctica del camper: "))
        promedio = (nota_teorica + nota_practica) / 2
        inscripcion_encontrada["Promedio"] = promedio
        inscripcion_encontrada["estado"][0]["ingreso"] = "Aprobado" if promedio >= 60 else "Reprobado"
        if inscripcion_encontrada["estado"][0]["ingreso"] == "Aprobado":
            print("Camper aprobado.")
            rutasEntrenamiento(camper)#yo lo habia hecho asi pero no me cuadro por lo que hay que volver a colocar el id 
        print("#####################")
        guardarArchivo(camper)
    else:
        print("No se encontró ninguna inscripción para el ID proporcionado.")

def areasEntrenamiento(camper):
    print("Áreas de entrenamiento")
    id_camper = input("Ingrese el ID del camper: ")
    inscripcion_encontrada = None
    
    for inscripcion in camper[0]["inscripciones"]:
        if str(inscripcion.get('id')) == id_camper:
            inscripcion_encontrada = inscripcion
            break
    
    if inscripcion_encontrada:
        print(f"ID: {id_camper}")
        print(f"Nombre: {inscripcion['nombre']}")
        print(f"Apellido: {inscripcion['apellido']}")
        print(f"Estado: {inscripcion['estado'][0]['ingreso']}")
        print(f"Ruta de entrenamiento: {inscripcion.get('rutaEntrenamiento', 'No asignada')}")
        print("#####################")
        print("1. Sputnik")
        print("2. Artemis")
        print("3. Apolo")
        area = input("Seleccione el área de entrenamiento para este camper: ")
        if area == "1":
            inscripcion_encontrada["Area de entrenamiento"] = "Sputnik"
            guardarArchivo(camper)
        elif area == "2":
            inscripcion_encontrada["Area de entrenamiento"] = "Artemis"
            guardarArchivo(camper)
        elif area == "3":
            inscripcion_encontrada["Area de entrenamiento"] = "Apolo"
            guardarArchivo(camper)
        else:
            print("Opción no válida, se asignará el área Sputnik por defecto.")
            inscripcion_encontrada["Area de entrenamiento"] = "Sputnik"
            guardarArchivo(camper)
        print("Asignación de área de entrenamiento completada.")
    else:
        print("No se encontró ninguna inscripción para el ID proporcionado.")

def crearRutaEntrenamiento(camper):
    print("Creación de nueva ruta de entrenamiento")
    print("Especifique los módulos para la nueva ruta:")
    
    # Módulos con opciones predefinidas
    modulo_fundamentos = "Introduccion a la algoritmia, PSeInt y Python"
    modulo_web = "HTML, CSS y Bootstrap"
    
    # Módulo de Programación formal con opciones para elegir
    print("Seleccione el módulo de Programación formal:")
    print("1. Java")
    print("2. JavaScript")
    print("3. C#")
    opcion_formal = input("Ingrese la opción deseada: ")
    if opcion_formal == "1":
        modulo_formal = "Java"
    elif opcion_formal == "2":
        modulo_formal = "JavaScript"
    elif opcion_formal == "3":
        modulo_formal = "C#"
    else:
        print("Opción no válida. Se asignará Java por defecto.")
        modulo_formal = "Java"
    
    # Módulo de Bases de datos con opciones para elegir SGDB principal y alternativo
    print("Seleccione el SGDB principal para la ruta de entrenamiento:")
    print("1. Mysql")
    print("2. MongoDb")
    print("3. Postgresql")
    opcion_sgdb_principal = input("Ingrese la opción deseada: ")
    if opcion_sgdb_principal == "1":
        sgdb_principal = "Mysql"
    elif opcion_sgdb_principal == "2":
        sgdb_principal = "MongoDb"
    elif opcion_sgdb_principal == "3":
        sgdb_principal = "Postgresql"
    else:
        print("Opción no válida. Se asignará Mysql por defecto.")
        sgdb_principal = "Mysql"
    
    print("Seleccione el SGDB alternativo para la ruta de entrenamiento:")
    print("1. Mysql")
    print("2. MongoDb")
    print("3. Postgresql")
    opcion_sgdb_alternativo = input("Ingrese la opción deseada: ")
    if opcion_sgdb_alternativo == "1":
        sgdb_alternativo = "Mysql"
    elif opcion_sgdb_alternativo == "2":
        sgdb_alternativo = "MongoDb"
    elif opcion_sgdb_alternativo == "3":
        sgdb_alternativo = "Postgresql"
    else:
        print("Opción no válida. Se asignará Mysql por defecto.")#hacer un bucle para condicionar si elige mal
        sgdb_alternativo = "Mysql"
    
    # Módulo de Backend con opciones para elegir
    print("Seleccione el módulo de Backend:")
    print("1. NetCore")
    print("2. Spring Boot")
    print("3. NodeJS")
    print("4. Express")
    opcion_backend = input("Ingrese la opción deseada: ")
    if opcion_backend == "1":
        modulo_backend = "NetCore"
        guardarArchivo(camper)
    elif opcion_backend == "2":
        modulo_backend = "Spring Boot"
        guardarArchivo(camper)
    elif opcion_backend == "3":
        modulo_backend = "NodeJS"
        guardarArchivo(camper)
    elif opcion_backend == "4":
        modulo_backend = "Express"
        guardarArchivo(camper)
    else:
        print("Opción no válida. Se asignará NetCore por defecto.")
        modulo_backend = "NetCore"
    
    horario = input("Ingrese el horario de clases para esta ruta: ")
    limite_estudiantes = 33  # El límite siempre es 33 para todas las rutas

    nombre_ruta = input("Ingrese el nombre de la nueva ruta de entrenamiento: ")

    rutas_existentes = [ruta.get("nombre") for ruta in camper]
    if nombre_ruta in rutas_existentes:
        print("La ruta de entrenamiento ya existe.")
        return

    nueva_ruta = {
        "nombre": nombre_ruta,
        "modulos": {
            "Fundamentos de programacion": modulo_fundamentos,
            "Programacion Web": modulo_web,
            "Programacion formal": modulo_formal,
            "Bases de datos": {
                "SGDB principal": sgdb_principal,
                "SGDB alternativo": sgdb_alternativo
            },
            "Backend": modulo_backend
        },
        "Horario": horario,
        "Limite de estudiantes": limite_estudiantes
    }
    camper.append(nueva_ruta)
    guardarArchivo(camper)
    print("Nueva ruta de entrenamiento creada con éxito.")

def asignarCamperRuta(camper):
    print("Asignar camper a ruta de entrenamiento")
    id_camper = input("Ingrese el ID del camper: ")
    inscripcion_encontrada = None
    
    for inscripcion in camper[0]["inscripciones"]:
        if str(inscripcion.get('id')) == id_camper:  
            inscripcion_encontrada = inscripcion
            break
    
    if inscripcion_encontrada and inscripcion_encontrada["estado"][0]["ingreso"] == "Aprobado":
        print("Camper aprobado. Puede ser asignado a una ruta de entrenamiento.")
        rutasEntrenamiento(camper)
    else:
        print("El camper no ha sido aprobado o no se encontró ninguna inscripción para el ID proporcionado.")
    guardarArchivo(camper)

def menu():
    print("")
    print("=====Menú=====")
    print("1. Inscripciones")
    print("2. Rutas de entrenamiento")
    print("3. Registrar notas")
    print("4. Áreas de entrenamiento")
    print("5. Crear nuevas rutas")
    print("6. Asignar camper a ruta de entrenamiento")
    print("7. Buscar camper")
    opcion = int(input("Ingrese una opción: "))
    
    if opcion == 1:
        procesar_inscripcion(camper)
    elif opcion == 2:
        rutasEntrenamiento(camper)
    elif opcion == 3:
        registrarNotas(camper)
    elif opcion == 4:
        areasEntrenamiento(camper)
    elif opcion == 5:
        crearRutaEntrenamiento(camper)
    elif opcion == 6:
        asignarCamperRuta(camper)
    elif opcion == 7:
        vercampers(camper)
    else:
        print("Opción no válida.")

camper = abrirArchivo()
menu()
