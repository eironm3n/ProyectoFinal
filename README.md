# ProyectoFinal - Aplicación CRUD con Patrón MVC

Una aplicación de consola educativa que demuestra la implementación del patrón Modelo-Vista-Controlador (MVC) con operaciones CRUD en Python.

## 🎯 Objetivo

Este proyecto sirve como ejemplo práctico para entender la separación de responsabilidades en el desarrollo de software, demostrando conceptos fundamentales como arquitectura limpia, interacción con bases de datos y buenas prácticas de desarrollo.

## 🏗️ Arquitectura MVC

### Modelo (`models.py`)
- **Responsabilidad**: Gestiona los datos y la lógica de negocio
- **Función**: Único punto de interacción con la base de datos
- **Implementación**: Utiliza ORM Peewee para mapear tablas a clases Python

### Vista (`view.py`) 
- **Responsabilidad**: Presentación de datos y captura de entradas del usuario
- **Función**: Interfaz de usuario sin lógica de negocio
- **Implementación**: Funciones de entrada y salida por consola

### Controlador (`controller.py`)
- **Responsabilidad**: Intermediario entre Modelo y Vista
- **Función**: Procesa entradas, ejecuta lógica y selecciona vistas
- **Implementación**: Punto de entrada de la aplicación

## 🛠️ Tecnologías

- **Lenguaje**: Python 3
- **Base de Datos**: SQLite
- **ORM**: Peewee
- **Gestión de Dependencias**: pip + requirements.txt

## 🚀 Instalación y Ejecución

### Prerrequisitos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/eironm3n/ProyectoFinal.git
cd ProyectoFinal
```

2. **Crear entorno virtual**
```bash
python -m venv .venv
```

3. **Activar entorno virtual**

**Windows:**
```bash
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

> 💡 **Nota**: Verás `(.venv)` al inicio de tu terminal cuando esté activo

4. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

5. **Ejecutar la aplicación**
```bash
python controller.py
```

## 📂 Estructura del Proyecto

```
ProyectoFinal/
├── controller.py      # Controlador principal - Punto de entrada
├── models.py          # Modelos de datos y lógica de negocio
├── view.py            # Interfaz de usuario y presentación
├── base.db            # Base de datos SQLite (generada automáticamente)
├── requirements.txt   # Dependencias del proyecto
├── .gitignore        # Archivos ignorados por Git
└── README.md         # Documentación del proyecto
```

## 📋 Funcionalidades

- ✅ **Crear** registros en la base de datos
- ✅ **Leer** y mostrar información almacenada
- ✅ **Actualizar** registros existentes
- ✅ **Eliminar** registros de la base de datos

## 🎓 Conceptos Demostrados

### Arquitectura Limpia
- Separación clara de responsabilidades
- Código mantenible y escalable
- Estructura fácil de entender y modificar

### ORM (Object-Relational Mapping)
- Mapeo automático de tablas a clases Python
- Interacción intuitiva con la base de datos
- Abstracción de consultas SQL

### Buenas Prácticas
- Uso de entornos virtuales
- Gestión de dependencias con `requirements.txt`
- Configuración correcta de `.gitignore`

## 🤝 Contribuir

- Gracias a Ariel Caruso y Guido por su apoyo durante este proyecto.

## 📝 Notas de Desarrollo

- La base de datos `base.db` se crea automáticamente al ejecutar la aplicación por primera vez
- El entorno virtual `.venv` está incluido en `.gitignore` para evitar conflictos
- Las dependencias están fijadas a versiones específicas para garantizar consistencia

## 🆘 Resolución de Problemas

### La aplicación no inicia
- Verifica que el entorno virtual esté activado
- Asegúrate de haber instalado las dependencias: `pip install -r requirements.txt`

### Error de permisos en la base de datos
- Verifica que tengas permisos de escritura en el directorio del proyecto
- En sistemas Unix, puedes usar: `chmod 755 base.db`

---

⭐ Si este proyecto te resultó útil, ¡no dudes en darle una estrella!