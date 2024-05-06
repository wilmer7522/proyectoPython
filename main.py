import json


def abrirArchivo():
    with open('info.json', encoding="utf-8") as openfile:
        return json.load(openfile)

def abrirArchivoRuta():
    with open('nuevasRutas.json', encoding="utf-8") as openfilerutas:
        return json.load(openfilerutas)
        

def guardarArchivo(miData):
    with open("info.json", "w") as outfile:
        json.dump(miData, outfile)

def guardarArchivoRuta(miDataRuta):
    with open("nuevasRutas.json", "w") as outfile:
        json.dump(miDataRuta, outfile)

camper = []
rutas = []

def procesar_inscripcion(camper):
    # Función para procesar la inscripción de un nuevo camper
    ultimo_id = 0
    for inscripcion in camper[0]["inscripciones"]:# Iterar sobre las inscripciones de los campers.
        if 'id' in inscripcion and inscripcion["id"] > ultimo_id:
            ultimo_id = inscripcion["id"]

    campers = ultimo_id + 1
    #Ingresar los datos del camper
    nombre = input("Ingrese los nombres del camper: ")
    apellido = input("Ingrese los apellidos del camper: ")
    identificacion = int(input("Ingrese el número de identificación del camper: "))
    direccion = input("Ingrese la dirección del camper: ")
    acudiente = input("Ingrese el nombre del acudiente: ")
    telefonoCelular = int(input("Ingrese el número de celular del camper: "))
    telefonoFijo = int(input("Ingrese un teléfono fijo del camper: "))
    valor = int(input("Ingrese el estado del camper\n1. En proceso de ingreso\n2. Inscrito\n"))
    if valor == 1:
        ingreso = "En proceso de inscripcion"
    elif valor == 2:
        ingreso = "Inscrito"
    else:
        print("")
        print("opción invalida intente de nuevo")
            
        
    #Guarda los datos ingresados anteriormente
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
                    
                }],
                
                "Promedio": 0,
                "rutaEntrenamiento": "",
                "horario": "",
                "riesgo": "",
                "trainer": "",
                "promedioGeneral": 0
                
        }                  
        
    )
    guardarArchivo(camper)
    print("Guardado con éxito.")

#Funcion para revisar los campers por medio del ID
def vercampers(camper):
    print("Buscar Camper")
    id_camper = input("Ingrese el ID del camper a verificar: ")
    camper_encontrado = None
    
    for inscripcion in camper[0]["inscripciones"]:# Iterar sobre las inscripciones de los campers.
        if str(inscripcion.get('id')) == id_camper:#se compara el id ingresado con la lista de todos los id en el json
            camper_encontrado = inscripcion #Guarda el ID del camper ingresado
            break
    #Imprime los datos del ID ingresado
    if camper_encontrado:
        print(f"ID: {camper_encontrado.get('id')}")
        print("####################")
        print(f"ID: {id_camper}")
        print(f"Nombre: {inscripcion['nombre']}")
        print(f"Apellido: {inscripcion['apellido']}")
        print(f"Estado: {inscripcion['estado'][0]['ingreso']}")
        print(f"Promedio: {inscripcion['Promedio']}")
        print(f"Riego: {inscripcion['riesgo']}")
        print(f"Ruta de Entrenamiento: {inscripcion['rutaEntrenamiento']}")
        print(f"Horario: {inscripcion['horario']}")
        print(f"Trainer: {inscripcion['trainer']}")
        print(f"Promedio General: {inscripcion["promedioGeneral"]}")
        
        print("#####################")
    else:
        print("No se encontró ningún camper con el ID proporcionado.")
        
