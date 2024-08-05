# Proyecto de Gestión de Campers
Este proyecto proporciona una aplicación para gestionar campers, permitiendo realizar diversas operaciones sobre la información almacenada en un archivo JSON. El sistema permite crear, leer, modificar y eliminar registros de campers a través de una interfaz en la línea de comandos.

## Tabla de contenidos
| Indice | Titulo  |
|--|--|
| 1 | Descripción |
| 2 | Funcionalidades |
| 3 | Notas Importantes |

### Instalación
Deberas ejecutar el comando git clone para copiar el repositorio
  [Link](https://github.com/wilmer7522/proyectoPython.git)

``` bash
sudo apt install app
```

``` Código realizado en:
- python
```
## Descripción
Este proyecto utiliza un archivo JSON para almacenar la información de los campers, incluyendo ID, nombre, modelo, y año. La aplicación permite realizar las siguientes acciones:
- Crear un nuevo camper: Añadir un camper al archivo JSON con la información proporcionada.
- Leer campers: Mostrar la información de todos los campers almacenados.
- Modificar un camper: Actualizar los datos de un camper existente basado en su ID.
- Eliminar un camper: Borrar un camper específico del archivo JSON utilizando su ID.
  
## Funcionalidades
- Crear Camper: Permite ingresar un nuevo camper con ID, nombre, modelo, y año. Los datos se guardan en el archivo campers.json.
- Leer Camper: Muestra la información de todos los campers almacenados en el archivo JSON.
- Modificar Camper: Actualiza la información de un camper existente. Puedes cambiar el nombre, modelo o año.
- Eliminar Camper: Permite eliminar un camper específico utilizando su ID.

Hecho por ***Karen Lorena Cristancho Caceres***

> Notas Importantes
> [!NOTE]
> Asegúrate de que el archivo campers.json existe en el directorio raíz del proyecto para que el script funcione correctamente.

> [!TIP]
> Mantén el archivo JSON bien estructurado y asegúrate de que todos los campers tienen un ID único para evitar problemas al modificar o eliminar registros.

> [!IMPORTANT]
> Verifica los datos ingresados para evitar errores en el archivo JSON. Los años deben ser enteros y representativos del año de fabricación.

> [!WARNING]
> El archivo campers.json puede sobrescribirse si hay errores en el script, por lo que es recomendable hacer copias de seguridad periódicas.

> [!CAUTION]
> Asegúrate de manejar correctamente los IDs para evitar confusiones entre campers y para garantizar que las modificaciones y eliminaciones se realicen en el camper correcto.
