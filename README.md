Proyecto Final: CRUD con Arquitectura MVC en Python
Este proyecto es una aplicación de consola simple que implementa operaciones CRUD (Crear, Leer, Actualizar, Eliminar) utilizando el patrón de diseño Modelo-Vista-Controlador (MVC). Su propósito principal es servir como un ejemplo práctico y educativo para entender la separación de responsabilidades en el desarrollo de software.
🎯 Propósito del Proyecto
El objetivo de este repositorio es demostrar de forma clara y minimalista los siguientes conceptos fundamentales:
Arquitectura Limpia: Cómo estructurar el código para que sea mantenible, escalable y fácil de entender.
Interacción con Bases de Datos: Uso de un ORM (Peewee) para manipular datos sin escribir consultas SQL directamente.
Buenas Prácticas: Gestión correcta de dependencias a través de entornos virtuales y un archivo requirements.txt bien definido.
✨ Conceptos Clave Demostrados
Separación de Responsabilidades (MVC):
Modelo (models.py): Gestiona los datos y la lógica de negocio. Es el único que interactúa con la base de datos.
Vista (view.py): Se encarga exclusivamente de presentar los datos al usuario y capturar sus entradas. No contiene ninguna lógica.
Controlador (controller.py): Actúa como el intermediario, procesando las entradas del usuario, interactuando con el Modelo y seleccionando la Vista a mostrar.
ORM (Object-Relational Mapping): La librería Peewee mapea las tablas de la base de datos a clases de Python, permitiendo una interacción más intuitiva y segura con los datos.
Gestión de Dependencias: El uso de requirements.txt asegura que cualquier desarrollador pueda replicar el entorno de ejecución exacto, mientras que el .gitignore previene que archivos innecesarios (como el entorno virtual) sean subidos al repositorio.
🛠️ Stack Tecnológico
Lenguaje: Python 3
Base de Datos: SQLite
ORM: Peewee
🚀 Puesta en Marcha
Sigue estos pasos para ejecutar el proyecto localmente. Es crucial utilizar un entorno virtual para mantener las dependencias aisladas.
1. Clonar el Repositorio
code
Bash
git clone https://github.com/eironm3n/ProyectoFinal.git
cd ProyectoFinal
2. Crear y Activar el Entorno Virtual
Este comando crea una carpeta .venv en tu proyecto que contendrá las librerías necesarias.
code
Bash
# Crear el entorno virtual
python -m venv .venv

# Activar el entorno (los comandos varían según tu sistema operativo)
# Windows:
.\.venv\Scripts\activate

# macOS / Linux:
source .venv/bin/activate
Notarás que el entorno está activo porque (.venv) aparecerá al inicio de la línea de tu terminal.
3. Instalar Dependencias
Este comando lee el archivo requirements.txt e instala las versiones exactas de las librerías necesarias dentro de tu entorno virtual.
code
Bash
pip install -r requirements.txt
4. Ejecutar la Aplicación
Con el entorno virtual activado y las dependencias instaladas, ejecuta el controlador, que es el punto de entrada de la aplicación.
code
Bash
python controller.py
La aplicación se iniciará en tu terminal y te mostrará un menú de opciones para interactuar con ella.
📂 Estructura del Repositorio
Archivo	Componente	Descripción
controller.py	Controlador	Orquesta la aplicación, maneja la lógica de flujo y conecta el Modelo con la Vista.
models.py	Modelo	Define la estructura de la base de datos y los métodos para interactuar con los datos.
view.py	Vista	Contiene todas las funciones que imprimen información en pantalla y reciben datos del usuario.
base.db	Base de Datos	Archivo de SQLite que almacena la información.
requirements.txt	Dependencias	Lista las librerías de Python necesarias para que el proyecto funcione.
.gitignore	Config. Git	Especifica los archivos y directorios que Git debe ignorar.