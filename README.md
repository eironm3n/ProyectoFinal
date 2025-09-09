Proyecto Final - Demo de Arquitectura MVC en Python
Este repositorio contiene un proyecto simple en Python que demuestra la implementación del patrón de diseño Modelo-Vista-Controlador (MVC). Sí, es un proyecto pequeño, y su objetivo principal es servir como un recurso educativo técnico para entender conceptos clave de la arquitectura de software y las buenas prácticas de desarrollo en Python.
Objetivos de Aprendizaje
Al explorar este repositorio, podrás aprender sobre:
Patrón de Diseño MVC: Comprender cómo separar las responsabilidades de una aplicación en tres componentes interconectados:
Modelo: La lógica de los datos y las reglas de negocio.
Vista: La representación de los datos (la interfaz de usuario).
Controlador: El intermediario que maneja las entradas del usuario y conecta el Modelo y la Vista.
Manejo de Bases de Datos con un ORM: Se utiliza la librería Peewee como un Mapeador Objeto-Relacional (ORM) para interactuar con una base de datos SQLite de una manera más "Pythónica", sin escribir SQL crudo.
Gestión de Dependencias Profesional:
La importancia de usar entornos virtuales (.venv) para aislar las dependencias del proyecto.
Cómo mantener un archivo requirements.txt limpio y conciso, conteniendo solo las librerías necesarias para que la aplicación funcione, excluyendo herramientas de desarrollo.
Seguridad en Dependencias: Entender la importancia de mantener las librerías actualizadas para corregir vulnerabilidades de seguridad, tal como lo notifican herramientas como Dependabot de GitHub.
Stack Tecnológico
Lenguaje: Python 3
Base de Datos: SQLite (a través del archivo base.db)
ORM: Peewee
Instalación y Puesta en Marcha
Para ejecutar este proyecto en tu máquina local, sigue estos pasos. Es fundamental crear un entorno virtual para no instalar paquetes en tu sistema global.
1. Clona el repositorio:
code
Bash
git clone https://github.com/eironm3n/ProyectoFinal.git
cd ProyectoFinal
2. Crea y activa un entorno virtual:```bash
Crear el entorno (esto crea una carpeta .venv)
python -m venv .venv
Activar el entorno
En Windows:
..venv\Scripts\activate
En macOS / Linux:
source .venv/bin/activate
code
Code
*Sabrás que está activado porque el nombre de tu terminal mostrará `(.venv)` al principio.*

**3. Instala las dependencias:**
Con el entorno activado, instala las librerías necesarias desde el archivo `requirements.txt`.
```bash
pip install -r requirements.txt
Uso del Proyecto
Una vez que las dependencias estén instaladas, puedes ejecutar la aplicación a través del script principal (probablemente el controlador):
code
Bash
python controller.py
Al ejecutar el script, se iniciará la aplicación en la consola y podrás interactuar con ella a través de las opciones que presente.
Estructura del Repositorio
models.py: (Modelo) Define la estructura de la base de datos (tablas y columnas) usando clases de Peewee. Aquí reside toda la lógica de los datos.
view.py: (Vista) Contiene las funciones responsables de mostrar información al usuario y de recibir las entradas (inputs) del mismo. No contiene lógica de negocio.
controller.py: (Controlador) Es el cerebro de la aplicación. Orquesta el flujo, recibe peticiones de la Vista, pide datos al Modelo y se los devuelve a la Vista para que los muestre.
base.db: El archivo de la base de datos SQLite.
requirements.txt: El listado de las dependencias de Python que necesita el proyecto para funcionar.
.gitignore: Un archivo que le dice a Git qué archivos y carpetas ignorar (como la carpeta .venv).