#Funcion para registrar las notas del camper
def registrarNotas(camper):
    print("Registro de notas")
    id_camper = input("Ingrese el ID del camper: ")
    inscripcion_encontrada = None
    
    for inscripcion in camper[0]["inscripciones"]:# Iterar sobre las inscripciones de los campers.
        if str(inscripcion.get('id')) == id_camper:#Se compara el id ingresado con la lista de todos los id en el json
            inscripcion_encontrada = inscripcion#Guarda el id del camper ingresado
            break
    #Imprime algunos datos del ID ingresado
    if inscripcion_encontrada:# Si cumple la condicion imprime 
        print("####################")
        print(f"ID: {id_camper}")
        print(f"Nombre: {inscripcion['nombre']}")
        print(f"Apellido: {inscripcion['apellido']}")
        print(f"N° Identificacion: {inscripcion["identificacion"]}")
        print(f"Estado: {inscripcion['estado'][0]['ingreso']}")
        print(f"Ruta de entrenamiento: {inscripcion.get('rutaEntrenamiento', 'No asignada')}")
        print("#####################")
        nota_teorica = float(input("Ingrese la nota teórica del camper: "))
        nota_practica = float(input("Ingrese la nota práctica del camper: "))
        promedio = (nota_teorica + nota_practica) / 2 # Suma las dos notas y los divide en 2 para poder sacar el promedio de cada nota
        inscripcion_encontrada["Promedio"] = promedio #Imprime el promedio
        inscripcion_encontrada["estado"][0]["ingreso"] = "Aprobado" if promedio >= 60 else "Reprobado" #Comprueba si el promedio es mayor a 60 asigna el estado en aprobado o menor a 60 asigna reprobado
    if inscripcion_encontrada["estado"][0]["ingreso"] == "Aprobado": #Compara si es aprobado el riesgo sera bajo
        inscripcion_encontrada["riesgo"] = "Bajo"
        
        print("Camper aprobado.")
        print("")
        #Agregar fecha de inicio y de finalización
        fecha_inicio = input("Ingrese la  fecha de inicio (DD-MM-AAAA: )")
        print("")
        fecha_finalizacion = input("Ingrese la fecha de finalización (DD-MM-AAAA):")
        inscripcion_encontrada["fecha_inicio"]= fecha_inicio
        inscripcion_encontrada["fecha_finalizacion"] = fecha_finalizacion
        #Opcion para asignar rutas ya predefinidas y asignar la ruta previamente creada
        print("")
        print("1. Ruta NodeJS")
        print("2. Ruta Java")
        print("3. Ruta NetCore")
        print("4. Nueva Ruta ")
        print("")
                    
        ruta = int(input("Seleccione la ruta para este camper: "))
        if ruta == 1:
            if len([c for c in camper[0]["inscripciones"] if c.get("rutaEntrenamiento")=="Ruta NodeJS"]) >=33:#itera sobre todo el json para buscar rutaEntremaniento y asignar la ruta designada
                print("Lo siento, la ruta de entrenamiento NodeJS está llena.")
                return
            inscripcion_encontrada["rutaEntrenamiento"] = "ruta NodeJS"
            guardarArchivo(camper)
        elif ruta == 2:
            if len([c for c in camper[0]["inscripciones"] if c.get("rutaEntrenamiento")=="Ruta Java"]) >=33:
                print("Lo siento, la ruta de entrenamiento Java está llena.")
                return
            inscripcion_encontrada["rutaEntrenamiento"] = "ruta Java"
            guardarArchivo(camper)
        elif ruta == 3:
            if len([c for c in camper[0]["inscripciones"] if c.get("rutaEntrenamiento")=="Ruta NetCore"]) >=33:
                print("Lo siento, la ruta de entrenamiento NetCore está llena.")
                return
            inscripcion_encontrada["rutaEntrenamiento"] = "ruta NetCore"
            guardarArchivo(camper)
            
        elif ruta == 4:
            a = 0
            for i in rutas[0]["rutasNuevas"]:# Se itera sobre el JSON donde se alojan las nuevas rutas
                a = a + 1 
            print("###############################################")
            print(f"ID: {i["idRuta"]} Nombre: {i['nombre']}\nModulos: {i["modulos"]["Fundamentos de programacion"]}\n{i["modulos"]["Programacion Web"]}\n{i["modulos"]["Programacion formal"]}\n{i["modulos"]["Bases de datos"]["SGDB principal"]}\n{i["modulos"]["Bases de datos"]["SGDB alternativo"]}\n{i["modulos"]["Backend"]}")
            print("###############################################")
            nuevo = int(input("ingrese id de la Ruta Creada: ")) #Se ingresa el ID de la ruta que se va a buscar
            if len([c for c in rutas[0]["rutasNuevas"] if c.get("idRuta")== nuevo]) >=33: #Se busca y se compara con el id ingresado 
                print("Lo siento, la ruta de entrenamiento NetCore está llena.")
                return
            inscripcion_encontrada["rutaEntrenamiento"] = rutas[0]["rutasNuevas"][nuevo]#Al encontra el campo rutaEntrenamineto ya verificado el id se agrega la nueva ruta del id seleccionado antes
            guardarArchivo(camper)           
            print("Ruta asignada")
    else:
            print("Opción invalida")
            guardarArchivo(camper)
            print("Ingrese el area de estudio")
            print("")
    area = int(input("1. Sputnik\n2. Artemis\n3. Apollo\n"))
    if area == 1:
            inscripcion_encontrada["areaEntrenamiento"] = "Sputnik"
            guardarArchivo(camper)
            hora = int(input("ingrese horario:\n1. 6:00 - 10:00\n2. 10:00 - 14:00\n3. 14:00 - 18:00\n4. 18:00 - 22:00\n"))     
            if hora == 1:       
                if len([c for c in camper[0]["inscripciones"] if c.get("horario")=="6:00 - 10:00" if c.get("areaEntrenamient") == "Sputnik"]) >=33:
                    print("Lo siento, el horario para el area de Sputnik está lleno.")
                    return
                inscripcion_encontrada["horario"] = "6:00 - 10:00"
                guardarArchivo(camper)
                print("Camper Asignado")
            if hora == 2:
                if len([c for c in camper[0]["inscripciones"] if c.get("horario")=="10:00 - 14:00"]) >=33:
                    print("Lo siento, el horario para el area de Sputnik está lleno.")
                    return
                inscripcion_encontrada["horario"] = "10:00 - 14:00"
                guardarArchivo(camper)
                print("Camper Asignado")
            if hora == 3:
                if len([c for c in camper[0]["inscripciones"] if c.get("horario")=="14:00 - 18:00"]) >=33:
                    print("Lo siento, el horario para el area de Sputnik está lleno.")
                    return
                inscripcion_encontrada["horario"] = "14:00 - 18:00"
                guardarArchivo(camper)
                print("Camper Asignado")
            if hora == 4:
                if len([c for c in camper[0]["inscripciones"] if c.get("horario")=="18:00 - 22:00"]) >=33:
                    print("Lo siento, el horario para el area de Sputnik está lleno.")
                    return
                inscripcion_encontrada["horario"] = "18:00 - 22:00"
                guardarArchivo(camper)
                print("Camper Asignado")

    if area == 2:
            if len([c for c in camper[0]["inscripciones"] if c.get("areaEntrenamiento")=="Artemis"]) >=33:
                print("Lo siento, el área de entrenamiento Artemis está llena.")
                return
            inscripcion_encontrada["areaEntrenamiento"] = "Artemis"
            guardarArchivo(camper)
            hora = int(input("1. 6:00 - 10:00\n2. 10:00 - 14:00\n3. 14:00 - 18:00\n4. 18:00 - 22:00\n"))     
            if hora == 1:       
                if len([c for c in camper[0]["inscripciones"] if c.get("horario")=="6:00 - 10:00"]) >=33:
                    print("Lo siento, el horario para el área de Artemis está lleno.")
                    return
                inscripcion_encontrada["horario"] = "6:00 - 10:00"
                guardarArchivo(camper)
                print("Camper Asignado")
            if hora == 2:
                if len([c for c in camper[0]["inscripciones"] if c.get("horario")=="10:00 - 14:00"]) >=33:
                    print("Lo siento, el horario para el area de Artemis está lleno.")
                    return
                inscripcion_encontrada["horario"] = "10:00 - 14:00"
                guardarArchivo(camper)
                print("Camper Asignado")
            if hora == 3:
                if len([c for c in camper[0]["inscripciones"] if c.get("horario")=="14:00 - 18:00"]) >=33:
                    print("Lo siento, el horario para el area de Artemis está lleno.")
                    return
                inscripcion_encontrada["horario"] = "14:00 - 18:00"
                guardarArchivo(camper)
                print("Camper Asignado")
            if hora == 4:
                if len([c for c in camper[0]["inscripciones"] if c.get("horario")=="18:00 - 22:00"]) >=33:
                    print("Lo siento, el horario para el area de Artemis está lleno.")
                    return
                inscripcion_encontrada["horario"] = "18:00 - 22:00"
                guardarArchivo(camper)
                print("Camper Asignado")

    if area == 3:
            if len([c for c in camper[0]["inscripciones"] if c.get("areaEntrenamiento")=="Apollo"]) >=33:
                print("Lo siento, el area de entrenamiento Apollo está llena.")
                return
            inscripcion_encontrada["areaEntrenamiento"] = "Apollo"
            guardarArchivo(camper)
            hora = int(input("1. 6:00 - 10:00\n2. 10:00 - 14:00\n3. 14:00 - 18:00\n4. 18:00 - 22:00\n"))     
            if hora == 1:       
                if len([c for c in camper[0]["inscripciones"] if c.get("horario")=="6:00 - 10:00"]) >=33:
                    print("Lo siento, el horario para el area de Apollo está lleno.")
                    return
                inscripcion_encontrada["horario"] = "6:00 - 10:00"
                guardarArchivo(camper)
                print("Camper Asignado")
            if hora == 2:
                if len([c for c in camper[0]["inscripciones"] if c.get("horario")=="10:00 - 14:00"]) >=33:
                    print("Lo siento, el horario para el area de Apollo está lleno.")
                    return
                inscripcion_encontrada["horario"] = "10:00 - 14:00"
                guardarArchivo(camper)
                print("Camper Asignado")
            if hora == 3:
                if len([c for c in camper[0]["inscripciones"] if c.get("horario")=="14:00 - 18:00"]) >=33:
                    print("Lo siento, el horario para el area de Apollo está lleno.")
                    return
                inscripcion_encontrada["horario"] = "14:00 - 18:00"
                guardarArchivo(camper)
                print("Camper Asignado")
            if hora == 4:
                if len([c for c in camper[0]["inscripciones"] if c.get("horario")=="18:00 - 22:00"]) >=33:
                    print("Lo siento, el horario para el area de Apollo está lleno.")
                    return
                inscripcion_encontrada["horario"] = "18:00 - 22:00"

                guardarArchivo(camper)
                print("Camper Asignado")
    print("Ingrese el trainer que desea asignar:")
    trainer = int(input("1. Pedro Gomez\n2. Jholver Pardo\n3. Miguel Angel Castillo\n4. Juan Carlos Mariño\n"))
    if trainer == 1:
            
            if len([c for c in camper[0]["inscripciones"] if c.get("trainer")=="Pedro"]) >=33:
                return
            inscripcion_encontrada["trainer"] = "Pedro Gomez"
        
            guardarArchivo(camper)
            print("Trainer Pedro Asignado")
    
        
    if trainer == 2:
            if len([c for c in camper[0]["inscripciones"] if c.get("trainer")=="Jholver"]) >=33:
                print("Lo siento, el trainer ya fue asignado a otra ruta.")
                return
            inscripcion_encontrada["trainer"] = "Jholver Pardo"
            guardarArchivo(camper)
            print("Trainer Jholver Asignado")
    if trainer == 3:
            if len([c for c in camper[0]["inscripciones"] if c.get("trainer")=="Miguel"]) >=33:
                    print("Lo siento, el trainer ya fue asignado a otra ruta.")
                    return
            inscripcion_encontrada["trainer"] = "Miguel Angel Castillo"
            guardarArchivo(camper)
            print("Trainer Miguel Asignado")
    if trainer == 4:
            if len([c for c in camper[0]["inscripciones"] if c.get("trainer")=="Juan"]) >=33:
                    print("Lo siento, el trainer ya fue asignado a otra ruta.")
                    return
            inscripcion_encontrada["trainer"] = "Juan Carlos Mariño"

            guardarArchivo(camper)
            print("Trainer Juan Asignado")
        

    elif inscripcion_encontrada["estado"][0]["ingreso"] == "Reprobado":
        print("")
        print("Camper reprobado no puede ser admitido")
        guardarArchivo(camper)
        

