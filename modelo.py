import sqlite3
from tkinter import messagebox
import re
from tkinter import simpledialog



class Modelo(self):
    var_id = StringVar()
    var_producto = StringVar()
    var_cantidad = IntVar()
    var_precio = IntVar()

    def __init__(self):
        try:
            self.conexionBD
        except:
            print("La base de datos ya esta creada")
    
    #Aquí se conecta a la base de datos o la crea en caso de que no exista
    def conexionBD():
        miConexion = sqlite3.connect("base.db")
        miCursor = miConexion.cursor()
        try:
            miCursor.execute('''CREATE TABLE planilla(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            PRODUCTO VARCHAR(80) NOT NULL,
            CANTIDAD INT(4) NOT NULL,
            PRECIO INT NOT NULL)''')
            messagebox.showinfo("CONEXION", "Base de Datos Creada exitosamente")
        except:
            messagebox.showinfo("CONEXION", "Conexión exitosa con la base de datos")
    
    #Crear base de datos
    def crear(self):
        miConexion = sqlite3.connect("base.db")
        miCursor = miConexion.cursor()
        try:
            datos = var_producto.get(), var_cantidad.get(), var_precio.get()
            miCursor.execute("INSERT INTO planilla VALUES(NULL,?,?,?)", datos)
            miConexion.commit()
        except:
            messagebox.showwarning("AVERTENCIA", "Ocurrió un error al crear el registro")
            pass
        limpiarCampos()
        mostrar()

    def seleccionarUsandoClick(event):
        item = tree.identify("item", event.x, event.y)
        var_id.set(tree.item(item, "text"))
        var_producto.set(tree.item(item, "values")[0])
        var_cantidad.set(tree.item(item, "values")[1])
        var_precio.set(tree.item(item, "values")[2])

    # Mostrar la información de la tabla con datos
    def mostrar(self):
        miConexion = sqlite3.connect("base.db")
        miCursor = miConexion.cursor()
        registros = tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        try:
            miCursor.execute("SELECT * FROM planilla")
            for row in miCursor:
                tree.insert("", 0, text=row[0], values=(row[1], row[2], row[3]))
        except:
            pass

    def actualizar(self):
        miConexion = sqlite3.connect("base.db")
        miCursor = miConexion.cursor()
        try:
            datos = var_producto.get(), var_cantidad.get(), var_precio.get()
            miCursor.execute('UPDATE planilla SET PRODUCTO=?, CANTIDAD=?, PRECIO=? WHERE ID=' + var_id.get(),(datos),)
            miConexion.commit()
        except:
            messagebox.showwarning("ADVERTENCIA", "Ocurrió un error al actualizar el registro")
            pass
        limpiarCampos()
        mostrar()


    def borrar(self):
        miConexion = sqlite3.connect("base.db")
        miCursor = miConexion.cursor()
        try:
            if messagebox.askyesno(title="ADVERTENCIA", message="¿Realmente desea eliminar el registro?"):
                miCursor.execute('DELETE FROM planilla WHERE ID=' + var_id.get())
                miConexion.commit()

        except:
            messagebox.showwarning(title="ADVERTENCIA", message="Ocurrió un error al eliminar el registro")
            pass
        limpiarCampos()
        mostrar()


    def buscar(self):
        miConexion = sqlite3.connect("base.db")
        miCursor = miConexion.cursor()

        patron = simpledialog.askstring("Buscar", "Introduzca el patrón de búsqueda:")

        registros = miCursor.execute('SELECT * FROM planilla')
        resultados = []
        for registro in registros:
            if re.search(patron, registro[1]):
                resultados.append(registro)

        for elemento in tree.get_children():
            tree.delete(elemento)

        for resultado in resultados:
            tree.insert("", 0, text=resultado[0], values=(resultado[1], resultado[2], resultado[3]))


    def eliminarBD(self):
        miConexion = sqlite3.connect("base.db")
        miCursor = miConexion.cursor()
        if messagebox.askyesno (message="Los datos se perderan definitivamente, ¿Desea continuar?", title="ADVERTENCIA",):
            miCursor.execute("DROP TABLE planilla")
        else:
            pass
        limpiarCampos()
        mostrar()


    def salirAplicacion(self):
        valor = messagebox.askquestion ("Salir", "Esta seguro que desea salir de la aplicación")
        if valor == "yes":
            root.destroy()


    def limpiarCampos(self):
        var_id.set("")
        var_producto.set("")
        var_cantidad.set("")
        var_precio.set("")


    def mensaje(self):
        acerca = """
        Aplicación CRUD
        Version 1.0
        Tecnología Python Tkinter
        """
        messagebox.showinfo(title="INFORMACIÓN", message=acerca)