def crearRutaEntrenamiento(rutas):
    
    print("Creación de nueva ruta de entrenamiento")
    print("Especifique los módulos para la nueva ruta:")
    nueva_id = 0
    for inscripcion in rutas[0]["rutasNuevas"]:
        if 'idRuta' in inscripcion and inscripcion["idRuta"] > nueva_id:
            nueva_id = inscripcion["idRuta"]

    nuevaRuta =nueva_id + 1
    modulo_fundamentos = "Introduccion a la algoritmia, PSeInt y Python"
    modulo_web = "HTML, CSS y Bootstrap"
    nombreNuevaRuta = str(input("Ingrese el Nombre de la nueva ruta "))
    print("Seleccione el módulo de Programación formal:")
    print("1. Java")
    print("2. JavaScript")
    print("3. C#")
    opcion_formal = int(input("Ingrese la opción deseada: "))
    if opcion_formal == 1:
        modulo_formal = "Java"
    elif opcion_formal == 2:
        modulo_formal = "JavaScript"
    elif opcion_formal == 3:
        modulo_formal = "C#"

        print("Seleccione el SGDB principal para la ruta de entrenamiento:")
    print("1. Mysql")
    print("2. MongoDb")
    print("3. Postgresql")
    opcion_sgdb_principal = int(input("Ingrese la opción deseada: "))
    if opcion_sgdb_principal == 1:
        sgdb_principal = "Mysql"
    elif opcion_sgdb_principal == 2:
        sgdb_principal = "MongoDb"
    elif opcion_sgdb_principal == 3:
        sgdb_principal = "Postgresql"

        print("Seleccione el SGDB alternativo para la ruta de entrenamiento:")
    print("1. Mysql")
    print("2. MongoDb")
    print("3. Postgresql")
    opcion_sgdb_alternativo = int(input("Ingrese la opción deseada: "))
    if opcion_sgdb_alternativo == 1:
        sgdb_alternativo = "Mysql"
    elif opcion_sgdb_alternativo == 2:
        sgdb_alternativo = "MongoDb"
    elif opcion_sgdb_alternativo == 3:
        sgdb_alternativo = "Postgresql"

        print("Seleccione el módulo de Backend:")
    print("1. NetCore")
    print("2. Spring Boot")
    print("3. NodeJS")
    print("4. Express")
    opcion_backend = int(input("Ingrese la opción deseada: "))
    if opcion_backend == 1:
        modulo_backend = "NetCore"
        guardarArchivo(camper)
    elif opcion_backend == 2:
        modulo_backend = "Spring Boot"
        guardarArchivo(camper)
    elif opcion_backend == 3:
        modulo_backend = "NodeJS"
        guardarArchivo(camper)
    elif opcion_backend == 4:
        modulo_backend = "Express"
        guardarArchivo(camper)
    

    rutas[0]["rutasNuevas"].append(
        {
                "idRuta": nuevaRuta,
                "nombre": nombreNuevaRuta,
                "modulos": {
                    "Fundamentos de programacion": modulo_fundamentos,
                    "Programacion Web": modulo_web,
                    "Programacion formal": modulo_formal,
                    "Bases de datos": {
                        "SGDB principal": sgdb_principal,
                        "SGDB alternativo": sgdb_alternativo
                    },
                    "Backend": modulo_backend
                }
                
            
            }
    )
    guardarArchivoRuta(rutas)
    print("Nueva ruta de entrenamiento creada con éxito.")

    

def evaluar_camper(camper):
    print("Evaluación de campers")
    id_camper = input("Ingrese el ID del camper a evaluar: ")

    # Buscar el camper por su ID
    camper_encontrado = None
    for inscripcion in camper[0]["inscripciones"]:
        if str(inscripcion.get('id')) == id_camper:
            camper_encontrado = inscripcion
            break
        
    if camper_encontrado:
        nota_teorica = float(input("Ingrese la nota teórica del camper: "))
        nota_practica = float(input("Ingrese la nota práctica del camper: "))
        trabajos = float(input("Ingrese la nota de los trabajos realizados por el camper: "))
        promedio = (nota_teorica * 0.3) + (nota_practica * 0.6) + (trabajos * 0.1)
        if promedio >= 60:
            camper_encontrado["estado"][0]["evaluacion"] = "Aprobado"
            camper_encontrado["promedioGeneral"] = promedio
        elif promedio <= 60:
            camper_encontrado["estado"][0]["evaluacion"] = "Reprobado"
            camper_encontrado["promedioGeneral"] = promedio
        print(f"Notas registradas y estado actualizado: {camper_encontrado['estado'][0]['evaluacion']}")
        guardarArchivo(camper)
        if promedio < 60:
            camper_encontrado["riesgo"]="Alto"
            print("El camper está en riesgo alto.")
            guardarArchivo(camper)

        else:
            camper_encontrado["riesgo"]="Bajo"
            guardarArchivo(camper)

    else:
        print("No se encontró ningún camper con el ID proporcionado.")

def listar_campers_inscritos(camper):
    print("Campers inscritos:")
    for inscripcion in camper[0]["inscripciones"]:
        if inscripcion.get("estado") and inscripcion["estado"][0]["ingreso"] in ["Inscrito"]:
        #if inscripcion["estado"][0]["ingreso"] == "Inscrito":
            print(f"Nombre: {inscripcion['nombre']} Apellido: {inscripcion['apellido']} Estado: {inscripcion["estado"][0]["ingreso"]}")
        guardarArchivo(camper)
def listar_campers_aprobados(camper):
    print("Campers que aprobaron el examen inicial:")
    for inscripcion in camper[0]["inscripciones"]:
        if inscripcion.get("estado") and inscripcion["estado"][0]["ingreso"] in ["Aprobado"]:
        #if inscripcion["estado"][0]["ingreso"] == "Aprobado":
            print(f"Nombre: {inscripcion['nombre']} Apellido: {inscripcion['apellido']} Estado: {inscripcion["estado"][0]["ingreso"]}")
        guardarArchivo(camper)
def listar_trainers(camper):
    print("Trainers trabajando con CampusLands:")
    trainers_mostrados = set()
    for inscripcion in camper[0]["inscripciones"]:
        if inscripcion.get("trainer") and inscripcion["trainer"] in ["Pedro Gomez", "Jholver Pardo", "Miguel Angel Castillo", "Juan Carlos Mariño"]:
            trainer = inscripcion["trainer"]
            if trainer not in trainers_mostrados:
                print(trainer)
                trainers_mostrados.add(trainer)
    guardarArchivo(camper)


def listar_campers_bajo_rendimiento(camper):
    print("Campers con bajo rendimiento:")
    for inscripcion in camper[0]["inscripciones"]:# Iterar sobre las inscripciones de los campers.
        promedio = inscripcion.get("promedioGeneral") # Obtener el promedio general de los campers
        if promedio is not None and promedio < 60:# Verificar si el promedio es válido y bajo (menor o igual a 60)
            print(f" {inscripcion['nombre']} {inscripcion['apellido']} Promedio: {inscripcion["promedioGeneral"]}") 
        guardarArchivo(camper)
def listar_campers_trainer_ruta(camper):
    print("Campers y Trainers asociados a una ruta de entrenamiento:")
    for inscripcion in camper[0]["inscripciones"]:
        if inscripcion.get("rutaEntrenamiento"):
            print(f"Camper: ID:{inscripcion["id"]} Nombre: {inscripcion['nombre']} Apellido: {inscripcion['apellido']}, Trainer: {inscripcion.get('trainer', 'No asignada')}, Ruta: {inscripcion['rutaEntrenamiento']}")
            print("")
        guardarArchivo(camper)
def listar_aprobados_y_reprobados(camper):
    print("Aprobados y reprobados por módulo:")
    for inscripcion in camper[0]["inscripciones"]:
        if inscripcion.get("estado") and inscripcion["estado"][0].get("evaluacion"):
            print(f"Camper: ID: {inscripcion["id"]} Nombre: {inscripcion['nombre']} Apellido: {inscripcion['apellido']}, Ruta: {inscripcion.get('rutaEntrenamiento', 'No asignada')}, Trainer: {inscripcion.get('trainer', 'No asignado')}, Evaluación: {inscripcion['estado'][0]['evaluacion']}")

# Definir contraseñas para el coordinador y el entrenador
contrasena_coordinador = "1234"
contrasena_trainer = "abcd"

def menu():
    print("")
    print("=====Menú General=====")
    print("1. Camper")
    print("2. Trainer")
    print("3. Coordinador")
    opcion = int(input("Ingrese una opción: "))
    
    if opcion == 1:
        print("Elija la opción deseada:")
        a = int(input("1. Ver Campers "))
        if a == 1:
            vercampers(camper)
        else:
            print("Opción no válida.")
    
    elif opcion == 2:
        print("Ingrese la contraseña del trainer:")
        contrasena_ingresada = input()
        if contrasena_ingresada == contrasena_trainer:
            print("Elija la opción deseada:")
            a = int(input("\n1. Ver Campers "))
            if a == 1:
                vercampers(camper)
            else:
                print("Contraseña incorrecta. Acceso denegado.")
        else:
            print("Contraseña incorrecta. Acceso denegado.")
    
    elif opcion == 3:
        print("Ingrese la contraseña del coordinador:")
        contrasena_ingresada = input()
        if contrasena_ingresada == contrasena_coordinador:
            print("Elija la opción deseada:")
            a = int(input("1. Procesar Inscripción\n2. Registrar Notas\n3. Evaluar Camper\n4. Crear Ruta de Entrenamiento\n5. Listar Campers Inscritos\n6. Listar Campers Aprobados\n7. Listar Campers con Rendimiento Bajo\n8. Listar Campers con Ruta de Trainer\n9. Listar Campers Aprobados y Reprobados\n10. Listar Trainers "))
            if a == 1:
                procesar_inscripcion(camper)
            elif a == 2:
                registrarNotas(camper)
            elif a == 3:
                evaluar_camper(camper)
            elif a == 4:
                crearRutaEntrenamiento(camper)
            elif a == 5:
                listar_campers_inscritos(camper)
            elif a == 6:
                listar_campers_aprobados(camper)
            elif a == 7:
                listar_campers_bajo_rendimiento(camper)
            elif a == 8:
                listar_campers_trainer_ruta(camper)
            elif a == 9:
                listar_aprobados_y_reprobados(camper)
            elif a == 10:
                listar_trainers(camper)
            else:
                print("Contraseña incorrecta. Acceso denegado.")
        else:
            print("Contraseña incorrecta. Acceso denegado.")

camper = abrirArchivo()
rutas = abrirArchivoRuta()
while True:
    menu()
